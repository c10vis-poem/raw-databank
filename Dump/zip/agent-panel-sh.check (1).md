---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/universal-memory/agent_panel.sh.docx
cleaned: 02-clean/universal-memory/agent-panel-sh.md
source_kind: docx
extractor: stdlib zipfile + xml.etree over word/document.xml
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS
fails: 0
warnings: 0
upstream_defects: 0
---

# Check — universal-memory/agent_panel.sh.docx

## Verdict: PASS

Every named detail an independent extractor found in the source was found again in the cleaned file. No detail is missing.

| | |
|---|---|
| docx_parts | 1 |
| rel_urls | 0 |
| atoms judged | 18 |
| atoms set aside (fused by the checker's own extractor) | 30 |
| segments checked | 47 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | yes |

