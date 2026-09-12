---
session: 2026-08-27
type: grill-session-prep
status: ready
---

# Grill Session Prep — 2026-08-27

This document is the full context brief for the grill session. It covers three reusable patterns to formalize, plus the complete architecture, project roster, and agent build plan the grill session must produce decisions about.

---

## 1. Corpus-Verify Skill

An independent document corpus verification tool. Given a source folder and a clean folder, it reads both using *different* extraction libraries than whatever cleaned the files, and checks whether content survived cleaning. Hard rule 5 in action: the tool that cleaned a file does not get a vote on whether the cleaning was good.

### Core algorithm

**squash(s)** — fold Unicode to ASCII, lowercase, strip all non-alphanumeric. Makes `CHIP SM8750` and `CHIPSM8750` identical for containment checks.

**wordstream(s)** — same fold but collapse separators to spaces. Preserves boundaries so you can tell whether a value survived as a separate word or got fused.

**find_atoms()** — extract named values from the source: URLs, paths, measurements, versions, identifiers, dates. Adjacency guard: if the checker's own reader produced a value fused to its neighbor, set it aside rather than asserting it missing.

**chunk_split()** — for a segment that fails containment, greedily cover it with the largest chunks that do survive. Names the culprit words.

**furniture_class()** — classify stripped lines against the strip policy in plain language, independent of the cleaner's implementation.

### Extractor independence

| format | cleaner uses | checker uses |
|---|---|---|
| pdf | pymupdf | pypdf |
| docx | pandoc | zipfile + xml.etree over word/document.xml |
| html | pandoc | html.parser, tag boundaries preserved |
| text | open() utf-8 | byte read + BOM probe |

### Output format

- One `.check.md` per source: verdict, fails with verbatim text and source line numbers, furniture audit, edge check
- `SUMMARY.md`: verdict table, findings count, list of every non-pass with links
- `FINDINGS.jsonl`: machine-readable, one JSON object per finding

### Verdict labels

`PASS` · `PASS WITH WARNINGS` · `FAIL` · `PASS + UPSTREAM DEFECT` · `PASS WITH WARNINGS + UPSTREAM DEFECT` · `NO-COUNTERPART` · `ERROR`

### Calibration rules — what to exclude

- Atoms the checker's own extractor produced fused to neighbors → unjudgeable, not a finding
- PDF table cells welded by the checker's reader → unjudgeable
- Icon-font glyphs that differ between readers → use chunk-based edge test, not exact-string

### Skill trigger

Any corpus ingestion pipeline where source files are converted to a clean/normalized format and you need independent verification that content survived.

### Formalization needed at grill session

Config layer (which formats to expect, what counts as furniture), installable skill definition, trigger string.

---

## 2. JSONL Manifest Pattern

A flat, one-object-per-item index file that makes any collection of documents, skills, tools, or repo modules queryable without loading every full file.

### Why it matters

Reading every document to find the relevant one is O(N). Reading a JSONL manifest and fetching only the one matching file is effectively O(1). For repos or databases with hundreds of files this is the difference between a session that loads everything vs a session that loads one thing.

### Field schema — general manifest

```json
{
  "id": "unique-slug",
  "path": "relative/path/to/file",
  "kind": "skill | tool | document | module | config",
  "purpose": "one sentence: what this thing does",
  "triggers": ["when to retrieve this", "keywords"],
  "covers": ["topic1", "topic2"],
  "cannot_answer": ["what it does not cover"],
  "depends_on": ["other-id"],
  "last_verified": "2026-08-27"
}
```

### Field schema — findings/audit JSONL

```json
{
  "source": "path/to/source/file",
  "clean": "path/to/cleaned/file",
  "kind": "pdf | docx | html | text",
  "severity": "FAIL | WARN | UPSTREAM",
  "class": "fused token | stray byte-order mark | respaced value | truncated source",
  "finding": "human-readable sentence naming the problem",
  "detail": "verbatim text or additional context"
}
```

### Where to put manifest files

