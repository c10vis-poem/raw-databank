---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/whyyoucodevoicelikeass/no shit Sherlock..txt
cleaned: 02-clean/whyyoucodevoicelikeass/no-shit-sherlock.md
source_kind: text
extractor: byte read, decoded utf-8-sig (BOM stripped)
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS WITH WARNINGS
fails: 0
warnings: 1
upstream_defects: 0
---

# Check — whyyoucodevoicelikeass/no shit Sherlock..txt

## Verdict: PASS WITH WARNINGS

| | |
|---|---|
| encoding | utf-8-sig |
| bom | True |
| bytes | 3437 |
| atoms judged | 16 |
| atoms set aside (fused by the checker's own extractor) | 9 |
| segments checked | 28 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### STRAY BYTE-ORDER MARK — the source's UTF-8 BOM was carried into the middle of the cleaned file, after the frontmatter

U+FEFF now sits at the first character of the markdown body

