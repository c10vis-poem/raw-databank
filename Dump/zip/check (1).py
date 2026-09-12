#!/usr/bin/env python3
"""
tools/check.py  --  the RLVR check.  01-sources + 02-clean  ->  03-check.

HARD RULE 5: nothing self-certifies.  This tool shares no code and no method
with tools/clean.py.  It does not import it.

                   tools/clean.py                 tools/check.py
    ------------  -----------------------------  -------------------------------
    pdf            pymupdf  fitz page.get_text()  pypdf  PdfReader.extract_text()
    docx           pandoc docx -> markdown        stdlib zipfile + xml.etree over
                                                  word/document.xml, headers,
                                                  footers, foot/endnotes, and
                                                  document.xml.rels hyperlinks
    html           pandoc html -> plain           stdlib html.parser, one text
                                                  node at a time, tag boundaries
                                                  kept, alt/title captured
    text           open().read()                  byte read + BOM/encoding probe
    zip            skipped                        opened and enumerated

    comparison     collections.Counter multiset   containment of named atoms and
                   difference of word frequencies order-sensitive segments in a
                   over the whole file            fold-and-squash character
                                                  stream, greedy chunk splitting
                                                  to name the culprit, plus an
                                                  exact line-level difflib audit
                                                  where extraction is faithful

There is no word-frequency counting anywhere in this file, and no percentage is
ever reported.  Every finding carries the verbatim text it is about.

    python3 tools/check.py            # write 03-check/
    python3 tools/check.py --dry-run  # print the roll-up, write nothing
"""

import datetime
import difflib
import io
import json
import os
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

SRC, CLEAN, OUT = "01-sources", "02-clean", "03-check"
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- normalising

# Zero-width marks and the BOM.  They carry no content, so they must not create
# a false difference — but a BOM left sitting inside a markdown body is worth
# saying out loud, so it is reported separately.
_INVISIBLE = dict.fromkeys(map(ord, "​‌‍⁠﻿­᠎"), None)

_LIGATURES = {"Æ": "AE", "æ": "ae", "Œ": "OE", "œ": "oe", "ß": "ss",
              "Ø": "O", "ø": "o", "Đ": "D", "đ": "d", "Ł": "L", "ł": "l",
              "Ð": "D", "þ": "th", "Þ": "Th"}


def fold(s):
    """Unicode -> comparable ASCII-ish.  Applied to both sides, always."""
    s = unicodedata.normalize("NFKC", s).translate(_INVISIBLE)
    s = "".join(_LIGATURES.get(c, c) for c in s)
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


_NOTALNUM = re.compile(r"[^a-z0-9]+")


def squash(s):
    """Every separator gone.  'CHIP SM8750' and 'CHIPSM8750' both become
    'chipsm8750', so a value welded to its neighbour is still found.  This is
    what makes the fused-token blind spot visible."""
    return _NOTALNUM.sub("", fold(s).lower())


def wordstream(s):
    """Every separator collapsed to one space, wrapped in spaces.  Word
    boundaries survive here, so comparing this against squash() says whether a
    boundary was destroyed."""
    return " " + _NOTALNUM.sub(" ", fold(s).lower()).strip() + " "


# ---------------------------------------------------------------- extraction

def extract_pdf(path):
    import pypdf
    reader = pypdf.PdfReader(path)
    pages = [(pg.extract_text() or "") for pg in reader.pages]
    return ("\n".join(pages),
            "pypdf %s PdfReader.extract_text()" % pypdf.__version__,
            {"pages": len(pages)})


_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
_M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
_DOCX_PARTS = ("word/document.xml", "word/header1.xml", "word/header2.xml",
               "word/header3.xml", "word/footer1.xml", "word/footer2.xml",
               "word/footer3.xml", "word/footnotes.xml", "word/endnotes.xml",
               "word/comments.xml")


