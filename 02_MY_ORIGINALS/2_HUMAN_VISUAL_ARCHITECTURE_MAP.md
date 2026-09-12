Recommended Android PDF Export Settings
When converting wide Markdown architecture maps, box-drawing diagrams, and multi-column tables to PDF on an Android device (via browser print preview, Obsidian, Markor, or a markdown viewer):
* Page Orientation: Landscape (Mandatory). Portrait orientation forces line wrapping on monospace code blocks wider than 80 characters, which will distort ASCII diagrams and tables.
* Paper Size: Letter Landscape (8.5 × 11 in / 216 × 279 mm) or A4 Landscape (210 × 297 mm).
   * If your PDF converter supports larger engineering paper sizes and you want the entire system schematic on a single uninterrupted poster view, select Tabloid / Ledger (11 × 17 in) or A3 Landscape.
* Margins: Set to Minimum or None (e.g., 0.25 in / 5 mm).
* Scaling: Set between 70% and 80% (or select "Fit to Page Width"). This ensures that 100-character-wide code frames and complex tables render with zero line breaks.
🗺️ HUMAN VISUAL ARCHITECTURE MAP & VERIFICATION GUIDE
Ecosystem: 5+1 Tier Cognitive Architecture, OpenWiki TUI, and Multi-Agent RLVR Target Audience: System Architect / Operator
1. End-to-End System Schematic
                                      =========================================
                                     ⚪ METACOGNITIVE ROOT: ROUTING & INDEXES
                                     =========================================
                                     [ MAP.md ]         [ manifest.jsonl ]
                                     (Ontology Graph)    (Global Hash Index)
                                                   │
            ┌──────────────────────────────────────┼──────────────────────────────────────┐
            ▼                                      ▼                                      ▼
┌──────────────────────────┐           ┌──────────────────────────┐           ┌──────────────────────────┐
│ 🟢 TIER 1: RAW SOURCES   │           │ 🟣 TIER 2: THE LLM WIKI  │           │ 🟡 TIER 3: RECALL CACHE  │
│ 01_raw_sources/          │           │ 02_wiki_md/              │           │ 03_recall_cache/         │
├──────────────────────────┤           ├──────────────────────────┤           ├──────────────────────────┤
│ • pdf/ (Whitepapers)     │ Ingest &  │ • concepts/ (Atomic MD)  │ Chunk &   │ • jsonl/ (Tokens)        │
│ • media/ (Audio/Video)   │ Screen    │ • architectures/ (Specs) │ Vectorize │ • vectors/ (HNSW/FAISS)  │
│ • text/ (Raw Scrapes)    ├──────────►│ • entities/ (Schemas)    ├──────────►│ • kv_store/ (Fast Lookup)│
│ [local manifest.jsonl]   │           │ • indexes/ (MOC Maps)    │           │ [local manifest.jsonl]   │
└──────────────────────────┘           │ [local manifest.jsonl]   │           └─────────────┬────────────┘
            │                         └────────────▲─────────────┘                         │
            │ Dual Extraction                      │ Managed via TUI                       │ Sub-second
            ▼                                      ▼                                       │ RAG Context
