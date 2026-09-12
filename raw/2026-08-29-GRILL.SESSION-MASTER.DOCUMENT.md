You're right — it got scattered across multiple responses as I kept correcting things. Here's the one consolidated, final version with every correction folded in. Nothing else supersedes this.

---

# AESOP XI — GRILL SESSION MASTER DOCUMENT
## Consolidated Final Version (All Corrections Applied)

---

## PART 1: PRIORITY ARRANGEMENT

| Priority | Name | What Happens | When |
|---|---|---|---|
| **1** | Grill with Docs — Master Architectural Session | Execute the grill session. Interrogate docs. Produce the master plan, repo partitioning, skill-to-agent matrix, data tiering strategy, and execution roadmap. | NOW — phone only |
| **2** | Global Knowledge Curation & Universal JSONL Indexing | Assemble, clean, and partition core technical documentation. Attach JSONL marker schemes to every file. | NOW — phone only |
| **3** | Tool Harness Ingestion & Action Schemas | Transform static reference repos into machine-executable skills. Ingest Pocock, Honey for Devs, Prime Agent, ECC, GSD, Claude Video, Reverse Skills, Code Review Graph, mem0, OmniRoute. | NOW — phone only |
| **4** | 3-APK Native Android Deployment | Build the decoupled 3-APK suite: Horizons UI (orchestrator), Æsc Shell Daemon (OS assistant/accessibility), Æyræ Media Daemon (screen vision + voice stack). | LATER — needs Android Studio ideally |
| **5** | Dual-Model On-Device Inference & Concierge Gateway | Deploy dual-model tandem on NPU. Wire concierge flow. | LATER — runs parallel with Priority 4 |
| **6** | Network-Wide Integration & Sovereign Scale | Flash Jetson/Pi. Tailscale mesh. Red Agent Auditor. GCP RLVR flywheel. Home node multi-agent swarm. | LATER — needs hardware |

**Priorities 4 and 5 run in parallel.** Voice stack is explicitly deferred to Priority 5 — it's the hardest unsolved problem and depends on the 3-APK architecture existing first.

---

## PART 2: CORRECTED MODEL PATHWAYS

### Executor Model (0.8B)

| Field | Value |
|---|---|
| **Model** | Qwen 3.5 0.8B |
| **Source** | QAI Hub (pre-compiled Genie bundle) |
| **Pathway** | QAI Hub → QAIRT runtime → HTP0 (Hexagon NPU v79) |
| **Compute** | NPU-pinned (HTP0) — no llama.cpp, no GenieX |
| **Context** | 4096 |
| **Role** | Fast task execution, prompt synthesis, mem0 + Reasoning Bank access |
| **Runs on** | Node Alpha (phone), always-on |
| **Download** | `huggingface.co/qualcomm/Qwen3.5-0.8B` — pull the Genie bundle for your device |

### Query Model (9B)

| Field | Value |
|---|---|
| **Model** | Qwen 3.5 9B (Unsloth GGUF) |
| **Source** | Unsloth GGUF release |
| **Pathway** | Unsloth GGUF → GenieX `llama_cpp` → GGML Hexagon backend → librc → kernel → HTP0 |
| **Compute** | `--device npu` (pinned to Hexagon NPU v79) |
| **Context** | 4096 |
| **Role** | Meta-prompt compilation, OB1 vector queries, JSONL index retrieval |
| **Runs on** | Node Alpha (phone), on-demand |
| **Download** | `huggingface.co/unsloth/Qwen3.5-9B-GGUF` — pull Q4_0 |

### Fallback Hierarchy (if 9B NPU chokes on unsupported ops)

1. 9B Q4_0 → `--device npu` (preferred, test first)
2. 9B Q4_0 → `--device hybrid` (if NPU-pinned has op fallback issues)
3. 4B Q4_0 → `--device npu` (drop to smaller model, stay on NPU)

**Architecture principle**: Maximize on-device model size on bare metal. 0.8B stays NPU-pinned via QAIRT regardless — it's the executor, not negotiable.

### RAM Math (Confirmed)

