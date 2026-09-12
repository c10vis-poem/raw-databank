---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/novaexopia-vincet/Copy of NovAEcopia (Drive text extract).txt
cleaned: 02-clean/novaexopia-vincet/copy-of-novaecopia-drive-text-extract.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — novaexopia-vincet/Copy of NovAEcopia (Drive text extract).txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 5345 |
| atoms judged | 23 |
| atoms set aside (fused by the checker's own extractor) | 19 |
| segments checked | 51 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

