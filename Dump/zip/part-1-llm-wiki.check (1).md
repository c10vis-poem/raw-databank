---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/Llm wiki/## Part 1꞉ Llm Wiki.txt
cleaned: 02-clean/Llm wiki/part-1-llm-wiki.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — Llm wiki/## Part 1꞉ Llm Wiki.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 18635 |
| atoms judged | 72 |
| atoms set aside (fused by the checker's own extractor) | 71 |
| segments checked | 130 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