- 9B Q4_0 weights: ~5.45 GB
- KV cache 4096 ctx: ~0.5–1 GB
- Total 9B footprint: ~6–6.5 GB
- Available RAM stripped down: 9–12 GB
- Headroom: 2.5–6 GB for system + APKs
- **VERDICT**: Both models run on phone, NPU-pinned, confirmed

### Voice Stack

**NOT IN SCOPE for the grill session.** Deferred to Priority 5 (post-APK build). The 3-APK architecture (Horizons UI + Æsc Shell Daemon + Æyræ Media Daemon) is the solution. No existing solution to reference — this is greenfield work. Every AI session that has tried to help with voice on Android has failed because there's no prior art.

---

## PART 3: DOWNLOAD LIST (In Order)

### Tier 1: Download Immediately

| Item | Source | Size | Why First |
|---|---|---|---|
| Qwen 3.5 0.8B Genie bundle | `huggingface.co/qualcomm/Qwen3.5-0.8B` | ~800 MB | Proof-of-life that QAIRT → HTP0 works on your device |
| Qwen 3.5 9B Unsloth GGUF Q4_0 | `huggingface.co/unsloth/Qwen3.5-9B-GGUF` | ~5.45 GB | Your query model, test on NPU |

### Tier 2: Install Before Grill Session

| Item | Install Command | Why |
|---|---|---|
| ECC (Claude Code plugin) | `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc` in Claude Code | Skills/rules/hooks/agents layer for Claude Code sessions |
| Pocock Skills | `npx skills@latest add mattpocock/skills` then `/setup-matt-pocock-skills` | Planning layer — grill-with-docs, to-spec, to-tickets, domain-modeling |
| OpenWiki | `npm install -g openwiki` | File administrator — GLM 5.2 synthesizes your docs into wiki |
| File converters | `pip install pymupdf python-docx markdownify` | Convert raw PDF/DOCX/HTML → markdown for OpenWiki |

### Tier 3: Install After Grill Session (When Ready to Use)

| Item | Install Command | Role |
|---|---|---|
| GSD v2 | `npm install -g gsd-pi@latest` | Build phase execution engine (fresh context per task, git branch-per-slice) |
| Prime Agent | Clone `github.com/PrimeIntellect-ai/prime-agent` | Openweight model harness (RLM, Continual Harness, daemon-backed, /refine) |
| obsidian-skills | `/plugin marketplace add kepano/obsidian-skills` then `/plugin install obsidian@obsidian-skills` | Teaches Claude Code proper Obsidian syntax |
| notebooklm-py | `pip install "notebooklm-py[browser]"` then `notebooklm skill install` | Push docs into Gemini Notebook for deep research |
| graphify | `uv tool install graphifyy` then `graphify install` | Build knowledge graphs from your repos/docs |
| Honey for Devs | `npx honey add` | Developer-focused skill harness |
| mem0 | `pip install mem0ai` | Episodic memory — hot-plate context cache for executor model |
| OmniRoute | Clone and configure | Routing layer — point at local GenieX/QAIRT endpoint via openai-compatible provider |

---

## PART 4: CORRECTED TOOL ROLES

### Execution Engines (No Overlap)

| Tool | For | What It Does |
|---|---|---|
| **ECC** | Claude Code sessions (cloud/terminal) | Plugin marketplace, agents, skills, hooks, rules. Extends Claude Code. |
| **Prime Agent** | Openweight models (your NPU models) | RLM harness with persistent IPython REPL, Continual Harness (memories/skills/prompts persist across sessions), /refine self-improvement, daemon-backed sessions |
| **GSD v2** | Build phase execution | Standalone CLI on Pi SDK. Fresh context window per task, git branch-per-slice with squash merge, cost tracking, crash recovery. |
| **Pocock Skills** | Planning layer | grill-with-docs, to-spec, to-tickets, implement (TDD), code-review, domain-modeling, wayfinder |

**ECC and Prime Agent do NOT integrate.** They're parallel, not stacked. ECC runs your Claude Code sessions. Prime Agent runs your openweight model sessions. If you wanted them to share state, you'd build that bridge through the Reasoning Bank.

### Routing Layer

