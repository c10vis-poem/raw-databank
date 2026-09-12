---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/Starting Point-.pdf
cleaned: 02-clean/universal-memory/starting-point.md
source_kind: pdf
extractor: pypdf 6.16.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/Starting Point-.pdf

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| pages | 3 |
| atoms judged | 15 |
| atoms set aside (fused by the checker's own extractor) | 10 |
| segments checked | 4 |
| furniture lines found by the checker | 5 |
| end of source survives | yes |
| start of source survives | yes |

## Furniture, audited independently — 5 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- still present in the cleaned file — browser/app chrome, source line 145: `tools`
- still present in the cleaned file — browser/app chrome, source line 533: `more`
- still present in the cleaned file — browser/app chrome, source line 609: `more`
- still present in the cleaned file — browser/app chrome, source line 651: `tools.`
- still present in the cleaned file — browser/app chrome, source line 1035: `tools."`

