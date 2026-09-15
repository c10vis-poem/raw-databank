# NovÆxorpus — the router

Tool-agnostic. Any agent/session that attaches to this repo follows this file —
not just Claude Code. This is the real rules file; `CLAUDE.md` (and any other
tool-specific file, e.g. a future `GEMINI.md`) is just a thin pointer to this one.

**It is not the wiki.** No daily updates, no session notes, no running knowledge —
those live in `wiki/` and `handoffs/`.

## What this repo is

The pre-planning database — this project's #dumbass (Database & Universal Memory
Bank Across Split Services): the universal memory layer meant to persist across
every repo and every agent, not scoped to any one project. Source documents named
in the 2026-08-18 session, translated verbatim into structured Markdown for the
`grill-with-docs` session. Read `README.md` before doing anything.

## Naming

`NAMING-CANON.md` is authoritative. NovÆxorpus · NovÆxenti · NovÆxopia ·
Æsop-Xi · Horizons-Ui · Æsc · Æyre. Source documents keep their original
spellings — never rewrite a source to match the canon.

## Hard rules

1. Verbatim. Content survives, furniture goes.
2. Nothing merged. Same file count out as in.
3. Nothing interpreted.
4. Speaker attribution is content.
5. Nothing self-certifies.
6. Push every session. `main` stays current.
7. Never stall on a tool. If it fails, do the job another way.

## Layout

| | |
|---|---|
| `01-sources/` | untouched originals + sha256 manifest |
| `02-clean/` | verbatim cleanups |
| `03-check/` | what the checking tool reported |
| `wiki/` | running knowledge — built later, from `02-clean/` |
| `handoffs/` | session state, rewritten and pushed every session |
| `unresolved.md` | durable, cross-repo, cross-agent backlog (moved here 2026-08-31) |
| `MASTER-RESUME.md`, `MASTER-CLAUDE.md` | auto-generated overview of every attached project's RESUME.md/CLAUDE.md — see below, don't hand-edit |
| `projects/<name>/` | same-device mirror symlinks into other repos' RESUME.md/CLAUDE.md — see below |
| `tools/` | scripts this repo uses |
| `skills/` | skills scoped to this repo |

## The RESUME/unresolved/CLAUDE discipline, reflected here (2026-08-31)

Rather than this repo keeping its own separate handoff discipline, every attached
project's own `RESUME.md`/`CLAUDE.md` gets mirrored here instead:

- **Same device**: `projects/<name>/RESUME.md` and `CLAUDE.md` are real symlinks
  into the actual repo (e.g. `projects/aesop-xi/RESUME.md` -> `~/repos/aesop-xi/RESUME.md`).
  Not copies — the literal same file, so there is no drift to manage.
- **A different device or cloud environment** cannot be symlinked in from here —
  symlinks don't cross physical machines. To attach a new environment:
  1. `git clone` this repo (novae-xorpus) into it.
  2. `git clone` whatever project repo it's working on, if not already present.
  3. Create the same local symlink within that environment.
  4. Every session there: `git pull` both repos at start, `git push` both at end
     (this is just hard rule 6 applied to every attached repo, not only this one).
- `unresolved.md` lives here directly (not mirrored) since it was never repo-specific
  to begin with.

### The MASTER-*.md auto-regeneration hook

`~/repos/aesop-xi/.git/hooks/post-commit` calls
`novae-xorpus/tools/regenerate_masters.sh` after every commit in aesop-xi, which
reads every `projects/*/RESUME.md` and `projects/*/CLAUDE.md` (via the symlinks,
live working-tree content) and concatenates each into its own overview —
`MASTER-RESUME.md` and `MASTER-CLAUDE.md`. This means **both reflect state as of
the last commit, not the current working tree** — edit a project's file without
committing, and the master stays one commit behind until the next commit fires
the hook. Any other repo added under `projects/` should get the same hook
installed in its own
`.git/hooks/post-commit`.

## Tools and skills

**`tools/clean.py`** — the only tool here. Converts `01-sources/` to
`02-clean/` in one pass: pymupdf for PDFs, pandoc for docx and html, plain
read for text. Detects PDFs by magic bytes, so extensionless files work.
Strips a fixed furniture list and runs a word-frequency loss check against the
raw extraction. Re-run it whenever new sources land — it is idempotent and
rewrites the whole tree.

    python3 tools/clean.py

Its loss check does **not** satisfy hard rule 5. Same script, no vote.

No skills yet. Populated when the grill session defines what's needed — not
before, and not by copying in a library. A skill without a stated trigger does
not get installed.

## Retrieval — how Drive files actually come down

The Google Drive connector works and is the normal path. Large files are not a
problem: when an MCP result exceeds the inline cap the harness spools the whole
thing to a JSON file on disk and returns the path. Read that file, decode the
`content` field, write the bytes — the base64 never enters context. This works
for multi-megabyte binaries. **Never paste base64 through model output**; that
truncates silently and has already corrupted files once.

rclone was never needed. No remote is configured and none is required.
