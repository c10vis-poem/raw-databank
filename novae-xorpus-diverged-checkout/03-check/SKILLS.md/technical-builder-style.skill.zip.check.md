---
checker: tools/check.py
checked: 2026-09-09
source: 01-sources/SKILLS.md/technical-builder-style.skill.zip
cleaned: 02-clean/SKILLS.md/technical-builder-style.skill.zip.md
source_kind: zip
extractor: stdlib zipfile — archive opened and enumerated
independent_of: tools/clean.py — different extractor, different comparison method, no shared code
verdict: FAIL
fails: 6
warnings: 0
upstream_defects: 0
---

# Check — SKILLS.md/technical-builder-style.skill.zip

## Verdict: FAIL

| | |
|---|---|
| members | 1 |
| text_members | 1 |
| atoms judged | 3 |
| atoms set aside (fused by the checker's own extractor) | 2 |
| segments checked | 11 |
| furniture lines found by the checker | 0 |
| end of source survives | yes |
| start of source survives | no |

## Fails — 6

Each names a detail that is in the source and is not in the cleaned file, or is there in a form a reader cannot get back out.

### MISSING VALUE — the measurement `989 bytes` appears in the source and not in the cleaned file

source line 1

### MISSING VALUE — the path `technical-builder-style/SKILL.md` appears in the source and not in the cleaned file

source line 1

### MISSING VALUE — the number `989` appears in the source and not in the cleaned file

source line 1

### MISSING TEXT — text at source line 1 is not in the cleaned file: `technical-builder-style/SKILL.md	989 bytes`

found nowhere in the cleaned file: `technical-builder-style/SKILL.md`, `989`, `bytes`

### MISSING TEXT — text at source line 2 is not in the cleaned file: `=== technical-builder-style/SKILL.md ===`

found nowhere in the cleaned file: `technical-builder-style/SKILL.md`

### HEAD MISSING — the beginning of the source is not in the cleaned file

the source begins `technical-builder-style/SKILL.md	989 bytes\n=== technical-builder-style/SKILL.md ===` — nowhere in the cleaned file: `technical-builder-style/SKILL.md`, `989`, `bytes`, `technical-builder-style/SKILL.md`

