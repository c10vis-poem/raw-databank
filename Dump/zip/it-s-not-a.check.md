---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/CCConvo/It's not a.txt
cleaned: 02-clean/CCConvo/it-s-not-a.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — CCConvo/It's not a.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1400 |
| atoms judged | 8 |
| atoms set aside (fused by the checker's own extractor) | 2 |
| segments checked | 9 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

