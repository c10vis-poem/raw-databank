---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/AESOP_XI_/Red agent needs RLVRl.docx
cleaned: 02-clean/AESOP_XI_/red-agent-needs-rlvrl.md
source_kind: docx
extractor: stdlib zipfile + xml.etree over word/document.xml
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — AESOP_XI_/Red agent needs RLVRl.docx

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| docx_parts | 1 |
| rel_urls | 0 |
| atoms judged | 16 |
| atoms set aside (fused by the checker's own extractor) | 22 |
| segments checked | 32 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

