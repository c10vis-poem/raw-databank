---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/Llm wiki/wiki desktop.txt
cleaned: 02-clean/Llm wiki/wiki-desktop.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — Llm wiki/wiki desktop.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1978 |
| atoms judged | 8 |
| atoms set aside (fused by the checker's own extractor) | 3 |
| segments checked | 22 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

