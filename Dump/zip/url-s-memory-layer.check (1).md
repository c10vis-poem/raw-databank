---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/URL's-MEMORY LAYER .docx
cleaned: 02-clean/universal-memory/url-s-memory-layer.md
source_kind: docx
extractor: stdlib zipfile + xml.etree over word/document.xml + document.xml.rels hyperlink targets
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/URL's-MEMORY LAYER .docx

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| docx_parts | 1 |
| rel_urls | 14 |
| atoms judged | 125 |
| atoms set aside (fused by the checker's own extractor) | 238 |
| segments checked | 203 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

