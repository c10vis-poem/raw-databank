---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/Mapping Runtimes and CLIs -!DOCTYPE.txt
cleaned: 02-clean/universal-memory/mapping-runtimes-and-clis-doctype.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/Mapping Runtimes and CLIs -!DOCTYPE.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 4061 |
| atoms judged | 56 |
| atoms set aside (fused by the checker's own extractor) | 10 |
| segments checked | 44 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

