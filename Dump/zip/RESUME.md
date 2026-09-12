# Æsop-Xi — Session Resume / Handoff

Full rewrite, not an append — see `CLAUDE.md` for why. Owner: c10vis-poem
(nav@clovispoem.com). For anything not addressed this session, see
`~/novae-xorpus/unresolved.md` (the real, durable, cross-repo backlog — items
14-18 are new from this session).

## What this is

Unchanged from last session — see `CLAUDE.md` / `ARCHITECTURE.md` for project
shape. This session (2026-09-06) was device-cleanup + making the local (Termux)
bootstrap actually match the cloud one, plus installing the Happy Ending
session-close plugin.

## Repo state (2026-09-06)

1. **`scripts/bootstrap-stack.sh` now works on this phone, not just in the
   cloud.** `session-start.sh`'s `CLAUDE_CODE_REMOTE=true` gate was dropped
   (local sessions get the identical bootstrap now, per operator direction) —
   but it still only fires when a session's project root is this repo; running
   it manually (`bash scripts/bootstrap-stack.sh`) works from anywhere.
2. **The real bug behind every Android failure**: these packages target glibc
   Linux; Termux is Android/bionic. Fixed by routing through `proot-distro
   login debian` (already installed) where a glibc target is genuinely needed,
   and using Termux's own native builds where those already exist and are
   better. Full writeup in `CLAUDE.md`'s new "Termux/Android platform gap"
   section — read that before re-debugging any of this from scratch.
3. **Fixed and verified working this session**: `clean-my-ai-harness` skill
   install (two bugs: `/tmp` not writable + wrong assumed zip layout),
   `code-review-graph` (built + registered for 3 repos via proot-Debian; its
   MCP server config repointed at the working venv in both `~/.claude.json`
   and `NovA-terrestrial-brain/.mcp.json`), `notebooklm-py`/Playwright installs
   cleanly via proot-Debian, terrestrial-brain's local Postgres+pgvector+MCP
   server (native Termux Postgres 18, pgvector built from source, native
   `deno` — responds correctly on :8000).
4. **Still broken, not yet fixed** (see `unresolved.md` #14-15): OmniRoute's
   dev server (needs Node 22+ inside proot-Debian, undici incompatibility with
   proot's default Node 20); terrestrial-brain's Obsidian-plugin build
   (`tsc: not found`, not root-caused).
5. **Happy Ending plugin installed** (session-close/handoff skill,
   skills-for-ai.com, single-seat license) — registered by hand-editing Claude
   Code's own config JSON since the interactive `/plugin marketplace add` flow
   is broken client-side on this build. Customized to explicitly check for
   `RESUME.md` (full-replace) / `unresolved.md` (durable, add-only) /
   `CLAUDE.md` (normal patch) in whatever repo it runs in — not just aesop-xi.
   Repo cleaned up: original vendor download moved out of shared Android
   Downloads into `~/downloads/happy-ending-1.0.0-vendor-original/`;
   `.agents/skills/happy-ending/` is now a symlink to the maintained
   `plugins/happy-ending/skills/happy-ending/` (was a duplicate, had already
   drifted once — can't drift again now).
6. **Two full inventory artifacts published this session** (not code, but real
   reference material): "Shelfware Audit" (every skill/agent/tool/MCP
   connector on this device + real usage counts from `~/.claude.json`
   telemetry) and "Bootstrap Triage" (every asset in `bootstrap-stack.sh`,
   what broke, what fixed it) — both in this session's artifact history.

## Do not carry forward

- Don't re-attempt `postgresql-16-pgvector` via proot-Debian for terrestrial-
  brain — Debian 13/trixie only has PG17, and Termux's own native PG18 route
  is simpler and already working. Native Termux Postgres is the answer here,
  not proot.
- Don't assume `/plugin marketplace add` works interactively on this Claude
  Code build — it silently registers nothing. Direct config-file edits (or the
  plain non-interactive `claude plugin marketplace add` / `install` CLI
  subcommands, confirmed working when OmniRoute's setup ran them) are the
  reliable path.

## Next best step

Restart this Claude Code session once, to confirm: (a) the `happy-ending`
skill actually loads, (b) the `code-review-graph` MCP connector actually
connects on the fixed config. Then decide whether to tackle OmniRoute's Node
version or terrestrial-brain's `tsc` issue (unresolved.md #14-15), or move on.

## Next-session prompt

> Continuing aesop-xi device work. State: bootstrap-stack.sh now runs
> correctly on this Termux phone (Android/bionic → proot-Debian glibc was the
> general fix, see CLAUDE.md). Fixed and verified: clean-my-ai-harness,
> code-review-graph (+ MCP config), notebooklm-py, terrestrial-brain's local
> Postgres+pgvector+MCP server. Still broken: OmniRoute (needs Node 22+ in
> proot-Debian), terrestrial-brain's Obsidian-plugin build (tsc not found) —
> see unresolved.md #14-15. Happy Ending session-close plugin is installed and
> customized for RESUME.md/unresolved.md/CLAUDE.md handoff — hasn't been
> confirmed loading after a restart yet. Start here: restart the session and
> verify both of those before doing anything else.