- Root of a repo → `MANIFEST.jsonl` covering all modules/files
- Root of a folder → `MANIFEST.jsonl` covering that folder
- Per-document companion → `filename.manifest.jsonl` for large multi-section documents

### What to index

Skills, tools, documents, modules, configs — anything a future agent session might need to retrieve. Not: generated artifacts, build outputs, temporary files.

### Formalization needed at grill session

Implement `MANIFEST.jsonl` at novae-xorpus root and per-folder. Define the standard schema for the ECC repo and other corpus targets.

---

## 3. Agent Architecture — On-Device Dual-Agent System

### What it actually is

The on-device dual-agent is the **primary AI for all daily computing**. File management, data compilation, research methods, web lookups, coding, CLI interactions, device control, cloud APIs, coordination with other agents — everything the operator does on a computer, phone, or tablet goes through one or more of these agents. It is not a routing layer to frontier models.

**Frontier models (Claude Code, Gemini, NotebookLM, Perplexity deep dive) are operator-initiated.** The operator opens those sessions manually when they want to use them. The 9B can structure the handoff and prepare context for those sessions, but it does not decide when to escalate. The routing call is always the operator's.

### Model roles

| Model | Role | When |
|---|---|---|
| **0.8B Qwen · Query** | Always-on. Understands the request, breaks it down, structures it, routes. Handles simple tasks directly — prompt cleanup, Q&A, formatting, quick lookups. | Every interaction passes through here first. |
| **9B Qwen · Execution** | Primary workhorse. Does the actual work across everything: files, research, data, web, code, CLI, cloud APIs, multi-step tasks, coordinating with other agents. | Most tasks — escalated from 0.8B when execution depth is required. |
| **Frontier (Claude / Gemini / Perplexity / NotebookLM)** | Hard synthesis, maximum-quality output, deep research sessions, training data generation. | Operator-initiated — opened manually. 9B structures the handoff and provides context; it does not make the routing call. |

### Voice I/O layer (when in use)

```
Voice input
    ↓
STT (dedicated tool — not the LLM)
    ↓
0.8B: clean transcript → structured prompt
    ↓
User reviews / approves
    ↓
9B executes (or 0.8B handles directly if task is simple)
    ↓
TTS reads output in real time
    ↓
VAD: user can interject at any point
    ↓
Follow-up: action routing (web lookup, file op, tool call, API, other agent)
```

### Memory layers

| Layer | Scope | Managed by |
|---|---|---|
| Context window | This session only — cleared on close | Runtime |
| mem0 | Persistent across sessions, selective | 0.8B reads at start / writes key facts at end |
| GCP dataset | Accumulates verified triples for LoRA training | Automated export after each verified session |

Open weights models do not retain anything between sessions. The weights are fixed files on disk. mem0 is what provides persistence. Fine-tuning (the GCP training loop) is the only mechanism that permanently changes what a model knows.

### RLVR training loop

1. Agents do real work during normal sessions
2. Red agent / cross-auditor verifies each output — pass or fail. This is the verifiable reward signal.
3. Verified task → output → verdict triples accumulate in Cloud Storage
4. At threshold (e.g., 500 new verified triples), GCP runs a LoRA fine-tuning job on the 9B
5. Updated LoRA adapter pushed back to home node — base model weights never modified
6. Evaluate 9B against benchmark. If degraded: discard adapter, start fresh from base.
7. Repeat. Each cycle the 9B gets better at the verified task types.

**Why LoRA, not full fine-tuning:** LoRA adds a thin trainable layer on top of frozen base weights. One bad training run → discard the adapter, base untouched. Full fine-tuning modifies base weights permanently. Use LoRA on GCP too — H100 runs burn through credits fast.

### Architecture type

This is **MoA (Mixture of Agents)** — multiple separate models, operator or orchestrator routes to the appropriate one. Not MoE, which is a single model's internal architecture and unrelated.

---

## 4. Project Roster and Repo Build Plan

These are the repos and APKs the grill session must produce repo structure, file tree, and build roadmap for. Source: README grill mandate + operator additions.

### APK layer (Horizons stack)

