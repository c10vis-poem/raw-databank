---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/Three-APK Architecture (v1).pdf
cleaned: 02-clean/three-apk-architecture-v1.md
source_kind: pdf
extractor: pypdf 6.16.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS + UPSTREAM DEFECT
fails: 0
warnings: 0
upstream_defects: 1
---

# Check — Three-APK Architecture (v1).pdf

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| pages | 3 |
| atoms judged | 29 |
| atoms set aside (fused by the checker's own extractor) | 9 |
| segments checked | 41 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `captured from session · reference material, not a build-out session on its own` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

