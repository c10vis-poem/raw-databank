# Foundation Sources

**The pre-planning database.**

A new repo. Nothing inherited, nothing forked, nothing migrated.

It holds the source documents this project is actually built on, translated
verbatim into structured Markdown. That's all it does. It doesn't plan, decide,
combine, or interpret anything.

## What it's for

The grilling session. `grill-with-docs` reads what's in here, the operator
answers, and out of that comes the plan — the foundation outline and the whole
repo structure that follows. The real data compilation starts after that, not
before.

```
[1] this repo        the named sources, cleaned up verbatim
                     ↓
[2] grill session    this data + the operator's answers
                     → the plan, the foundation outline, the structure
                     ↓
[3] graph the vault
                     ↓
[4] compilation      the actual combining and condensing
```

Everything downstream is shaped by what lands here, so what lands here has to be
complete and unaltered. `grill-with-docs` is marked
`disable-model-invocation: true` — only the operator can start it.

## Hard rules

1. Ask The Builder. No actions without permissions or directions 
2.  Agent written rules are usually created by the agent itself out of thin air at the time of writing and rarely reflect the views and opinions of The Builder 

## One home

Everything lives in the Obsidian vault, and the vault is the repo. Same tree —
edited in Obsidian, tracked by git, pushed to main.

**This repo is the vault.** Operator-stated 2026-08-26: NovÆxorpus is a
**replacement, not a sibling**. It is the universal memory layer and Data Bank,
and the home of the living `wiki.md` (the llm-wiki).

Three legacy Obsidian vaults still exist alongside it on the device:

```
/storage/emulated/0/OBSIDIAN_VAULT/        ← a container, not a vault
├── .OBSIDIAN/           has .obsidian/  → legacy vault
├── OBSIDIAN-WIKI.md/    has .obsidian/  → legacy vault
├── OBSIDIAN_VAULT.md/   has .obsidian/  → legacy vault
└── novae-xorpus/        has .git/       → THIS REPO — the vault
```

None of the three has ever synced, which is why three handoffs written in August
never reached GitHub. They are resolved by steps 1–2 of the grill mandate below:
evaluate for useful files *and file-tree structure*, then purge. Obsidian hooks
and git hooks on this repo are still to be wired.

## What the files are for

| | |
|---|---|
| **`CLAUDE.md`** | The router. Tools, tool calling, skill loading, and the contexts that go with them. **Not the wiki.** No daily updates. |
| **Handoff** | The constantly changing session data. Rewritten and pushed **every session**. |
| **Wiki** | Running knowledge. Built later, from the cleaned sources. |
| **`01-sources/`** | Untouched originals. Never edited. |

## The one job

Take an original, strip the furniture, keep every word, write structured
Markdown.

**Strip** — page headers, footers, page numbers, browser and app chrome
(`Ask anything`, `Use code with caution`, `AI Mode`, nav bars, source panels),
watermarks, logo blocks, export metadata, per-page boilerplate.

**Keep** — every sentence of content, code as fenced code, tables as tables,
lists and headings and emphasis, diagram labels, captions, footnotes, and any
date the document states about itself.

Unsure whether something is content or furniture? Keep it.

### Chat exports: keep the turns separate

Most of these are chat exports. The operator's typed turns are the primary
content, by a wide margin. Model turns are secondary and routinely mix useful
iteration with conflation and error.

The cleanup doesn't judge which is which. It keeps both and makes the boundary
unmistakable: every turn marked with who said it, order preserved exactly, never
merged, never interleaved. A bare `.` or `stop` is a turn and stays.

## Output

One `.md` per source, mirroring the source tree.

Long documents also get an inline `.jsonl`, one record per section, so a tool
can query without loading the whole file. Short ones don't need it.

```yaml
---
source: 01-sources/pdf/novaegenti-defined-pt1.pdf
origin: drive://<file_id>
doc_date: 2026-08-13          # the document's own date, from inside it
file_modified: 2026-08-14
cleaned: 2026-08-24
---
```

The dates are there because the grill session decides stale versus garbage
versus keeper and can't without them. Later is a reasonable tiebreak between two
documents on the same subject — a prior, not a ranking. Contradictions between
sources are left exactly as they are.

## The check — RLVR

