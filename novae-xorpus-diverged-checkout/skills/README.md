# Skills

Skills scoped to this repo.

Nothing gets installed without a stated trigger — what has to be true for it to
fire. A skill library with no usage rule is pure cost: 894 skills were once
installed on this device and never used once.

- `corpus-verify/` — independent RLVR check for the `01-sources` -> `02-clean`
  pipeline. Added 2026-08-27.

Each entry here must also exist at `~/.claude/skills/<name>/` on this device
(and on any other device/session working in this repo) or it isn't actually
loadable — `<name>/SKILL.md`, not a flat `<name>.skill.md` file. This repo's
copy is canonical; the local copy is a synced working copy, same convention as
`aesop-xi/skills/`.