| Project | Type | Status |
|---|---|---|
| **Horizons-UI** | Android APK — main UI layer for the on-device agent | Needs overhaul (`horizons-ui-v1.2` repo) |
| **Æsc** | Android APK — accessibility daemon #1 | Separate repo |
| **Æyre** | Android APK — accessibility daemon #2 | Separate repo |

All three run independently. Three separate repos is probably the right structure. Tools likely assigned: OpenAI + Node.js + Omni Route.

### Agent layer (NovÆxenti / NovÆxopia / Æsop-Xi)

| Project | What it is | Open question |
|---|---|---|
| **NovÆxenti** | The actual agent logic — models, tools, skills, dual-agent query/executor that runs through Horizons-UI and the accessibility daemons | — |
| **NovÆxopia** | The claw — tools, webhooks, on-device accessibility engines, runtime, PC/MCP servers, IDE access | Whether this compiles with NovÆxenti or must stand alone |
| **Æsop-Xi** | Orchestration layer — memory extraction protocols, agent parameters, ethical agent logic. Rules, guidelines, infrastructure for agents. Implements KAG and RLVR audits. Works with openwiki for file management. | `aesop-xi-protocol` repo needs massive overhaul |

Also needs overhaul: `nova-claw-runtime`, `termux-building-skills` (scope expands to all device agent setups — far beyond Termux).

### Data layer

| Project | What it is |
|---|---|
| **NovÆxorpus** | This repo. Universal memory layer and Data Bank. The vault. |
| **wiki.md (llm-wiki)** | Living knowledge base built from the cleaned corpus. Lives in this repo. |

---

## 5. Four Permanent Agents

These are fixtures in the architecture. Source: README grill mandate §5, operator additions.

### Agent 1 — Search / Web Agent

**Role:** Scrapes for latest updates, breakthroughs, currently trending repos, and industry news applicable to any project in the corpus. Cross-references and reviews what it finds so it can advise on alternative implementations or methods any project could use. Runs on a routine.

**Model:** 9B or frontier (needs decision at grill session).
**Tools:** Perplexity web search substitution + Crawl4AI (open-source Firecrawl equivalent, confirmed 2026-08-26).

### Agent 2 — Help Desk

**Role:** Every app built gets running instructions, like any user manual. Upload a manual into this agent and it grabs data live, answers questions by voice, acts as a live help desk. Works with any operator manual, system, or repo — whatever files are uploaded become its enterprise data bank for questions, how-tos, and troubleshooting on any installed project.

**Model:** Nano / smol (see §7 — exact model to be decided at grill session).
**Platform:** On-device. Loaded on demand, not always-on.

### Agent 3 — Housekeeping / Script Keeper / Data Extractor

**Role:** Goes through at end of day — collects chat logs, tool-calling history, all of it. Writes into structured Markdown and JSONL. Audits against the corpus and uses open web search tools for RLVR audits. Being local and the main hub, it also assists across the full three-device work setup: pulling tools, grepping data, acting as active-workflow cross-agent auditor.

**Platform:** One of the two apps custom-built on Google Cloud Agent Builder using enterprise app-building credits. GCP Agent Builder = managed RAG + tool-calling — exactly the cross-auditor and script-collector role.

### Agent 4 — Red Agent Auditor

**Role:** Cross-auditor, output verification, RLVR signal generator. Verifies every output independently — pass or fail. The verified triples it produces are the training data that feeds the GCP LoRA loop.

**Model:** 9B or frontier.
**Platform:** One of the two apps custom-built on Google Cloud Agent Builder.

---

## 6. GCP Enterprise Build

What gets built on Google Cloud with the enterprise developer credits. The grill session must decide which agents map to which GCP services and produce the build plan.

### What GCP handles

| Capability | What it means |
|---|---|
| **Enterprise query agents** | Agents 3 and 4 (Housekeeping and Red Agent) built on GCP Agent Builder — managed RAG + tool-calling over the operator's data |
| **Data retrieval** | RAG over scripts, chat logs, corpus documents, tool inventory — queried without loading every file |
| **Audit verification** | Red Agent on GCP runs output verification independently of the home node |
| **Bucket storage** | Cloud Storage accumulates verified RLVR triples (task → output → verdict) from every session |
| **Script training** | H100 LoRA fine-tuning jobs on the 9B, triggered at threshold (e.g., 500 new verified triples). Updated adapter pushed back to home node. |