┌──────────────────────────┐           ┌──────────────────────────┐                         │
│ 🔵 TIER 4: PROCEDURAL    │           │ 🖥️ OPENWIKI TUI          │                         │
│ 04_skills_runtime/       │           │ Files Executive Agent    │                         │
├──────────────────────────┤           │ Command Center           │                         │
│ • prompt_skills/ (SKILL) │           └──────────────────────────┘                         │
│ • extracted_tools/ (CLI) │                                                                │
│ • runtimes/ (Shell/Py)   │◄─────────────────────── Loaded into Context Window ────────────┤
│ • policies/ (Heuristics) │                                                                │
│ [local manifest.jsonl]   │                                                                │
└──────────────────────────┘                                                                │
                                                                                           ▼
                                              ┌────────────────────────────────────────────────────────┐
                                              │ 🧠 WORKING MEMORY (Active Context Window)              │
                                              │ Daily Driver Edge Session                              │
                                              │                                                        │
                                              │  [Query Model]     [Executor Model]   [Frontier API]   │
                                              │  (Task Planning)   (Local Scripting)  (Deep Reasoning) │
                                              └───────────────────────────┬────────────────────────────┘
                                                                          │
                                                                          │ End-of-Day P2P Sync
                                                                          ▼
                                              ┌────────────────────────────────────────────────────────┐
                                              │ 🔴 TIER 5: EPISODIC LOGS & HOME CROSS-AUDIT            │
                                              │ 05_episodic_logs/                                      │
                                              ├────────────────────────────────────────────────────────┤
                                              │ 1. Ingest to: daily_driver_sync/                       │
                                              │ 2. Cross-Auditor Agent: Reconstructs tri-model traces  │
                                              │ 3. Script Collector: Compiles candidate tools          │
                                              │ 4. Grounding Check against Universal Database/Memory   │
                                              └───────────────────────────┬────────────────────────────┘
                                                                          │
                                                                          ▼
                                              ┌────────────────────────────────────────────────────────┐
                                              │ 🛑 SANDBOXED CROSS AGENT AUDITOR GATEKEEPER                    │
                                              │ 05_episodic_logs/cross_agent_audit/                    │
                                              ├────────────────────────────────────────────────────────┤
                                              │ • Isolated execution (No external net, clean state)    │
                                              │ • Truth check against universal database               │
                                              │ • Strict deterministic linting & safety audits         │
                                              └───────────────┬────────────────────────┬───────────────┘
                                                              │                        │
                                         VERDICT_APPROVED (+1.0)          VERDICT_REJECTED (-1.0)
                                                              │                        │
                                                              ▼                        ▼
                                              ┌────────────────────────┐  ┌────────────────────────────┐
                                              │ ☁️ GCP CLOUD STORAGE   │  │ 🛡️ RECURSIVE MITIGATION   │
                                              │ gs://<bucket>/rlvr/    │  │ Logged to sandbox quarantine│
                                              └───────────────┬────────┘  │ Updates Tier 4 policies    │
                                                              │           └────────────────────────────┘
                                                              ▼
                                              ┌────────────────────────────────────────────────────────┐
                                              │ ⚙️ GCP RLVR SCRIPTER APPLICATION                       │
                                              │                                                        │
                                              │ • Executes automated syntax & AST harnesses            │
                                              │ • Verifies runtime assertions & state transitions      │
                                              │ • Produces updated weights, adapters & prompt packs    │
                                              └───────────────┬────────────────────────────────────────┘
                                                              │
                                                              └──► Deploys to Tier 4 & Daily Driver

2. Structural & Functional Overview
Tier
	Component & Path
	Operator / Engine
	Primary Data Artifacts
	Invariant Rule
	0
	Metacognitive Index /MAP.md /manifest.jsonl
	Planning Agent / Global Router
	Markdown link trees, JSONL file registry with SHA-256 hashes.
	Must be read before performing global lookups.
	1
	Cold Sensory Archive 01_raw_sources/
	Ingestion Engine
	Raw immutable source files: .pdf, .mp4, .wav, .txt, .html.
	Strictly Read-Only. Never modified by automated agents.
	2
	The LLM Wiki 02_wiki_md/
	Files Executive Agent (OpenWiki TUI)
	Atomic notes (concepts/), system blueprints (architectures/), registries (entities/), MOCs (indexes/).
	All notes require YAML frontmatter and bidirectional links.
	3
	Recall Cache 03_recall_cache/
	Indexing Workers
	Pre-tokenized chunks (jsonl/), vector indices (vectors/), entity caches (kv_store/).
	Ephemeral / Rebuildable. Discardable without data loss.
	4
	Procedural Runtime 04_skills_runtime/
	Compilation Agent
	Extracted tools (extracted_tools/), prompt templates (prompt_skills/), runtimes (runtimes/), policies (policies/).
	Must enforce dual extraction (skills + executable tools).
	5
	Episodic Store 05_episodic_logs/
	Cross-Auditor & Cross Agent Auditors
	Multi-model traces (trajectories/), sync batches (daily_driver_sync/), audit logs (cross_agent_audit/), verifier scores (rlvr_verifiers/).
	Append-Only. Stores telemetry and verifier reward values.
	3. Human Operator Verification Guide
