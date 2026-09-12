---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/TRAINING/Page - Purpose - Key evidence sources (Google Doc export).txt
cleaned: 02-clean/universal-memory/TRAINING/page-purpose-key-evidence-sources-google-doc-export.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS + UPSTREAM DEFECT
fails: 0
warnings: 0
upstream_defects: 1
---

# Check — universal-memory/TRAINING/Page - Purpose - Key evidence sources (Google Doc export).txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1707 |
| atoms judged | 8 |
| atoms set aside (fused by the checker's own extractor) | 22 |
| segments checked | 30 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `/open-questions.md          — 4 act` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