### Constraints

- Use LoRA on GCP — not full fine-tuning. H100 runs burn through credits fast.
- $1,000 enterprise credits cover significant inference time but finite training compute.
- Base model weights never modified — only the LoRA adapter layer updates.
- If a training run degrades the model: discard adapter, start fresh from base.

### What stays on-device

The 0.8B and 9B run entirely on the home node. GCP is compute and auditing — not the primary inference path. The dual-agent operates without GCP connectivity for all local tasks.

---

## 7. Nano Agent Variants

NPU Manager and Help Desk both use sub-2B "nano" or "smol" models. The grill session must decide exact models per role after testing. What is known:

### Constraints (non-negotiable)

- Must run on Android on-device — no torch wheels available on Android, so torch-based models need a separate compute path
- Hexagon NPU is available for hardware-accelerated inference (QAIRT routing)
- Always-on agents must have minimal footprint — sub-1B ideal for the NPU Manager role

### Role-specific requirements

| Agent | Model tier | Why |
|---|---|---|
| **NPU Manager** | Sub-1B, always-on | Handles shell/terminal/low-level device ops. Runs continuously. Needs to fit in NPU SRAM or load/unload fast. |
| **Help Desk** | 1–2B, loaded on demand | Doc Q&A by voice. Heavier than NPU Manager but only active when invoked. Can use CPU fallback if NPU is busy. |

### Candidate model families

- **SmolLM2** (HuggingFace): 135M, 360M, 1.7B — purpose-built for on-device inference, ONNX-exportable
- **Qwen 2.5** 0.5B — lightest in the Qwen family, same inference stack as the 0.8B/9B pair
- **Phi-3 mini** (3.8B) — larger than nano tier, but ONNX-available if NPU Manager role needs more capability

**Open:** exact model selection per role — to be tested and decided at or after the grill session.

---

## 8. Frontier Sessions — Operator-Initiated

This is a standing correction to any framing that describes the 9B as "deciding when to escalate to frontier." That is wrong.

**The operator opens frontier sessions manually.** Claude Code, Gemini, NotebookLM, Perplexity deep dive — the operator reaches for these tools when they want them. The dual-agent does not make that call.

**What the 9B does when the operator opens a frontier session:**
- Structures the prompt and surfaces relevant context from mem0 and the corpus
- Prepares the handoff so the frontier session starts with everything it needs
- Records the output for potential RLVR verification

**What the 9B does not do:**
- Autonomously decide to open or call a frontier model
- Route to frontier without operator action
- Treat frontier escalation as a fallback for tasks it "can't handle"

The 9B handles most things. When the operator wants a Claude Code session, or a Gemini deep research session, or a NotebookLM notebook, they open it. The 9B prepares; the operator drives.

---

## 9. Tool and Asset Assignment

Source: README §"Tool and asset assignment" (2026-08-26). Assignment is per-agent, not global. Some is tried and true, much is untested. The grill session states, per agent, what gets used and what still needs a trial. An assignment with no stated reason is a guess and must be labelled one.

### Critical first (corpus process, ahead of everything)

- **ECC**
- **Honey for Devs**
- **Pocock Skills**

### Full working inventory — all need corpus process treatment

These are source material, not just dependencies. They get skill-and-tool extraction the same way a Qualcomm SDK manual does.

**ECC** · **Honey for Devs** · **Pocock Skills** · **Prime Agent** · **code review graph** · **reverse skills** · **Obsidian skills** · **notebooklm-py** · **Graphify skills** · **OpenAI** · **GSD** · **mem0** · **OB1** · **Omni Route** · **Claude Video** · **Node.js** · **Crawl4AI** · **Perplexity web search substitution** — and more.

### Current likely assignments

