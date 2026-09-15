---
name: corpus-verify
description: >
  Independent RLVR corpus checker. Reads 01-sources/ and 02-clean/ with
  different extraction libraries than tools/clean.py used, compares by
  named-atom and segment containment, and writes results to 03-check/.
  Hard rule 5: the tool that cleaned a file does not get a vote on whether
  the cleaning was good.
tools:
  - Bash
  - Read
  - Glob
  - Grep
---

Follow the full skill definition at `skills/corpus-verify.skill.md`.

## Quick invocation

```bash
# Standard run — reads 01-sources/, compares 02-clean/, writes 03-check/
python3 tools/check.py

# Dry run — prints roll-up only, writes nothing
python3 tools/check.py --dry-run
```

Requires `pypdf` (`pip install pypdf`). All other dependencies are stdlib.

## When to fire

- After any run of `tools/clean.py` (first run or re-run)
- After adding new sources to `01-sources/`
- After modifying `tools/clean.py`
- Before any grill session or downstream compilation
- Any time a source is suspected of losing detail through cleaning

## After running

Read `03-check/SUMMARY.md` for the roll-up. Any verdict that is not PASS
requires action — see `skills/corpus-verify.skill.md` §"After running —
required actions" for what to do per verdict type.

Do not treat an ERROR verdict as a pass. Do not treat UPSTREAM DEFECT as
something to repair. Do not skip or disable any check to get a green result.