def _docx_walk(el, out):
    for child in el:
        tag = child.tag
        if tag in (_W + "t", _W + "delText", _W + "instrText", _M + "t"):
            out.append(child.text or "")
        elif tag == _W + "tab":
            out.append("\t")
        elif tag in (_W + "br", _W + "cr"):
            out.append("\n")
        elif tag == _W + "hyperlink":
            # consecutive hyperlinks in one paragraph have no separator of
            # their own; welding them here would manufacture a finding
            out.append("\n")
            _docx_walk(child, out)
            out.append("\n")
        else:
            _docx_walk(child, out)
        if tag in (_W + "p", _W + "tr"):
            out.append("\n")
        elif tag == _W + "tc":
            out.append("\t")


def extract_docx(path):
    chunks, seen, urls = [], [], []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        for part in _DOCX_PARTS:
            if part not in names:
                continue
            seen.append(part)
            out = []
            _docx_walk(ET.fromstring(z.read(part)), out)
            chunks.append("".join(out))
        # Hyperlink targets live in the .rels, not in the paragraph text.
        # pandoc renders them into the markdown, so they have to be checkable.
        if "word/_rels/document.xml.rels" in names:
            for rel in ET.fromstring(z.read("word/_rels/document.xml.rels")):
                t = rel.get("Target", "")
                if t.startswith("http") or t.startswith("mailto:"):
                    urls.append(t)
        if urls:
            chunks.append("\n".join(urls))
    return ("\n".join(chunks),
            "stdlib zipfile + xml.etree over %s%s" % (
                ", ".join(seen),
                " + document.xml.rels hyperlink targets" if urls else ""),
            {"docx_parts": len(seen), "rel_urls": len(urls)})


class _HTMLText(HTMLParser):
    """One text node at a time, with a hard boundary at every tag.

    pandoc's html->plain renders adjacent inline elements with no separator,
    which is how <span>CHIP</span><span>SM8750</span> became CHIPSM8750.
    Keeping the boundary is the entire reason to extract it differently.
    """
    SKIP = {"script", "style", "noscript", "title"}   # containers only
    VOID = {"br", "hr", "img", "meta", "link", "input", "source", "col",
            "area", "base", "embed", "param", "track", "wbr"}
    ATTRS = ("alt", "title", "aria-label")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
            return
        self.out.append("\n")
        if self.skip:
            return
        for k, v in attrs:
            if k in self.ATTRS and v:
                self.out.append(v + "\n")

    def handle_startendtag(self, tag, attrs):
        # self-closing: never opens a region
        if tag in self.SKIP:
            return
        self.out.append("\n")
        if self.skip:
            return
        for k, v in attrs:
            if k in self.ATTRS and v:
                self.out.append(v + "\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if tag in self.VOID:
            return
        self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def extract_html(path):
    raw, enc, bom = _read_text(path)
    p = _HTMLText()
    p.feed(raw)
    p.close()
    text = "".join(p.out)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]*\n+", "\n", text)
    return (text,
            "stdlib html.parser, tag boundaries preserved (decoded %s)" % enc,
            {"encoding": enc, "bom": bom})


def extract_zip(path):
    listing, texts = [], []
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            listing.append("%s\t%d bytes" % (info.filename, info.file_size))
            if info.file_size and re.search(
                    r"\.(md|txt|json|ya?ml|py|sh|toml|cfg|ini)$", info.filename, re.I):
                try:
                    texts.append("=== %s ===\n%s" % (
                        info.filename, z.read(info).decode("utf-8", "replace")))
                except Exception:
                    pass
    return ("\n".join(listing) + "\n" + "\n".join(texts),
            "stdlib zipfile — archive opened and enumerated",
            {"members": len(listing), "text_members": len(texts)})


def _read_text(path):
    data = open(path, "rb").read()
    bom = data.startswith(b"\xef\xbb\xbf")
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return data.decode(enc), enc, bom
        except UnicodeDecodeError:
            continue
    return data.decode("latin-1", "replace"), "latin-1/replace", bom


