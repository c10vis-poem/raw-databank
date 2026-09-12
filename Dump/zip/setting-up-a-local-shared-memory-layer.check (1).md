---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/Setting up a local shared memory layer.pdf
cleaned: 02-clean/universal-memory/setting-up-a-local-shared-memory-layer.md
source_kind: pdf
extractor: pypdf 6.16.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/Setting up a local shared memory layer.pdf

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| pages | 2 |
| atoms judged | 8 |
| atoms set aside (fused by the checker's own extractor) | 4 |
| segments checked | 0 |
| furniture lines found by the checker | 6 |
| end of source survives | yes |
| start of source survives | yes |

## Furniture, audited independently — 6 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- still present in the cleaned file — browser/app chrome, source line 301: `tools.`
- still present in the cleaned file — browser/app chrome, source line 311: `Tools`
- still present in the cleaned file — page number, source line 341: `1`
- still present in the cleaned file — page number, source line 347: `2`
- still present in the cleaned file — browser/app chrome, source line 855: `tools`
- still present in the cleaned file — browser/app chrome, source line 899: `tools`

