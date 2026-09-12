---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/CCConvo/The first.txt
cleaned: 02-clean/CCConvo/the-first.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — CCConvo/The first.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 3803 |
| atoms judged | 10 |
| atoms set aside (fused by the checker's own extractor) | 9 |
| segments checked | 24 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