def extract_text(path):
    raw, enc, bom = _read_text(path)
    return (raw.replace("\r\n", "\n").replace("\r", "\n"),
            "byte read, decoded %s%s" % (enc, " (BOM stripped)" if bom else ""),
            {"encoding": enc, "bom": bom, "bytes": os.path.getsize(path)})


def kind_of(path):
    with open(path, "rb") as f:
        head = f.read(8)
    if head.startswith(b"%PDF"):
        return "pdf"
    ext = path.rsplit(".", 1)[-1].lower() if "." in os.path.basename(path) else ""
    if head.startswith(b"PK\x03\x04"):
        return "docx" if ext == "docx" else "zip"
    if ext in ("html", "htm"):
        return "html"
    return "text"


EXTRACTORS = {"pdf": extract_pdf, "docx": extract_docx, "html": extract_html,
              "zip": extract_zip, "text": extract_text}

# Extraction is byte-faithful only for plain text.  An exact line-level audit
# is valid there and nowhere else.
EXACT = {"text"}


# ------------------------------------------------------- the documented spec
#
# Transcribed by hand from README.md -> "The one job".  This is the *policy*,
# not clean.py's implementation of it.  A line counts as furniture only if it
# is made of nothing but these fragments; anything else that went missing is a
# finding, whatever the cleaner called it.

CHROME = [
    ("browser/app chrome", re.compile(
        r"Use code with caution\.?|Ask anything|AI Mode"
        r"|All\s+Images\s+Videos\s+News\s+Maps\s+Shopping\s+Books\s+Flights\s+Finance"
        r"|Try without personalization|Search Labs|Sign in"
        r"|Show more|Show less|\bMore\b|\bTools\b"
        r"|\d+\s+sites?\b", re.I)),
]
PAGE_NUMBER = ("page number", re.compile(r"^\s*(?:page\s+)?[-–—]?\s*\d{1,4}\s*(?:/\s*\d{1,4}\s*)?[-–—]?\s*$", re.I))


def furniture_class(line, kind):
    """Name the furniture rule a line falls under, or None if it is content."""
    if not line.strip():
        return "blank line"
    if kind == "pdf" and PAGE_NUMBER[1].match(line):
        return PAGE_NUMBER[0]
    residue = line
    hit = None
    for name, rx in CHROME:
        new = rx.sub(" ", residue)
        if new != residue:
            hit = name
        residue = new
    if hit and not re.sub(r"[^\w]", "", residue):
        return hit
    return None


# ---------------------------------------------------------------- the atoms
#
# Named, typed details.  Each is looked for by containment; none is counted.

