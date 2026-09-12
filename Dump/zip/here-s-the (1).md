---
source: CCConvo/Here's the.txt
cleaned: 2026-08-26
converter: none - plain text
---
Here's the current structure, mapped fresh — new stuff on top, the standard taxonomy underneath, exactly as asked. It's spread across two nesting levels now (`__NovÆ-Corpus(NÆX)` → `___Lex-Novi-Æxentis-Copiæ`), not one flat folder.

**New — folders you added, not part of the original taxonomy**

At the `__NovÆ-Corpus(NÆX)` level: `--7•📱_REPO's_💻~`, `Base Skill Guideline`, `Canon(needs-c>c>c)`, `G`, `PRIMARY DESIGN CORPUS`, `aesop`, `clis-and-agents`, `•🌐-_Asset-Integrations_`, `•🖥️_TERMUX_[>_ ]`

One level deeper, inside `___Lex-Novi-Æxentis-Copiæ`: `-•🦁 NovusÆxenti🌳NovÆcopia🕸️•~`, `.claude`, `.migrate`, `Files_structur3`, `Hardware allocation map`, `Llm wiki`, `Local voice layer`, `Mobile Browser Conversation Extraction Bookmarklet`, `Planning&Reference.docs`, `System mapping and data flow graph`, `novaecopia`

**Standard — the original DataBank taxonomy, present but relocated**

At `__NovÆ-Corpus(NÆX)`: `ReadMe`, `BUILDERS_GUIDE`, `EMPIRICAL_DATA`, `TERMUX_main`, `PENDING_CORPORA`, `OBSIDIAN_VAULT`

Nested inside `___Lex-Novi-Æxentis-Copiæ`: `HORIZONS_UI`, `AESOP_XI`, plus lowercase-renamed ones — `file-management-system`, `github-ci-cd`, `global-documentation-vault`, `horizons-ui`, `pending-corpora`, `registries`, `reverse-engineering`, `skills`, `termux`

**Two things worth flagging, not just cataloguing:**

**`-•🗂️_DataBank_(main)📚•` is now completely empty.** Everything that used to be inside it has been pulled out and redistributed across the two levels above. That folder is just a shell now.

**This breaks the manifests I built earlier tonight.** Every `path` field in `xgrep_/index.jsonl`, `ccan_/index.jsonl`, and the rest was recorded against the old DataBank locations. Since those files have moved during your restructure, those paths no longer resolve — the manifests are a snapshot of where things *were*, not where they *are* now. They're still useful as records of what got classified and why, but not as live navigation. If you want them re-pointed at current locations, that's a real re-scan, not a quick fix.

**Not located anywhere in this pass:** `SKILLS.md`, `CLAUDE.md`, `AUGUST-'26`, `NOVUS-AGENTI`, `PENDING_ACTIONS` — the old numbered/emoji names for these. Possibly renamed into the new lowercase ones (`skills`, `pending-corpora` look like likely successors), possibly nested somewhere I haven't checked. Didn't want to guess rather than just tell you they're not where I expected.