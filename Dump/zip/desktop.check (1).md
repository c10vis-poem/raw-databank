---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/Llm wiki/desktop.txt
cleaned: 02-clean/Llm wiki/desktop.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — Llm wiki/desktop.txt

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 1524 |
| atoms judged | 7 |
| atoms set aside (fused by the checker's own extractor) | 5 |
| segments checked | 15 |
| furniture lines found by the checker | 1 |
| end of source survives | yes |
| start of source survives | yes |

## Furniture, audited independently — 1 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 15: `Use code with caution.`

