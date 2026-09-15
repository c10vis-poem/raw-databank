---
checker: tools/check.py
checked: 2026-09-09
source: 01-sources/NovA-Corpus Diagnostic.pdf
cleaned: 02-clean/nova-corpus-diagnostic.md
source_kind: pdf
extractor: pypdf 6.14.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS WITH WARNINGS
fails: 0
warnings: 1
upstream_defects: 0
---

# Check — NovA-Corpus Diagnostic.pdf

## Verdict: PASS WITH WARNINGS

| | |
|---|---|
| pages | 9 |
| atoms judged | 81 |
| atoms set aside (fused by the checker's own extractor) | 43 |
| segments checked | 173 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

## Warnings — 1

The detail survived; something about its shape did not.

### RESPACED VALUE — the acronym `FINDINGS` survives with its internal spacing changed

source line 1