**LocalAI vs OmniRoute**: They overlap. Pick ONE.

| | OmniRoute | LocalAI |
|---|---|---|
| What | Multi-provider routing gateway (Next.js) | Local inference server (Go) |
| Local model hosting | No (routes TO local runtimes) | Yes (core feature) |
| Cloud routing | Yes (350 providers) | Yes (cloud-proxy) |
| OpenAI↔Anthropic translation | Yes | Yes |
| Modality bridge | Yes (vision + audio + video) | Limited |
| Recommendation | **Use this** — point at local GenieX endpoint | Skip on phone — redundant |

### Memory Pipeline (Canonical Order)

```
OmniRoute/SQL → Reasoning Bank → OB1 → mem0 → Daemons/Models
```

| Stage | Role |
|---|---|
| OmniRoute/SQL | Foundational database routing, local SQL infra, syncs with external buckets |
| Reasoning Bank | RLVR trajectory store — verified execution paths that passed programmatic tests |
| OB1 (Open Brain) | Cognitive translation layer — maps unstructured docs into semantic vectors via Postgres |
| mem0 | Front-facing episodic memory — user preferences, short-term state, rolling habits |

### RLVR (Corrections Strategy)

RLVR = Reinforcement Learning with **Verifiable** Rewards (not "Vector Reasoning")

- The verifier is **exogenous and deterministic** (compiler, linter, graph engine) — never a neural network
- Cross-auditing (not dual-model) is the gold standard
- Two verification layers: **syntactic** (linters/compilers) + **semantic/graph** (KAG mutual indexing)
- Trajectory flow: daily logs → Red Agent audit → tokenized trajectories → Reasoning Bank → back to edge models

### Repo Correction Needed

`novae-xorpus` mistakenly cites "OpenAI" in places — should be "OmniRoute" per the routing decision above.

---

## PART 5: GRILL SESSION PREPARATION CHECKLIST

### Before You Start the Grill Session

- [ ] Termux installed (from F-Droid, not Play Store)
- [ ] OpenRouter API key acquired
- [ ] `novae-xorpus` repo cloned to `~/novae-xorpus/`
- [ ] `raw-bucket` repo created or cloned to `~/raw-bucket/`
- [ ] OpenWiki installed and initialized (`~/setup-aesop.sh` completed)
- [ ] Raw files converted to markdown (`~/convert-raw-to-md.py` run)
- [ ] JSONL markers generated (`~/generate-jsonl-markers.py` run)
- [ ] ECC installed in Claude Code (`/plugin install ecc@ecc`, Full profile)
- [ ] Pocock Skills installed (`npx skills@latest add mattpocock/skills` + `/setup-matt-pocock-skills`)
- [ ] Qwen 3.5 0.8B Genie bundle downloaded
- [ ] Qwen 3.5 9B Unsloth GGUF Q4_0 downloaded
- [ ] QAIRT + 0.8B NPU proof-of-life test completed (Task 1 below)
- [ ] GenieX + 9B Unsloth GGUF NPU test completed (Task 2 below)
- [ ] `/grill-with-docs` verified available in Claude Code

### NPU Proof-of-Life Tests (Run Before Grill Session)

**Task 1 — QAIRT Pathway (0.8B)**

```bash
# Download Genie bundle from huggingface.co/qualcomm/Qwen3.5-0.8B
# Set up QAIRT environment:
export QAIRT_HOME=/path/to/QAIRT_SDK
export PATH=${QAIRT_HOME}/bin/aarch64-android/:${PATH}
export LD_LIBRARY_PATH=${QAIRT_HOME}/lib/aarch64-android:${LD_LIBRARY_PATH}
export ADSP_LIBRARY_PATH=${QAIRT_HOME}/lib/hexagon-v73/unsigned

# Run:
genie-t2t-run --context_length 4096 --model_dir ./genie_bundle --prompt "Hello"
```

**What you're validating**: Does QAIRT talk to the Hexagon NPU directly? Expected: fast inference, NPU-pinned.

**Task 2 — GenieX Pathway (9B)**