The operator orchestrates it. A different tool reads the original and the
cleaned version and reports which details are missing. Not the tool that did the
cleaning.

That's the reward signal, and it's why it works as RLVR: "is this detail present
in both" is mechanically verifiable, so the score is real rather than an
opinion. A missing detail is a fail with a name attached, not a percentage.

The corollary is the rule that governs everything downstream: **anything whose
output isn't mechanically checkable can't be an artifact — only a review
candidate.**

## Sources

Dictated 2026-08-18, 11:56–12:50. Verbatim record in
`ORIGINAL-DIRECTIONS-2026-08-18.md`, which is copied in here as a source itself.

Nearly all of it lives in one Drive tree, `___Lex-Novi-Æxentis-Copiæ`.

| # | Time | Named | Files | Where |
|---|---|---|---|---|
| 1 | 11:56 | `NovÆgenti Defined (pt.1).pdf` | 1 | on device (Claude artifact, not in Drive) |
| 2 | 11:56 | `Three-APK Architecture` v1 + v2 | 2 | Drive `ReadMe*` · v2 on device |
| 3 | 12:00 | `Continualharness.md` | 1 of 5 | Drive — **five candidates, pick one** |
| 4 | 12:04 | `Not wrongtxt` | 1 | Drive · on device |
| 5 | 12:08 | `NovÆcopia Vincet` (Doc + docx) | 2 | Drive `(NÆc)Æxi` · docx on device |
| 6 | 12:08 | `NovA-Corpus Diagnostic` | 1 | Drive `(NÆc)Æxi` |
| 7 | 12:10 | "all four of these PDFs" | ? | **ambiguous — confirm which four** |
| 8 | 12:12 | `CCConvo` folder | **29** | Drive `(NÆc)Æxi` — never pulled |
| 9 | 12:15 | `Nova Corpus — Device Stack` | 1 | Drive |
| 10 | 12:17 | `## Part 1- Lex (1).txt` | 1 (+2 dups) | Drive root · Docs in `ReadMe*` |
| 11 | 12:19 | the Drive link = folder **`Llm wiki`** | **12** | Drive `ReadMe*` — never pulled |
| 12 | 12:21 | `TERMUX_❔'s` folder | 4 | Drive — never pulled |
| 13 | 12:22 | `Coding ❔'s` — two docs | 2 | Drive — never pulled |
| 14 | 12:24 | `•⛔-whyyoucodevoicelikeass-` | ? | **not found by that name** |
| 15 | 12:26 | `Recursive Training Through Verification` | 1 of 2 | Drive — **two copies, pick one** |
| 16 | 12:27 | `Universal_Memory_` + `AESOP_XI_` non-dups | 11 + 8 | Drive — plus 11 subfolders to recurse |
| 17 | 12:31 | `Building inside of Google` + `App_Builders_Guide_` | 4 | Drive — vault copy is **0 bytes**, re-pull |
| 18 | 12:50 | `--🗂️~SKILLS.md_🛠️_` | 3 | Drive — plus 5 subfolders |

**~95 files located and reachable.** 6 already on device. 1 corrupt at 0 bytes.
1 folder unfindable by the name given. 3 items with two candidates each.

Exact names, byte sizes, and Drive file IDs for every one:
[`SOURCE-RETRIEVAL-MAP.md`](SOURCE-RETRIEVAL-MAP.md).

**Also a source:** the 2026-08-24 session that produced this README. It settled
the compilation-versus-compression distinction, what the daemons and Horizons
actually are, the CLAUDE.md / handoff split, and the RLVR check. At least as
current as the 08-18 material.

The old `manifests/sources.jsonl` is not this list — a 124-entry Drive crawl
where only 34 entries trace to anything asked for. Ignore it.

## What the grill session has to produce

Operator-stated, 2026-08-26. This is the mandate for the `grill-with-docs`
session. The agent running that session takes the data in this repo and produces
all of the following.

**NovÆxorpus is a replacement, not a sibling.** This repo *is* the vault — the
universal memory layer and Data Bank, and the home of the living `wiki.md`
(the llm-wiki). The other Obsidian vaults on the device are legacy and are
resolved by steps 1–2 below.

### 1. Evaluate the remaining Drive files

Grep every remaining file in Drive and determine what data is actually useful in
the universal memory layer and database.

