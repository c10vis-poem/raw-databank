---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/whyyoucodevoicelikeass/whyyoubreaknofix.pdf
cleaned: 02-clean/whyyoucodevoicelikeass/whyyoubreaknofix.md
source_kind: pdf
extractor: pypdf 6.16.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS + UPSTREAM DEFECT
fails: 0
warnings: 0
upstream_defects: 1
---

# Check — whyyoucodevoicelikeass/whyyoubreaknofix.pdf

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| pages | 14 |
| atoms judged | 46 |
| atoms set aside (fused by the checker's own extractor) | 132 |
| segments checked | 424 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Bash  ` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