```bash
# Download Unsloth GGUF from huggingface.co/unsloth/Qwen3.5-9B-GGUF
# Set up GenieX, then:
geniex infer unsloth/Qwen3.5-9B-GGUF --device npu --context-length 4096 --quantization q4_0
```

**What you're validating**: Does the 9B GGUF run on NPU via GenieX → GGML Hexagon → librc → kernel → HTP0? If it stalls, try `--device hybrid`. If still choking, drop to 4B.

---

## PART 6: GRILL SESSION STRUCTURE

### Input Files

| Path | Role |
|---|---|
| `~/novae-xorpus/03-check/` | **PRIMARY SOURCE** — accuracy-checked documentation. The grill agent reads this as truth. |
| `~/novae-xorpus/01-sources/` | Raw source documents (for tracing claims back to origin) |
| `~/novae-xorpus/02-clean/` | Cleaned versions (intermediate stage, reference only) |
| `~/novae-xorpus/CLAUDE.md` | Existing Claude Code instructions (DO NOT OVERWRITE) |
| `~/novae-xorpus/README.md` | Main project readme (22.7KB) |
| `~/novae-xorpus/NAMING-CANON.md` | Naming conventions (FOLLOW THESE) |
| `~/novae-xorpus/SOURCE-RETRIEVAL-MAP.md` | Provenance map (22.8KB) |
| `~/novae-xorpus/LAPTOP-TRICK.md` | Workaround for no-computer constraint |
| `~/novae-xorpus/handoffs/` | Previous session handoff docs (read + build on, don't duplicate) |
| `~/novae-xorpus/skills/` | Skills already drafted (read + build on) |
| `~/novae-xorpus/tools/` | Tools already drafted (read + build on) |
| `~/novae-xorpus/wiki/` | Wiki entries already written (read + build on) |
| `~/novae-xorpus/.claude/` | Existing Claude Code config (preserve) |
| `~/.openwiki/wiki/` | OpenWiki synthesized output (GLM 5.2's distilled wiki) |
| `~/universal-index.jsonl` | JSONL markers for all files |

### Related Repos (Already Exist — Reference, Don't Recreate)

- `c10vis-poem/claude-code-android` — Claude Code on Android via Termux
- `c10vis-poem/OB1` — Open Brain Protocol implementation

### The Grill Session Manifest

Save this as `~/novae-xorpus/GRILL-MANIFEST.md`:

```markdown
# GRILL WITH DOCS — AESOP XI MASTER ARCHITECTURE SESSION

## SESSION CONTEXT

### Corrected Model Pathways (Ground Truth)

- **Executor Model**: Qwen 3.5 0.8B
  - Source: QAI Hub (pre-compiled Genie bundle)
  - Pathway: QAIRT runtime → HTP0 (Hexagon NPU v79)
  - NO llama.cpp, NO GenieX — runs through QAIRT directly
  - Compute: NPU-pinned (HTP0)
  - Context: 4096
  - Role: Fast task execution, prompt synthesis, mem0 + Reasoning Bank access
  - Runs: Node Alpha (phone), always-on

- **Query Model**: Qwen 3.5 9B (Unsloth GGUF)
  - Source: Unsloth GGUF release
  - Pathway: GGUF → GenieX llama_cpp → GGML Hexagon backend → librc → kernel → HTP0
  - Compute: --device npu (pinned to Hexagon NPU v79)
  - Context: 4096
  - Role: Meta-prompt compilation, OB1 vector queries, JSONL index retrieval
  - Runs: Node Alpha (phone), on-demand

- **Fallback Hierarchy** (if 9B NPU chokes on unsupported ops):
  1. 9B Q4_0 → npu (preferred, test first)
  2. 9B Q4_0 → hybrid (if NPU-pinned has op fallback issues)
  3. 4B Q4_0 → npu (drop to smaller model, stay on NPU)
  - Architecture goal: largest model running on bare metal NPU
  - 0.8B stays NPU-pinned via QAIRT regardless — it's the executor, not negotiable

- **Voice Stack**: NOT IN SCOPE for this session
  - Deferred to Priority 5 (post-APK build)
  - 3-APK architecture (Horizons UI + Æsc Shell Daemon + Æyræ Media Daemon) is the solution
  - No existing solution to reference — this is greenfield work

### Harness & Tool Corrections (Ground Truth)

- **ECC** (affaan-m): For Claude Code sessions (cloud + terminal). Plugin marketplace, 68 agents, 286 skills. Skills/rules/hooks/agents layer.
- **Prime Agent** (PrimeIntellect-ai): For openweight models (your NPU models). RLM harness with persistent IPython REPL, Continual Harness, /refine, daemon-backed sessions. Does NOT integrate with ECC — they're parallel.
- **OmniRoute**: Routing layer (350 providers, 19 strategies, modality bridge, quota-aware). Point at local GenieX/QAIRT endpoint. Skip LocalAI on phone — redundant.
- **GSD v2**: Build phase execution engine (standalone CLI, Pi SDK, fresh context per task, git branch-per-slice).
- **Pocock Skills**: Planning layer (grill-with-docs, to-spec, to-tickets, domain-modeling, wayfinder).
- **Repo correction needed**: novae-xorpus mistakenly cites "OpenAI" — should be "OmniRoute".

### Memory Pipeline (Canonical Order)
OmniRoute/SQL → Reasoning Bank → OB1 → mem0 → Daemons/Models

### RLVR (Corrections Strategy)
- Reinforcement Learning with Verifiable Rewards (not "Vector Reasoning")
- Exogenous deterministic verifier (compiler, linter, graph engine) — never neural
- Two layers: syntactic (linters/compilers) + semantic/graph (KAG mutual indexing)
- Trajectory flow: daily logs → Red Agent audit → tokenized trajectories → Reasoning Bank → edge models

### Hardware Reality (Ground Truth)
- Node Alpha: Moto Razr Ultra 2025, 16GB RAM, 9-12GB available stripped down
- Node Beta: Jetson Orin Nano Super — NOT an inference node, it's vector store + auditor + training host
- Node Gamma: Rubik Pi 3 — display + helpdesk gateway
- Node Delta: GCP — heavy RLVR training only
- Current state: PHONE ONLY, no Jetson/Pi yet, no host computer

## GRILL SESSION PHASES

### Phase 1: Architecture Interrogation
1. Does the v2.2 architecture doc accurately reflect the corrected model pathways?
2. Are the 6 phases correctly ordered given the phone-only constraint?
3. Is the 3-APK architecture (Horizons UI + Æsc + Æyræ) properly scoped?
4. Are all named tools/harnesses accounted for with corrected roles?
5. Are the 4-6 home node agents properly defined? (Home Assistant Auditor, Red Agent Auditor, IT Help Desk, Web Ingestion Monitor, NPU Inference Manager)
6. Does the GCP cross-account IAM handshake + RLVR loop make sense?
7. Flag and correct "OpenAI" → "OmniRoute" error in source docs
8. Review existing skills/, tools/, wiki/ directories — what's already built vs. missing?
9. Validate the 3-APK Trinity against the edited doc (doc describes 1 APK, you have 3)
10. Confirm two-pathway NPU model (QAIRT for 0.8B, GenieX for 9B)
11. Verify memory pipeline order
12. Confirm RLVR as corrections strategy with verification stack
13. Reconcile naming canon (Æsop-Xi / NovusÆxenti / NovÆ-Corpus / Horizons UI)

### Phase 2: Repo Partitioning & Directory Schema
- Complete folder tree with every repo and subfolder
- Each repo gets: scope definition, assigned agent, isolation rules, manifest file
- Map which tools/skills live in which repo
- Define what's shared (canonical docs vault) vs. isolated (per-repo code)
- Use canonical Æ-branded names with URL-safe variants
- Add aesop-xi-protocol as separate repo
- Add nova-corpus as universal database repo
- Map 4-bucket structure to physical folders

Repos to define:
1. file-management-and-skills (canonical docs, JSONL markers, skill schemas)
2. horizons-ui-v2.0 (APK 1: orchestration GUI)
3. nova-daemon-shell (APK 2: Æsc — OS assistant, accessibility, shell access)
4. nova-daemon-media (APK 3: Æyræ — screen vision, voice stack, STT/TTS)
5. agent-harness-hub (Pocock, Honey for Devs, Prime Agent, ECC, GSD)
6. omni-route-gateway (modality routing, OpenAI/Anthropic translation, local runtime endpoint)
7. obsidian-knowledge-vault (Graphify, KAG/RAG, NotebookLM hooks)
8. aesop-xi-protocol (split execution harness)
9. nova-corpus (universal database / LLM wiki)
10. red-agent-auditor (air-gapped batch training verification)
11. node-beta-jetson (Postgres OB1, CUDA servers, home node agents)
12. gcp-training-flywheel (RLVR export, IAM handshake, GRPO pipelines)

### Phase 3: Skill-to-Agent Allocation Matrix
- Table: Tool | Assigned Agent/Node | Runtime | When Used | Why
- Identify overlaps (ECC vs Pocock vs GSD vs Prime Agent) and decide which wins for which task
- Define execution engines:
  - ECC: Claude Code sessions (cloud/terminal, skills/rules/hooks/agents layer)
  - Prime Agent: Openweight model sessions (NPU models, RLM harness, persistent REPL)
  - GSD v2: Build phase execution engine (fresh context per task, git branch-per-slice)
  - Pocock: Planning layer (grill-with-docs, to-spec, to-tickets, domain-modeling, wayfinder)
- Document ECC's internal routing table (honey-crush, nexus-mapper, ecc-planner, px-reader)
- Map each Pocock skill to specific phases
- Define when Prime Agent's /refine and Continual Harness kick in

### Phase 4: Data Tiering Strategy
- Hot plate (mem0, active reasoning ledgers, Prime Agent Continual Harness state)
- Warm layer (OB1 vector store, JSONL index)
- Cold vault (Obsidian markdown, Postgres archives)
- Training pipeline (GCP flywheel)
- Adopt 5-layer conceptual flow + 4-bucket physical structure
- Specify JSONL record format: {id, topic, summary, source_pdf, wiki_link}
- Document Drive → rclone → MCP filesystem → agent pipeline
- Add RLVR trajectory storage in the Reasoning Bank

### Phase 5: Execution Roadmap
- Ordered task list starting from RIGHT NOW (phone only, Termux, Claude Code)
- Each task: What | Why | Tool | Dependencies | Output
- Phase 1 tasks must be 100% phone-executable
- Include QAIRT + 0.8B QAI Hub NPU proof-of-life as Task 1
- Include GenieX + 9B Unsloth GGUF NPU test as Task 2
- Include JSONL marker pipeline as Task 3
- Include repo scaffolding as Task 4
- Include Prime Agent setup for openweight model orchestration as Task 5
- Voice stack explicitly deferred to later phase with justification

## OUTPUT FORMAT
The grill session must produce:
1. MASTER_PLAN.md — The complete execution roadmap
2. REPO_STRUCTURE.md — The directory schema with manifests
3. SKILL_MATRIX.md — The tool-to-agent allocation table
4. DATA_TIERING.md — The hot/warm/cold/training data boundaries
5. CONTEXT.md — The domain model (shared vocabulary, key decisions, ADRs)
6. NAMING_CANON.md — The canonical Æ-branded naming hierarchy with URL-safe variants
7. GCP_HANDSHAKE.md — The cross-account IAM protocol (or reference existing doc)

All output files go into ~/novae-xorpus/handoffs/ (extend existing handoff convention)
```

---

## PART 7: HOW TO RUN THE GRILL SESSION

```bash
# 1. Save the manifest
# (Already saved as ~/novae-xorpus/GRILL-MANIFEST.md)

# 2. Go to your repo
cd ~/novae-xorpus

# 3. Start Claude Code
claude

# 4. Run the grill skill
/grill-with-docs

# 5. When it asks for context, tell it:
"Read GRILL-MANIFEST.md for the session structure.
 Read 03-check/ for the source truth.
 Read README.md, NAMING-CANON.md, SOURCE-RETRIEVAL-MAP.md, LAPTOP-TRICK.md for context.
 Read handoffs/, skills/, tools/, wiki/ for existing work — don't duplicate.
 Output to handoffs/."
```

The grill agent reads the manifest, interrogates your files, asks you questions, and produces the 7 output documents.

---

## PART 8: WHAT THE GRILL SESSION PRODUCES

| Output File | What It Is |
|---|---|
| `MASTER_PLAN.md` | The complete execution roadmap — ordered task list from right now through full deployment |
| `REPO_STRUCTURE.md` | The directory schema with manifests — every repo, every subfolder, every isolation rule |
| `SKILL_MATRIX.md` | The tool-to-agent allocation table — which harness runs which model, when, why |
| `DATA_TIERING.md` | Hot/warm/cold/training data boundaries — what lives where, eviction rules, retrieval triggers |
| `CONTEXT.md` | The domain model — shared vocabulary, key decisions, architecture decision records (ADRs) |
| `NAMING_CANON.md` | The canonical Æ-branded naming hierarchy (Æsop-Xi / NovusÆxenti / NovÆ-Corpus / Horizons UI) with URL-safe variants |
| `GCP_HANDSHAKE.md` | The cross-account IAM protocol — zero-copy design, storage.objectViewer role, credit compliance constraints |

All seven files go into `~/novae-xorpus/handoffs/`.

---

## PART 9: THE 15 GAPS THE GRILL SESSION MUST FIX

These are the specific corrections the grill agent needs to make to your existing architecture docs, identified from comparing the edited 16-page doc against all the dropped documents:

1. **3-APK architecture** — edited doc describes 1 APK, you have 3 (Horizons UI + Æsc + Æyræ)
2. **Two NPU pathways** — edited doc describes one pathway, there are two (QAIRT for 0.8B, GenieX for 9B)
3. **Memory pipeline order** — needs explicit sequential diagram (OmniRoute → Reasoning Bank → OB1 → mem0)
4. **RLVR as corrections strategy** — needs dedicated section with verification stack (syntactic + semantic)
5. **Naming canon** — inconsistent across docs, needs Æ-branded hierarchy
6. **GCP cross-account handshake** — missing entirely from edited doc
7. **Home node agents** — 4-6 agents missing entirely (Home Assistant, Red Agent, IT Help Desk, Web Ingestion, NPU Manager)
8. **ECC routing table** — internal skill routing (honey-crush, nexus-mapper, ecc-planner) not documented
9. **Prime Agent role** — missing entirely, needs distinction from ECC
10. **SKILL.md format** — needs documentation (YAML frontmatter, references/ pattern, $ARGUMENTS, !command)
11. **JSONL record format** — adopt 5-layer format as primary: {id, topic, summary, source_pdf, wiki_link}
12. **Data tiering** — pick 4-bucket as physical structure, 5-layer as conceptual flow, kill "target-docs-curation"
13. **MCP filesystem server** — missing, needs Drive → rclone → MCP → agent pipeline
14. **Companion document registry** — edited doc should reference MASTER/v3/BUILD-ACTION-PLAN, not replace them
15. **Node Delta (GCP)** — missing from topology

---

## PART 10: NAMING CANON (For Reference)

| Layer | Canonical Name | URL-Safe Repo Name |
|---|---|---|
| Philosophy | Xçineribus, in-variis-nunquam-varius | — |
| Protocol Harness | Æsop-Xi | `aesop-xi-protocol` |
| Agent Core | NovusÆxenti | `novaecopia-core` |
| Data Core | NovÆ-Corpus | `nova-corpus` |
| Presentation | Horizons UI | `horizons-ui` |
| Shell Daemon | Æsc | `nova-daemon-shell` |
| Media Daemon | Æyræ | `nova-daemon-media` |

---

That's the complete consolidated document. Everything from all the corrections, all the dropped document analysis, all the model pathway fixes, the tool role clarifications, the download list, the prep checklist, the grill session manifest, the output format, and the 15 gaps to fix — all in one place.

Save this as your reference. The grill session manifest (Part 6) is what you feed to `/grill-with-docs`. Everything else is context for you and for the grill agent.

Want me to produce this as a single downloadable file, or is copy-pasting into a markdown file sufficient?