### 2. Purge the legacy vaults and repos

Evaluate the still-remaining vaults and repos for any useful files *or file-tree
structure* worth keeping, then purge the rest.

### 3. Run the chosen files through the corpus process

Everything selected in 1–2 undergoes the same process as the existing corpus
documents. The result is the initial structure of the memory layer / Data Bank —
a starting point that continues to grow, expand, condense, and fork over time.

### 4. Determine the repo count

Decide how many repositories are needed in the immediate future, and extrude
whatever information the "grand repository" holds that can be used inside them.

### 5. Define the file format and file tree for each repo

Produce an outline for each repo's README and setup docs, so the agent building
that project starts with the building blocks it needs.

**Projects lined up, and repos that may need building:**

- **NovÆxorpus** — this repo.
- **Horizons-Ui**, plus the two adjacent access daemons (**Æsc**, **Æyre**).
  All three APKs run independently of each other, so three separate repos is
  probably the more efficient structure.
- **Four permanent agents**, fixtures in the architecture:
  1. **Search / recommendations / web-scraping** — tools, skills, and repo
     applicator. Runs a routine that scrapes for the latest updates,
     breakthroughs, currently trending repos, and industry news applicable to
     any project in the corpus. Cross-references and reviews what it finds so it
     can advise on alternative implementations or methods any project could use.
  2. **Help desk / operator's manual and install guide** — every app built gets
     running instructions, like any user manual. Upload a manual into this agent
     and it grabs data live, answers questions by voice, and acts as a live help
     desk. Works with any operator manual, system, or repo: whatever files are
     uploaded become its enterprise data bank for questions, how-tos, and
     troubleshooting on any installed project.
  3. **Housekeeping / script keeper / data extractor** — chat logs, tool-calling
     history, all of it. Goes through at end of day, collects the history, and
     writes it into structured Markdown and JSONL. Audits against the corpus and
     uses open web search tools for RLVR audits. Being local and the main hub, it
     also assists across the full three-device work setup: pulling tools,
     grepping data, and acting as active-workflow cross-agent auditor.
  4. **Red agent auditor** — previously defined.

  The last two agents will use one or two apps custom-built on the Google Cloud
  agent platform, using the enterprise app-building credits.

### 6. NovÆxenti

The actual agent logic, models, tools, and skills making up the dual-agent
query/executor model that acts as the main on-device assistant, using
Horizons-Ui and the accessibility daemons.

### 7. NovÆxopia

The claw aspect of the agent: tools, webhooks, on-device accessibility engines,
the runtime, PC/MCP servers, and IDE access. **Open question:** whether this can
be compiled together with NovÆxenti or has to stand alone.

### 8. Æsop-Xi

The orchestration layer — memory extraction protocols, agent parameters, and the
ethical agent logic compilation. The rules, guidelines, and infrastructure that
guide agents, manage how they operate, and monitor use of the Data Bank. Works
in conjunction with openwiki for file management, and implements the KAG and
RLVR audits and script training for assigned agents.

### Tools, not just skills

Operator-stated 2026-08-26. This corrects a bias in how items 1–3 were written.

Extracting **skills** from the source documents is only half the job, and
probably the smaller half. Most of these documents explain **parameters,
guidelines, and pathways** — not actions, functions, or specific executions.
A document describing how QAIRT routes a model to the Hexagon NPU is not a
skill; it is the spec for a *tool*.

Expect **at least as many tools extracted as skills, likely more.** A plan
that only produces a skill library has read these documents wrong.

### The shape of the output

Operator-stated 2026-08-26. Items 1–8 say what the grill session must decide.
This says what the deliverable must *look like*.

The format template is
[`01-sources/architecture-edits/EDIT-Clarifying Clean Text…`](01-sources/architecture-edits/) —
an earlier architecture document the operator annotated by hand. **Its layout
is the target.** Numbered file-by-file blocks, each with an explicit
destination path, a stated operational mandate, ASCII topology diagrams for
dataflow, and inline JSON schemas where a contract is being defined. It was
written to be readable by a human at a glance and still precise enough for an
agent to execute against.

Two warnings about that document:

1. **The content is out of date.** It predates the three-APK architecture and
   most of the tool inventory. The operator's own annotation: *"this is
   written way before the 3 APK architecture and additional tools are added
   so this is way out of date but still correct thinking process."* Copy the
   structure, not the claims.
