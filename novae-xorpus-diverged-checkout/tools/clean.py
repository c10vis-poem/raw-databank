#!/usr/bin/env python3
"""01-sources -> 02-clean. Verbatim extraction + furniture strip + loss check."""
import os, re, sys, io, json, subprocess, hashlib, datetime
from collections import Counter

SRC, OUT = "01-sources", "02-clean"
TODAY = datetime.date.today().isoformat()

FURNITURE = {
    "Use code with caution.", "Ask anything", "AI Mode",
    "All Images Videos News Maps Shopping Books Flights Finance",
    "Try without personalization", "Sign in", "Search",
    "Try without personalization Search Labs", "Show more", "Show less",
}
FURNITURE_RE = re.compile(r"^\s*(Use code with caution\.?|AI Mode|Ask anything|Try without personalization|All Images Videos.*|\d+ sites?)\s*$")

def slug(p):
    s = os.path.splitext(os.path.basename(p))[0]
    s = s.replace("Æ","ae").replace("æ","ae").replace("Ç","c").replace("ç","c")
    s = re.sub(r"[^A-Za-z0-9]+","-",s).strip("-").lower()
    return re.sub(r"-+","-",s) or "untitled"

def extract(p):
    e = p.rsplit(".",1)[-1].lower() if "." in os.path.basename(p) else ""
    with open(p,"rb") as f: head = f.read(8)
    if head.startswith(b"%PDF"): e = "pdf"
    if e == "pdf":
        import fitz
        d = fitz.open(p)
        return "\n".join(pg.get_text() for pg in d), "pymupdf get_text()", d.page_count
    if e == "docx":
        r = subprocess.run(["pandoc","-f","docx","-t","markdown","--wrap=none",p],
                           capture_output=True,text=True)
        return r.stdout, "pandoc docx->markdown", None
    if e in ("html","htm"):
        raw = io.open(p,encoding="utf-8",errors="replace").read()
        raw = re.sub(r"(?is)<style\b.*?</style>|<script\b.*?</script>","",raw)
        r = subprocess.run(["pandoc","-f","html","-t","plain","--wrap=none"],
                           input=raw,capture_output=True,text=True)
        return r.stdout, "pandoc html->plain (style/script stripped)", None
    if e == "zip":
        return None, None, None
    return io.open(p,encoding="utf-8",errors="replace").read(), "none - plain text", None

def strip_furniture(t):
    kept, removed = [], 0
    for line in t.split("\n"):
        if FURNITURE_RE.match(line) or line.strip() in FURNITURE:
            removed += 1; continue
        kept.append(line)
    return "\n".join(kept), removed

WORD = re.compile(r"[A-Za-z0-9ÆæÇç_~·—→●'’/§£.\-]+")
def loss(a,b):
    m = Counter(WORD.findall(a)) - Counter(WORD.findall(b))
    return dict(m)

def main():
    rows=[]
    for root,_,files in os.walk(SRC):
        for fn in sorted(files):
            if fn.startswith("MANIFEST"): continue
            p = os.path.join(root,fn)
            rel = os.path.relpath(p,SRC)
            try: raw,conv,pages = extract(p)
            except Exception as ex:
                rows.append((rel,"EXTRACT-FAIL",str(ex)[:60],"")); continue
            if raw is None:
                rows.append((rel,"SKIP","binary/zip","")); continue
            body,removed = strip_furniture(raw)
            sub = os.path.dirname(rel)
            od = os.path.join(OUT,sub) if sub else OUT
            os.makedirs(od,exist_ok=True)
            dest = os.path.join(od, slug(fn)+".md")
            fm = ["---",
                  "source: %s" % rel.replace("\\","/"),
                  "cleaned: %s" % TODAY,
                  "converter: %s" % conv]
            if pages: fm.append("source_pages: %d" % pages)
            if removed: fm.append("furniture_lines_stripped: %d" % removed)
            fm += ["---",""]
            io.open(dest,"w",encoding="utf-8").write("\n".join(fm)+body)
            miss = loss(raw,body)
            FURN_WORDS = {"Use","code","with","caution.","AI","Mode","Ask","anything",
                          "Try","without","personalization","All","Images","Videos","News",
                          "Maps","Shopping","Books","Flights","Finance","sites","site"}
            expected = all(w in FURN_WORDS or w.isdigit() for w in miss)
            status = "OK" if not miss else ("furniture-only" if expected else "CHECK")
            rows.append((rel,status,"%d chars"%len(body), json.dumps(miss)[:70] if miss else ""))
    w=max(len(r[0]) for r in rows)
    for r in rows: print("%-*s  %-14s %-12s %s"%(w,r[0],r[1],r[2],r[3]))
    print("\ntotal: %d   OK: %d   furniture-only: %d   CHECK: %d   fail/skip: %d" % (
        len(rows), sum(1 for r in rows if r[1]=="OK"),
        sum(1 for r in rows if r[1]=="furniture-only"),
        sum(1 for r in rows if r[1]=="CHECK"),
        sum(1 for r in rows if r[1] in ("EXTRACT-FAIL","SKIP"))))

main()
