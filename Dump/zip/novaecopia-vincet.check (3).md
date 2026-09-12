---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/novaexopia-vincet/NovÆcopia Vincet.txt
cleaned: 02-clean/novaexopia-vincet/novaecopia-vincet.md
source_kind: text
extractor: byte read, decoded utf-8-sig (BOM stripped)
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS WITH WARNINGS
fails: 0
warnings: 1
upstream_defects: 0
---

# Check — novaexopia-vincet/NovÆcopia Vincet.txt

## Verdict: PASS WITH WARNINGS

| | |
|---|---|
| encoding | utf-8-sig |
| bom | True |
| bytes | 8747 |
| atoms judged | 20 |
| atoms set aside (fused by the checker's own extractor) | 20 |
| segments checked | 90 |
| furniture lines found by the checker | 2 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### STRAY BYTE-ORDER MARK — the source's UTF-8 BOM was carried into the middle of the cleaned file, after the frontmatter

U+FEFF now sits at the first character of the markdown body

## Furniture, audited independently — 2 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 16: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 140: `Use code with caution.`