2. **It is full of blanks.** Sections marked well-written are also marked
   *"missing numerous key aspects."* Treat it as a skeleton to fill, not a
   draft to edit.

The operator's annotations on that document are a standing punch list:

| Where | What has to change |
|---|---|
| Priority 4 vs 5 | **Swapped.** They run **parallel** — the three-APK architecture and on-device agents come forward, alongside runtime validation. |
| Priority 1 | Unsloth is optional. Higher priority: Google's app builders and the agent platform (formerly Vertex AI), plus the full tool/harness inventory below. |
| Priority 3 | This is the **first main goal of the grill session** — repo structure, folders, file structure, content, *and* roadmapping the agent build across every harness and tool: what gets used, how, when, where, why, and by whom. |
| Priority 6 | Not just Horizons + red auditor. Also on-device inference (query/executor), home-node housekeeping / cross-agent auditor / log compiler / script editor agent, help desk agent, web search agent, openwiki file management, and the on-device NPU/inference manager. |
| Repo list, items 4–6 | `horizons-ui-v1.2`, `nova-claw-runtime`, `aesop-xi-protocol` — all three need a massive overhaul. |
| Repo list, item 3 | `termux-building-skills` scope expands far beyond Termux, to **all device agent setups**. |
| Repo list, item 8 | The headless-node repos matter less than **the four agents** (red auditor plus three others) and **one to two separate apps**. |
| Skill-building protocol (File 5) | Operator: *"this is exactly what I want to happen… benefits would be profound."* The JSON schema approach is right; the code needs replacing. |
| File verifier (File 6) | Good foundation, needs filling in. Same format should extend to the **multi-agent cross-auditing setup for the home node**. |
| Audit schema (File 7) | Must expand to cover the Google-platform agents and the **four to six on-device agents**. |
| Final build block | The directory tree is **not** run by hand in Termux. The grill agent executes it — that agent is the **traffic director** managing development of the architectural framework. |

### Tool and asset assignment

Operator-stated 2026-08-26. Assignment is **per-agent**, not global — the same
tool serves different agents differently, and much of this is explicitly
trial-and-error. What follows is the operator's current read, not a locked
decision.

**Critical first, ahead of everything else:**

- **ECC**
- **Honey for Devs**
- **Pocock Skills**

**The working inventory to route through the corpus process.** This is the
operator completing a thought that was cut off mid-sentence in the annotated
architecture document — the list of assets that must get the same
skill-and-tool extraction treatment as the technical docs:

**ECC** · **Honey for Devs** · **Pocock Skills** · **Prime Agent** ·
**code review graph** · **reverse skills** · **Obsidian skills** ·
**notebooklm-py** · **Graphify skills** · **OpenAI** · **GSD** · **mem0** ·
**OB1** · **Omni Route** · **Claude Video** · **Node.js** · **Crawl4AI** ·
**Perplexity web search substitution** — and more.

Not an exhaustive list and not a ranking. The point is that **these repos and
skill packages are themselves source material**, not just dependencies to
install. They get extracted for tools and skills the same way a Qualcomm SDK
manual does.

**Assignments the operator considers likely:**

| Consumer | Tools |
|---|---|
| The three-APK setup | **OpenAI + Node.js + Omni Route** — operator: *"pretty sure this is going to work well"* |
| On-device open-weight models | **Prime Agent**; possibly **Qwen CLI** if the Qwen models end up driving it (unconfirmed) |
| Claude-based agents | **ECC** |
| Data-scraping / web-search agent | **Perplexity web search substitution** + **Crawl4AI** (the open-source Firecrawl equivalent — confirmed by operator 2026-08-26) |
| Auditing and **KAG** | **Graphify** + **notebooklm-py** |
| Specific agents (TBD which) | **Claude Video**, **reverse skills** |
| Multi-agent swarms | Ringer, CrewAI, and the other swarm tools |
| Universal memory bank | A whole litany of tools and assets — mem0, OB1, Reasoning Bank, openwiki, and more, to be enumerated |

**How to treat this list:** some of it is already tried and true, much of it is
untested. The grill session's job is not to pick winners on paper — it is to
state, per agent, what gets used and what still needs a trial. An assignment
with no stated reason is a guess and must be labelled one.