| Consumer | Tools | Confidence |
|---|---|---|
| Three-APK setup (Horizons-UI/Æsc/Æyre) | OpenAI + Node.js + Omni Route | Operator: "pretty sure this is going to work well" |
| On-device open-weight models (NovÆxenti) | Prime Agent; possibly Qwen CLI if Qwen drives it | Unconfirmed |
| Claude-based agents | ECC | — |
| Web-search agent | Perplexity web search substitution + Crawl4AI | Confirmed 2026-08-26 |
| Auditing and KAG | Graphify + notebooklm-py | — |
| Specific agents (TBD which) | Claude Video, reverse skills | TBD |
| Multi-agent swarms | Ringer, CrewAI, other swarm tools | — |
| Universal memory bank | mem0, OB1, Reasoning Bank, openwiki + more | To be enumerated |

---

## 10. What the Grill Session Must Produce

Source: README §"What the grill session has to produce" (operator-stated 2026-08-26). This is the mandate.

1. **Evaluate remaining Drive files** — grep every remaining file, determine what is useful in the universal memory layer and database
2. **Purge the legacy vaults and repos** — evaluate three legacy Obsidian vaults for useful files or file-tree structure, then purge the rest
3. **Run chosen files through the corpus process** — everything selected in 1–2 gets `clean.py` + `check.py` treatment. This is the initial structure of the memory layer / Data Bank.
4. **Determine repo count** — how many repositories are needed in the immediate future; extrude information from the "grand repository" into them
5. **Define file format and file tree for each repo** — produce an outline for each repo's README and setup docs
6. **NovÆxenti** — produce the agent logic, model selection, tool/skill wiring spec
7. **NovÆxopia** — produce the claw spec; decide standalone vs. combined with NovÆxenti
8. **Æsop-Xi** — produce the orchestration layer spec

**Format template:** `01-sources/architecture-edits/EDIT-Clarifying Clean Text…` — numbered file-by-file blocks, explicit destination paths, ASCII topology diagrams for dataflow, inline JSON schemas where a contract is defined. Copy the structure, not the content (it is out of date and predates the three-APK architecture).

**Tools, not just skills.** Most source documents describe parameters, guidelines, and pathways — not actions. Expect at least as many tools extracted as skills, likely more. A plan that only produces a skill library has read these documents wrong.

**The grill agent is the traffic director.** The directory tree is not run by hand in Termux. The grill agent executes it and manages development of the architectural framework.

---

## 11. Wiring Still Needed

Not blockers on the grill session, but required for the ecosystem to function:

- Obsidian hooks **and** git hooks on this vault/repo
- **Claude-in-Obsidian** — operator needs to be walked through setup
- **Obsidian ↔ GitHub** — connection, UI, and desktop applications
- **graphify** wired to operator's main account
- **notebooklm-py** skill — so Gemini notebooks attach and update into this repo

---

## Next Grill Session Action Items

1. Re-clean `Nova Corpus — Device Stack.html` with html.parser, re-run check.py — one file, seven known fused tokens
2. Decide on `SKILLS.md/technical-builder-style.skill.zip` — clean its text members or formally document the skip (hard rule 2)
3. Implement `MANIFEST.jsonl` at novae-xorpus root and per folder; define schema for ECC repo and other corpus targets
4. Formalize corpus-verify as an installable skill: trigger string, config layer, skill definition file in `skills/`
5. Close six retrieval gaps from 2026-08-26: part1-lex, Coding-questions (2), TERMUX (2 + PDF), App_Builders_Guide_ (~3), AESOP_XI_ (~1)
6. Wire: Claude-in-Obsidian, Obsidian ↔ GitHub, graphify on main account, notebooklm-py
7. Route working inventory (ECC, Honey for Devs, Pocock Skills) through corpus process
8. Produce build plan for each repo in §4: file tree, README outline, operational mandate
9. Decide nano model selection for NPU Manager and Help Desk after testing (§7)
10. Decide which two GCP Agent Builder apps get built first: Housekeeping/Script Keeper or Red Agent (§6)
11. Per-agent tool assignment: state what gets used, what still needs trial, label guesses as guesses (§9)
