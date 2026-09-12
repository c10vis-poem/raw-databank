---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/ORIGINAL-DIRECTIONS-2026-08-18.md
cleaned: 02-clean/original-directions-2026-08-18.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS + UPSTREAM DEFECT
fails: 0
warnings: 0
upstream_defects: 1
---

# Check — ORIGINAL-DIRECTIONS-2026-08-18.md

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 24169 |
| atoms judged | 69 |
| atoms set aside (fused by the checker's own extractor) | 52 |
| segments checked | 183 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `Can't move screen equals can't sign in` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

