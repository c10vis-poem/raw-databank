---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/whyyoucodevoicelikeass/local voice layer .txt
cleaned: 02-clean/whyyoucodevoicelikeass/local-voice-layer.md
source_kind: text
extractor: byte read, decoded utf-8-sig
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: PASS + UPSTREAM DEFECT
fails: 0
warnings: 0
upstream_defects: 1
---

# Check — whyyoucodevoicelikeass/local voice layer .txt

## Verdict: PASS + UPSTREAM DEFECT

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| bytes | 3239 |
| atoms judged | 6 |
| atoms set aside (fused by the checker's own extractor) | 5 |
| segments checked | 38 |
| furniture lines found by the checker | 4 |
| end of source survives | yes |
| start of source survives | yes |

## Upstream defects — 1

Already wrong in the source before this repo touched it. Reported, not repaired — hard rule 1.

### SOURCE TRUNCATED — the SOURCE itself stops mid-sentence — an upstream defect, not a cleaning defect

its own last words: `What should happen: Your device will show a sy` — the cleaned file reproduces that ending faithfully. Nothing in this repo can repair this; it needs re-retrieving at the origin.

## Furniture, audited independently — 4 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- removed, and it is furniture — browser/app chrome, source line 15: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 20: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 49: `Use code with caution.`
- removed, and it is furniture — browser/app chrome, source line 62: `Use code with caution.`