Use this checklist to audit the repository structure, verify synchronization pipelines, and ensure memory integrity across the nodes.
Check 1: Directory & Manifest Integrity
# Verify that all 6 tiers contain an active manifest.jsonl
for dir in . 01_raw_sources 02_wiki_md 03_recall_cache 04_skills_runtime 05_episodic_logs; do
 if [ -f "$dir/manifest.jsonl" ]; then
   echo "PASS: $dir/manifest.jsonl exists ($(wc -l < "$dir/manifest.jsonl") records)"
 else
   echo "FAIL: $dir/manifest.jsonl missing!"
 fi
done

* Pass Criteria: All 6 manifest files exist and are populated with valid JSON objects containing id, path, tier, sha256, and last_synced.
Check 2: The LLM Wiki (02_wiki_md/) Link Graph
1. Open the repository inside the OpenWiki TUI.
2. Run a graph health check to ensure there are no broken links:
   * Every link formatted as [[concept_name]] must resolve to an existing .md file under 02_wiki_md/.
   * Check frontmatter integrity: Confirm that sources:, extracted_skills:, and extracted_tools: arrays contain valid file paths.
3. Verify that 02_wiki_md/indexes/ contains up-to-date Maps of Content (MOCs) reflecting newly ingested concepts.
Check 3: Dual Skill & Tool Extraction Coverage
When a new technical source document (e.g., manual.pdf) is added:
* Tool Extraction Check: Inspect 04_skills_runtime/extracted_tools/cli/ or wrappers/ to confirm that any command syntax or code snippets from the PDF were extracted into executable .sh or .py files.
* Skill Extraction Check: Inspect 04_skills_runtime/prompt_skills/ to confirm that operational workflows or reasoning patterns were formatted into a SKILL.md with standard YAML frontmatter.
* Traceability Check: Verify that the provenance_source field in 04_skills_runtime/manifest.jsonl correctly references the original document in 01_raw_sources/.
Check 4: End-of-Day P2P Sync & Cross-Audit Trace Alignment
1. Sync Check: Confirm that daily driver session logs are transferred via P2P into 05_episodic_logs/daily_driver_sync/YYYYMMDD_session.jsonl.
2. Trace Alignment Check: Verify that each session record interleaves:
   * Query Model: Intent, system context, decomposition steps.
   * Executor Model: Tool parameters, command executions, return codes.
   * Frontier Model: Fallbacks, complex refactors, escalation reasoning.
3. Database Grounding Check: Confirm that the Cross-Auditor evaluated script outputs against the universal database before passing files to the Cross Agent Auditor.
Check 5: Sandboxed Cross Agent Auditor Gatekeeper
Inspect 05_episodic_logs/cross_agent_audit/:
* Confirm that no script was uploaded to the cloud without a corresponding VERDICT_APPROVED record.
* Check rejected scripts in 05_episodic_logs/cross_agent_audit/rejected_*.jsonl:
   * Each rejection must include: error_type, offending_line, sandbox_trace, and violated_invariant.
   * Verify that rejected patterns caused a corresponding update in 04_skills_runtime/policies/ to prevent recurrence.