ATOM_RULES = [
    ("url", re.compile(r"(?:https?://|www\.|drive://|file://|git@)[^\s<>\"'()\[\]{}]+")),
    ("email", re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")),
    ("hash/key", re.compile(r"\b(?:[0-9a-f]{16,}|gh[pousr]_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("measurement", re.compile(
        r"\b\d[\d,]*(?:\.\d+)?\s*(?:[-–—]\s*\d[\d,]*(?:\.\d+)?\s*)?"
        r"(?:GB|MB|KB|TB|GiB|MiB|KiB|TOPS|GHz|MHz|kHz|Hz|ms|fps|dpi|px|%|bytes?|"
        r"tokens?|pages?|files?|cores?|threads?|USD|W)\b")),
    ("version", re.compile(r"\bv?\d+\.\d+(?:\.\d+)*(?:[A-Za-z]\w*)?\b")),
    ("path", re.compile(r"(?:[A-Za-z0-9_.~\-]+/){1,}[A-Za-z0-9_.\-]+")),
    ("identifier", re.compile(
        r"\b(?:[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+"       # snake_case / SCREAMING
        r"|[A-Za-z]{2,}\d[A-Za-z0-9]*"                   # SM8750, v79
        r"|\d+[A-Za-z]{2,}[A-Za-z0-9]*)\b")),            # 3APK
    ("acronym", re.compile(r"\b[A-Z][A-Z0-9]{2,9}\b")),
    ("date", re.compile(r"\b(?:20\d\d[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]20\d\d)\b")),
    ("number", re.compile(r"\b\d[\d,]*(?:\.\d+)?\b")),
]

MIN_MISSING = 3    # squashed length below which absence cannot be asserted
MIN_FUSED = 4      # squashed length below which a substring hit means nothing
MIN_SEGMENT = 24   # squashed length of a segment worth checking as a whole


_RUNCHAR = re.compile(r"[A-Za-z0-9._\-\u2013/]")


def find_atoms(lines):
    """-> ([(klass, verbatim, line_no)], n_unjudgeable), deduped on (klass, text).

    An atom is only usable if THIS checker's own extractor produced it as a
    complete run.  pypdf welds tightly-set figure cells (0.40 and 0.95 arrive
    as 0.400.95); demanding that a fragment of that appear as a standalone
    token in the cleaned file would invent a failure that is the checker's own
    fault.  Fragments are counted and set aside, never asserted.
    """
    seen, atoms, skipped = set(), [], 0
    for n, line in lines:
        for klass, rx in ATOM_RULES:
            for m in rx.finditer(line):
                before = line[m.start() - 1] if m.start() > 0 else ""
                after = line[m.end()] if m.end() < len(line) else ""
                if (before and _RUNCHAR.match(before)) or (after and _RUNCHAR.match(after)):
                    skipped += 1
                    continue
                v = m.group(0).strip(".,;:)]}'\"")
                key = (klass, v)
                if not v or key in seen:
                    continue
                seen.add(key)
                atoms.append((klass, v, n))
    return atoms, skipped


def judge_atom(verbatim, hay_sq, hay_ws):
    """INTACT | RESPACED | FUSED | MISSING | None (too short to judge)"""
    a_sq, a_ws = squash(verbatim), wordstream(verbatim).strip()
    if len(a_sq) < MIN_MISSING:
        return None
    if a_ws and (" " + a_ws + " ") in hay_ws:
        return "INTACT"
    if a_sq not in hay_sq:
        return "MISSING"
    if len(a_sq) < MIN_FUSED:
        return None
    return "FUSED" if a_ws and a_ws in hay_ws else "RESPACED"


# -------------------------------------------------------------- the segments

_SENT = re.compile(r"(?<=[.!?;])\s+")


def segments(lines):
    """Order-sensitive units.  A word-frequency diff is blind to these: every
    word can be present and the sentence still gone."""
    out = []
    for n, line in lines:
        line = line.strip()
        if not line:
            continue
        parts = _SENT.split(line) if len(line) > 300 else [line]
        for p in parts:
            if len(squash(p)) >= MIN_SEGMENT:
                out.append((p.strip(), n))
    return out


def chunk_split(seg, hay_sq):
    """Greedily cover a segment with the fewest contiguous runs that each
    survive in the cleaned file.  -> [(text, survived)].

    One chunk  = the phrase survived intact.
    Two chunks = a line break moved; the words are all there, in order.
    More, or a chunk marked False = something to report by name.
    """
    words = [w for w in seg.split() if w]
    chunks, i, n = [], 0, len(words)
    while i < n:
        j = n
        while j > i and squash(" ".join(words[i:j])) not in hay_sq:
            j -= 1
        if j == i:
            chunks.append((words[i], False))
            i += 1
        else:
            chunks.append((" ".join(words[i:j]), True))
            i = j
    return chunks


# ------------------------------------------------------------- the two ends

TAIL_STEPS = (400, 250, 150, 80, 40)
_ENDS_CLOSED = re.compile(r"[.!?…\"'”’)\]}|:*_`—–-]\s*$")
_BARE_TAG = re.compile(r"^\s*</?[A-Za-z][\w:-]*\s*/?>\s*$")


EDGE_CHARS = 60


def edge_block(content, head):
    """The first (or last) content lines of the source, enough of them to make
    EDGE_CHARS squashed characters."""
    seq = content if head else list(reversed(content))
    acc, got = 0, []
    for _n, line in seq:
        if not line.strip():
            continue
        got.append(line)
        acc += len(squash(line))
        if acc >= EDGE_CHARS:
            break
    return "\n".join(got if head else reversed(got))


def edge_check(content, hay_sq, head):
    """-> (block, [pieces of it that are nowhere in the cleaned file]).

    Chunk-based rather than one contiguous run: pypdf and pymupdf disagree
    about icon glyphs and line breaks at the very end of a page, and that
    disagreement is not a truncation.  A piece that is nowhere at all is."""
    block = edge_block(content, head)
    if not squash(block):
        return block, []
    return block, [c for c, ok in chunk_split(block, hay_sq) if not ok]


def last_real_line(text):
    """The last line that is actually prose, ignoring a trailing wrapper tag
    such as the </content> that Drive text exports end with."""
    for line in reversed(text.rstrip().split("\n")):
        if line.strip() and not _BARE_TAG.match(line):
            return line.strip()
    return ""


def looks_truncated(text):
    """Does the SOURCE itself stop mid-thought?  Upstream defect if so —
    reported, never repaired."""
    last = last_real_line(text)
    if not last or _ENDS_CLOSED.search(last):
        return None
    if re.match(r"^(#{1,6}\s|[-*+]\s|\d+[.)]\s|\||```|---|===|\{|\})", last):
        return None
    if len(last.split()) < 3:
        return None
    return last[-100:]


# ------------------------------------------------------------------- pairing

def read_clean(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    fm, body = {}, raw
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 3)
        if end != -1:
            for line in raw[4:end].split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
            body = raw[end + 5:]
    return fm, body


def build_pairs():
    """Pair by the `source:` line the cleaned file already declares.  Reading a
    declaration is not the same as trusting a verdict."""
    sources = sorted(
        os.path.relpath(os.path.join(r, f), SRC).replace("\\", "/")
        for r, _, fs in os.walk(SRC) for f in fs if not f.startswith("MANIFEST"))
    by_source, orphans = {}, []
    for r, _, fs in os.walk(CLEAN):
        for f in sorted(fs):
            cp = os.path.join(r, f).replace("\\", "/")
            fm, body = read_clean(cp)
            key = fm.get("source", "")
            if not key:
                orphans.append((cp, "no `source:` line in frontmatter"))
            elif key in by_source:
                orphans.append((cp, "second file claiming source %r" % key))
            elif key not in sources:
                orphans.append((cp, "claims source %r, which is not in %s/" % (key, SRC)))
            else:
                by_source[key] = (cp, fm, body)
    return sources, by_source, orphans


# ------------------------------------------------------------------ checking

MAX_LIST = 40


def q(s, n=170):
    s = s.replace("\n", "\\n")
    return "`" + (s[:n] + "…" if len(s) > n else s).replace("`", "'") + "`"


def check_one(rel, clean_path, body):
    src_path = os.path.join(SRC, rel)
    kind = kind_of(src_path)
    findings, notes = [], []

    try:
        src, extractor, meta = EXTRACTORS[kind](src_path)
    except Exception as ex:
        findings.append(("FAIL", "extraction failed",
                         "the checker could not read %s independently" % rel,
                         "%s: %s" % (type(ex).__name__, ex)))
        return "ERROR", findings, notes, kind, "n/a", {}, None

    if clean_path is None:
        findings.append((
            "FAIL", "no counterpart",
            "%s has no file in %s/" % (rel, CLEAN),
            "%d characters of text were extracted from this source by an "
            "independent reader (%s) and none of them are anywhere in the "
            "corpus." % (len(src.strip()), extractor)))
        return "NO-COUNTERPART", findings, notes, kind, extractor, meta, None

    hay_sq, hay_ws = squash(body), wordstream(body)

    # --- split the source into content and documented furniture -------------
    all_lines = list(enumerate(src.split("\n"), 1))
    content, furniture = [], []
    for n, line in all_lines:
        why = furniture_class(line, kind)
        if why and why != "blank line":
            furniture.append((n, line, why))
        elif why != "blank line":
            content.append((n, line))
    content_text = "\n".join(l for _, l in content)

    for n, line, why in furniture:
        survived = squash(line) and squash(line) in hay_sq
        notes.append("%s — %s, source line %d: %s"
                     % ("still present in the cleaned file" if survived
                        else "removed, and it is furniture", why, n, q(line)))

    # --- atoms --------------------------------------------------------------
    buckets = {"MISSING": [], "FUSED": [], "RESPACED": []}
    judged = 0
    atoms, unjudgeable = find_atoms(content)
    for klass, verbatim, line_no in atoms:
        v = judge_atom(verbatim, hay_sq, hay_ws)
        if v is None:
            continue
        judged += 1
        if v != "INTACT":
            buckets[v].append((klass, verbatim, line_no))

    for klass, verbatim, line_no in buckets["MISSING"]:
        findings.append((
            "FAIL", "missing value",
            "the %s %s appears in the source and not in the cleaned file"
            % (klass, q(verbatim)), "source line %d" % line_no))
    for klass, verbatim, line_no in buckets["FUSED"]:
        findings.append((
            "FAIL", "fused token",
            "the %s %s survives only welded to its neighbour" % (klass, q(verbatim)),
            "source line %d — the characters are in the cleaned file, the "
            "separate token is not, so a word diff cannot see it" % line_no))
    for klass, verbatim, line_no in buckets["RESPACED"]:
        findings.append((
            "WARN", "respaced value",
            "the %s %s survives with its internal spacing changed"
            % (klass, q(verbatim)), "source line %d" % line_no))

    # --- segments -----------------------------------------------------------
    segs = segments(content)
    for seg, line_no in segs:
        if squash(seg) in hay_sq:
            continue
        chunks = chunk_split(seg, hay_sq)
        lost = [c for c, ok in chunks if not ok]
        if lost:
            findings.append((
                "FAIL", "missing text",
                "text at source line %d is not in the cleaned file: %s"
                % (line_no, q(seg, 240)),
                "found nowhere in the cleaned file: "
                + ", ".join(q(x, 70) for x in lost[:8])))
        elif len(chunks) > 2:
            findings.append((
                "WARN", "broken run",
                "source line %d survives only in %d separate pieces: %s"
                % (line_no, len(chunks), q(seg, 240)),
                "the pieces: " + " || ".join(q(c, 60) for c, _ in chunks[:6])))
        # exactly two chunks is a line break moving; not a loss

    # --- exact line audit, where extraction is byte-faithful ----------------
    if kind in EXACT:
        a = [fold(l).rstrip() for _, l in all_lines]
        b = [fold(l).rstrip() for l in body.split("\n")]
        raw_a = [l for _, l in all_lines]
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        already = {f[2] for f in findings}
        for op, i1, i2, _j1, _j2 in sm.get_opcodes():
            if op not in ("delete", "replace"):
                continue
            for k in range(i1, i2):
                line = raw_a[k]
                if not line.strip():
                    continue
                if furniture_class(line, kind):
                    continue
                if squash(line) and squash(line) in hay_sq:
                    continue   # moved, not lost — the containment checks own it
                msg = ("source line %d was removed and is not furniture under "
                       "the README strip policy: %s" % (k + 1, q(line, 240)))
                if msg in already:
                    continue
                findings.append((
                    "FAIL", "line removed", msg,
                    "exact line-level audit — extraction is byte-faithful for "
                    "plain text, so this is definitive"))

    if meta.get("bom") and body.startswith("﻿"):
        findings.append((
            "WARN", "stray byte-order mark",
            "the source's UTF-8 BOM was carried into the middle of the cleaned "
            "file, after the frontmatter",
            "U+FEFF now sits at the first character of the markdown body"))

    # --- the two ends -------------------------------------------------------
    tail_block, tail_lost = edge_check(content, hay_sq, head=False)
    head_block, head_lost = edge_check(content, hay_sq, head=True)
    if tail_lost:
        findings.append((
            "FAIL", "truncated by cleaning",
            "the end of the source is not in the cleaned file",
            "the source ends %s — nowhere in the cleaned file: %s"
            % (q(tail_block, 170), ", ".join(q(x, 70) for x in tail_lost[:8]))))
    if head_lost:
        findings.append((
            "FAIL", "head missing",
            "the beginning of the source is not in the cleaned file",
            "the source begins %s — nowhere in the cleaned file: %s"
            % (q(head_block, 170), ", ".join(q(x, 70) for x in head_lost[:8]))))

    upstream = looks_truncated(content_text)
    if upstream:
        reproduced = not tail_lost
        findings.append((
            "UPSTREAM", "source truncated",
            "the SOURCE itself stops mid-sentence — an upstream defect, not a "
            "cleaning defect",
            "its own last words: %s — the cleaned file %s. Nothing in this "
            "repo can repair this; it needs re-retrieving at the origin."
            % (q(upstream), "reproduces that ending faithfully" if reproduced
               else "does not even reach that ending")))

    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    ups = [f for f in findings if f[0] == "UPSTREAM"]
    if fails:
        verdict = "FAIL"
    elif warns:
        verdict = "PASS WITH WARNINGS"
    else:
        verdict = "PASS"
    if ups:
        verdict += " + UPSTREAM DEFECT"

    meta = dict(meta)
    meta.update({"atoms judged": judged,
                 "atoms set aside (fused by the checker's own extractor)": unjudgeable,
                 "segments checked": len(segs),
                 "furniture lines found by the checker": len(furniture),
                 "end of source survives": "no" if tail_lost else "yes",
                 "start of source survives": "no" if head_lost else "yes"})
    return verdict, findings, notes, kind, extractor, meta, None


# -------------------------------------------------------------------- report

def render(rel, clean_path, verdict, findings, notes, kind, extractor, meta):
    fails = [f for f in findings if f[0] == "FAIL"]
    warns = [f for f in findings if f[0] == "WARN"]
    ups = [f for f in findings if f[0] == "UPSTREAM"]
    L = ["---",
         "checker: tools/check.py",
         "checked: %s" % TODAY,
         "source: %s" % (SRC + "/" + rel),
         "cleaned: %s" % (clean_path or "NONE"),
         "source_kind: %s" % kind,
         "extractor: %s" % extractor,
         "independent_of: tools/clean.py — different extractor, different "
         "comparison method, no shared code",
         "verdict: %s" % verdict,
         "fails: %d" % len(fails),
         "warnings: %d" % len(warns),
         "upstream_defects: %d" % len(ups),
         "---", "",
         "# Check — %s" % rel, "",
         "## Verdict: %s" % verdict, ""]
    if not findings:
        L += ["Every named detail an independent extractor found in the source "
              "was found again in the cleaned file. No detail is missing.", ""]
    L += ["| | |", "|---|---|"]
    for k, v in meta.items():
        L.append("| %s | %s |" % (k, v))
    L.append("")

    def block(title, rows, blurb):
        if not rows:
            return
        L.append("## %s — %d" % (title, len(rows)))
        L.extend(["", blurb, ""])
        for _sev, klass, name, detail in rows[:MAX_LIST]:
            L.append("### %s — %s" % (klass.upper(), name))
            if detail:
                L.extend(["", detail])
            L.append("")
        if len(rows) > MAX_LIST:
            L.extend(["_… and %d more of the same kind. All of them are in "
                      "`03-check/FINDINGS.jsonl`._" % (len(rows) - MAX_LIST), ""])

    block("Fails", fails,
          "Each names a detail that is in the source and is not in the cleaned "
          "file, or is there in a form a reader cannot get back out.")
    block("Warnings", warns,
          "The detail survived; something about its shape did not.")
    block("Upstream defects", ups,
          "Already wrong in the source before this repo touched it. Reported, "
          "not repaired — hard rule 1.")

    if notes:
        L.append("## Furniture, audited independently — %d line(s)" % len(notes))
        L += ["",
              "Every line the *checker* judges furniture under the strip policy "
              "in `README.md` → \"The one job\", and what actually became of it. "
              "This is not the cleaner's own report of what it removed.", ""]
        for n in notes[:MAX_LIST]:
            L.append("- %s" % n)
        if len(notes) > MAX_LIST:
            L.append("- _… and %d more._" % (len(notes) - MAX_LIST))
        L.append("")
    return "\n".join(L) + "\n"


def main():
    dry = "--dry-run" in sys.argv
    sources, by_source, orphans = build_pairs()
    rows, jsonl = [], []

    for rel in sources:
        pair = by_source.get(rel)
        clean_path, body = (pair[0], pair[2]) if pair else (None, "")
        verdict, findings, notes, kind, extractor, meta, _ = check_one(
            rel, clean_path, body)
        report = render(rel, clean_path, verdict, findings, notes, kind,
                        extractor, meta)
        if clean_path:
            dest = os.path.join(OUT, os.path.splitext(
                os.path.relpath(clean_path, CLEAN))[0] + ".check.md")
        else:
            dest = os.path.join(OUT, rel + ".check.md")
        if not dry:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            io.open(dest, "w", encoding="utf-8").write(report)
        nf = sum(1 for f in findings if f[0] == "FAIL")
        nw = sum(1 for f in findings if f[0] == "WARN")
        nu = sum(1 for f in findings if f[0] == "UPSTREAM")
        rows.append((rel, verdict, nf, nw, nu, dest, kind))
        for sev, klass, name, detail in findings:
            jsonl.append({"source": rel, "clean": clean_path, "kind": kind,
                          "severity": sev, "class": klass,
                          "finding": name, "detail": detail})

    if not dry:
        os.makedirs(OUT, exist_ok=True)
        with io.open(os.path.join(OUT, "FINDINGS.jsonl"), "w", encoding="utf-8") as f:
            for r in jsonl:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    w = max(len(r[0]) for r in rows)
    for rel, verdict, nf, nw, nu, _d, _k in rows:
        print("%-*s  %-34s F%-4d W%-4d U%d" % (w, rel, verdict, nf, nw, nu))
    print()
    for cp, why in orphans:
        print("ORPHAN in %s: %s — %s" % (CLEAN, cp, why))
    print("sources: %d   paired with a cleaned file: %d   orphan cleaned files: %d"
          % (len(rows), sum(1 for r in rows if by_source.get(r[0])), len(orphans)))
    print("FAIL %d   PASS WITH WARNINGS %d   PASS %d   NO-COUNTERPART %d"
          % (sum(1 for r in rows if r[1].startswith("FAIL")),
             sum(1 for r in rows if r[1].startswith("PASS WITH")),
             sum(1 for r in rows if r[1].startswith("PASS") and "WITH" not in r[1]),
             sum(1 for r in rows if r[1].startswith("NO-COUNTERPART"))))
    print("findings: %d fails, %d warnings, %d upstream defects"
          % (sum(r[2] for r in rows), sum(r[3] for r in rows), sum(r[4] for r in rows)))
    return rows, jsonl, orphans


if __name__ == "__main__":
    main()
