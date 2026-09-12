---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/NovÆcopia Vincet.docx
cleaned: 02-clean/novaecopia-vincet.md
source_kind: docx
extractor: stdlib zipfile + xml.etree over word/document.xml
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — NovÆcopia Vincet.docx

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| docx_parts | 1 |
| rel_urls | 0 |
| atoms judged | 20 |
| atoms set aside (fused by the checker's own extractor) | 20 |
| segments checked | 90 |
| furniture lines found by the checker | 2 |
| end of source survives | yes |
| start of source survives | yes |

## Furniture, audited independently — 2 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 14: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 121: `Use code with caution.`

