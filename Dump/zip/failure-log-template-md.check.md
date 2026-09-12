---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/TRAINING/failure_log_template.md.pdf
cleaned: 02-clean/universal-memory/TRAINING/failure-log-template-md.md
source_kind: pdf
extractor: pypdf 6.16.2 PdfReader.extract_text()
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/TRAINING/failure_log_template.md.pdf

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| pages | 2 |
| atoms judged | 7 |
| atoms set aside (fused by the checker's own extractor) | 2 |
| segments checked | 0 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