### Wiring this repo still needs

Not blockers on the grill session, but required for the ecosystem to work:

- Obsidian hooks **and** git hooks on this vault/repo.
- **Claude-in-Obsidian** connection — operator needs to be walked through it.
- **Obsidian ↔ GitHub** connection, the UI, and the desktop applications.
- **graphify** wired to the operator's main account.
- **notebooklm-py** skill, so the Gemini notebooks attach and update into this
  repo along with everything else.

## Layout

```
01-sources/   originals, untouched
02-clean/     the .md (and .jsonl for long ones)
03-check/     what the checking tool reported, one file per source
handoffs/     session state, pushed every session
CLAUDE.md     the router
```

## Extraction note

`pymupdf` `get_text("dict")` works on this device. `pymupdf4llm` drops content —
13% of one sample, half of another — because it discards text overlapping
images. Anything torch-based needs a wheel Android doesn't have.

Two of the PDFs are Chrome print-to-PDF: heading levels, table cells and list
semantics were destroyed before the file was written. There's no structure in
them to recover, so don't invent one.

**And none of that is a reason to stop.** If a converter fails, use another one,
or write the twenty lines that do the job. If a sub-agent chokes on a tool, do
it directly. A blocked tool has already cost this project more than a day of
waiting — it is never a reason to stall.

## Status — 2026-08-27

| | |
|---|---|
| `01-sources/` | **94 sources** across 14 directories (+ 5 `MANIFEST*` bookkeeping files) |
| `02-clean/` | **93 files**, produced by `tools/clean.py` |
| `03-check/` | **94 reports + `SUMMARY.md` + `FINDINGS.jsonl`** — the RLVR pass has been run |

The 2026-08-26 counts here said 93 sources and 92 clean files. Both were one
low. Excluding the five `MANIFEST*` files, `01-sources/` holds **94**; one of
them (`technical-builder-style.skill.zip`) has no counterpart, so `02-clean/`
holds **93**. 93 + 1 = 94. Raw file count is 99.

### The check — result

`tools/check.py` re-extracted every source with a different reader and compared
by a different method (see "The check — RLVR" above and the header of the tool).
94 sources checked, one report each.

| verdict | files |
|---|---|
| PASS | 44 |
| PASS, source has an upstream defect | 22 |
| PASS with warnings | 22 |
| PASS with warnings, source has an upstream defect | 4 |
| **FAIL** | **1** |
| **no counterpart in `02-clean/`** | **1** |

**The two that are not passes, by name:**

- `Nova Corpus — Device Stack.html` — **7 fused tokens.** `CHIP`, `32 GB`,
  `CLIENTS`, and the four repo paths `c10vis-poem/Horizons-UI`,
  `c10vis-poem/novus-agenti`, `c10vis-poem/aesop`, `c10vis-poem/nova-skills`
  survive only welded to the label beside them (`RAM32 GB`, `CHIPSM8750`). The
  source separates them with element boundaries; `pandoc html->plain` did not.
  The frontmatter warning on that file was right, and it is now specific.
- `SKILLS.md/technical-builder-style.skill.zip` — **no file in `02-clean/`.**
  It was recorded as "a zip has no text to extract". Opened independently, the
  archive holds text members. That content is not in the corpus.

**Nothing else lost a detail.** Across the other 92 sources: zero missing
values, zero missing text, zero content truncated by the cleaning, and zero
lines removed that the strip policy does not cover. The "14 files lose only
furniture" claim was re-derived from scratch and holds.

**26 sources are truncated in the source itself** — an upstream defect, not a
cleaning defect, reported and not repaired. That includes all three that were
already suspected: `part1-lex/## Part 1- Lex (1)`,
`universal-memory/TRAINING/Page - Purpose - Key evidence sources`, and
`whyyoucodevoicelikeass/local voice layer `. In two of them the truncation was
hidden behind a trailing `</content>` wrapper tag from the Drive export.

Warnings, which are shape and not content: 77 values respaced, 21 files
carrying the source's UTF-8 BOM into the middle of the markdown body.

Full roll-up in [`03-check/SUMMARY.md`](03-check/SUMMARY.md); every finding
machine-readable in `03-check/FINDINGS.jsonl`.
