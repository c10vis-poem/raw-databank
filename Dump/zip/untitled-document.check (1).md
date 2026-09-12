---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/whyyoucodevoicelikeass/Untitled document.txt
cleaned: 02-clean/whyyoucodevoicelikeass/untitled-document.md
source_kind: text
extractor: byte read, decoded utf-8-sig (BOM stripped)
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS WITH WARNINGS + UPSTREAM DEFECT
fails: 0
warnings: 1
upstream_defects: 1
---

# Check — whyyoucodevoicelikeass/Untitled document.txt

## Verdict: PASS WITH WARNINGS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | True |
| bytes | 679 |
| atoms judged | 4 |
| atoms set aside (fused by the checker's own extractor) | 0 |
| segments checked | 1 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### STRAY BYTE-ORDER MARK — the source's UTF-8 BOM was carried into the middle of the cleaned file, after the frontmatter

U+FEFF now sits at the first character of the markdown body

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `emma that multimodal and operate the piper or something I mean I think yourself outside the box dude` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

