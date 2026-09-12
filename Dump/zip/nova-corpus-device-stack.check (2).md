---
checker: tools/check.py
checked: 2026-08-27
source: 01-sources/Nova Corpus — Device Stack.html
cleaned: 02-clean/nova-corpus-device-stack.md
source_kind: html
extractor: stdlib html.parser, tag boundaries preserved (decoded utf-8-sig)
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: FAIL
fails: 7
warnings: 0
upstream_defects: 0
---

# Check — Nova Corpus — Device Stack.html

## Verdict: FAIL

| | |
|---|---|
| encoding | utf-8-sig |
| bom | False |
| atoms judged | 148 |
| atoms set aside (fused by the checker's own extractor) | 33 |
| segments checked | 74 |
| furniture lines found by the checker | 1 |
| end of source survives | yes |
| start of source survives | yes |

## Fails — 7

Each names a detail that is in the source and is not in the cleaned file, or is there in a form a reader cannot get back out.

### FUSED TOKEN — the acronym `CHIP` survives only welded to its neighbour

source line 176 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the measurement `32 GB` survives only welded to its neighbour

source line 494 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the acronym `CLIENTS` survives only welded to its neighbour

source line 502 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the path `c10vis-poem/Horizons-UI` survives only welded to its neighbour

source line 514 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the path `c10vis-poem/novus-agenti` survives only welded to its neighbour

source line 517 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the path `c10vis-poem/aesop` survives only welded to its neighbour

source line 520 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

### FUSED TOKEN — the path `c10vis-poem/nova-skills` survives only welded to its neighbour

source line 523 — the characters are in the cleaned file, the separate token is not, so a word diff cannot see it

## Furniture, audited independently — 1 line(s)

Every line the *checker* judges furniture under the strip policy in `README.md` → "The one job", and what actually became of it. This is not the cleaner's own report of what it removed.

- still present in the cleaned file — browser/app chrome, source line 469: `TOOLS`