Check 6: Cloud RLVR Pipeline & Storage Sync
* Storage Ingestion: Check Google Cloud Storage (gs://<repo>-rlvr-training-pipeline/) for incoming verified batches.
* Reward Distribution: Inspect 05_episodic_logs/rlvr_verifiers/:
   * Tasks that pass deterministic unit tests, syntax checks, and state validations must register reward: 1.0.
   * Failed attempts must register reward: -1.0 alongside AST error traces.
* Model Deployment: Verify that new model adapters, weights, or refined prompt skill bundles generated by the cloud scripter synchronize back into 04_skills_runtime/prompt_skills/ on local nodes.




📦 vault_root/
 ├── 📜 MAP.md                           # ⚪ [METACOGNITIVE] Master human ontology & cross-tier map
 ├── 📊 manifest.jsonl                   # ⚪ [METACOGNITIVE] Global RAG catalog, sha256 hashes & index
 │
 ├── 📁 01_raw_sources/                  # 🟢 [TIER 1: COLD ARCHIVE] Immutable sensory ground truth
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of all raw assets & provenance
 │   ├── 📑 pdf/                         #   ├── Source research papers, whitepapers, manuals
 │   ├── 🎬 media/                       #   ├── Raw video lectures, audio memos, screen recordings
 │   └── 📝 text/                        #   └── Web scrapes, raw transcripts, raw API payload dumps
 │
 ├── 📁 02_wiki_md/                      # 🟣 [TIER 2: THE LLM WIKI] Semantic Memory (OpenWiki TUI)
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of conceptual nodes & graph links
 │   ├── 💡 concepts/                    #   ├── Atomic markdown notes (Zettelkasten / topic cards)
 │   ├── 🏛️ architectures/               #   ├── System blueprints, data contracts, interface specs
 │   ├── 🏷️ entities/                    #   ├── Schemas, hardware registers, device profiles
 │   └── 🧭 indexes/                     #   └── Maps of Content (MOCs) & taxonomy graph hubs
 │
 ├── 📁 03_recall_cache/                 # 🟡 [TIER 3: RECALL CACHE] Working Memory Accelerator
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of vector & chunk shards
 │   ├── ⚡ jsonl/                       #   ├── Pre-tokenized chunks for low-latency context injection
 │   ├── 📐 vectors/                     #   ├── Dense embedding indices (FAISS / Chroma / HNSW)
 │   └── 🗝️ kv_store/                    #   └── Key-value tables for fast exact-match lookups
 │
 ├── 📁 04_skills_runtime/               # 🔵 [TIER 4: PROCEDURAL MEMORY] Dual Skills & Extracted Tools
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of all extracted skills & tools
 │   ├── 🎯 prompt_skills/               #   ├── Modular agent definitions (YAML frontmatter + SKILL.md)
 │   ├── 🛠️ extracted_tools/             #   ├── Deterministic tools mined by Files Executive Agent
 │   │   ├── cli/                        #   │   └── Shell utilities & command wrappers (*.sh)
 │   │   └── wrappers/                   #   │   └── Python API wrappers & micro-utilities (*.py)
 │   ├── ⚙️ runtimes/                     #   ├── Master operational scripts & execution hooks
 │   └── 🛡️ policies/                    #   └── Self-correction heuristics & validation schemas
 │
 └── 📁 05_episodic_logs/                # 🔴 [TIER 5: EPISODIC TELEMETRY] Trajectories & RLVR Audits
     ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of sessions, audits & verifiers
     ├── 📲 daily_driver_sync/           #   ├── Ingested logs from edge device sessions
     ├── ⏱️ trajectories/                #   ├── Tri-model traces (Query, Executor, Frontier)
     ├── 🛑 cross_agent_audit/           #   ├── Cross Agent Auditor evaluations & quarantine reports
     ├── ⚖️ rlvr_verifiers/              #   ├── Graded assertions & reward signals (+1.0 / -1.0)
     └── 🧹 hygiene_reports/             #   └── Schema validation logs & broken link audits