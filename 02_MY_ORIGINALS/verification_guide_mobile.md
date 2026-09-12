
Block 1: Visual Architecture Tree
📦 vault_root/
├── 📜 MAP.md            # ⚪ Global map
├── 📊 manifest.jsonl    # ⚪ Global RAG
│
├── 📁 01_raw_sources/   # 🟢 TIER 1 (Cold)
│   ├── 📊 manifest.jsonl
│   ├── 📑 pdf/
│   ├── 🎬 media/
│   └── 📝 text/
│
├── 📁 02_wiki_md/       # 🟣 TIER 2 (Wiki)
│   ├── 📊 manifest.jsonl
│   ├── 💡 concepts/
│   ├── 🏛️ architectures/
│   ├── 🏷️ entities/
│   └── 🧭 indexes/
│
├── 📁 03_recall_cache/  # 🟡 TIER 3 (Cache)
│   ├── 📊 manifest.jsonl
│   ├── ⚡ jsonl/
│   ├── 📐 vectors/
│   └── 🗝️ kv_store/
│
├── 📁 04_skills_runtime/# 🔵 TIER 4 (Skills)
│   ├── 📊 manifest.jsonl
│   ├── 🎯 prompt_skills/
│   ├── 🛠️ extracted_tools/
│   │   ├── cli/
│   │   └── wrappers/
│   ├── ⚙️ runtimes/
│   └── 🛡️ policies/
│
└── 📁 05_episodic_logs/ # 🔴 TIER 5 (Logs)
    ├── 📊 manifest.jsonl
    ├── 📲 daily_driver_sync/
    ├── ⏱️ trajectories/
    ├── 🛑 cross_agent_audit/
    ├── ⚖️ rlvr_verifiers/
    └── 🧹 hygiene_reports/

Block 2: Tier Architecture Cards
========================================
TIER BREAKDOWN & OPERATIONAL CARDS
========================================

[⚪ ROOT: METACOGNITIVE INDEX]
• Path:      / (vault_root)
• Files:     MAP.md & manifest.jsonl
• Operator:  Planning Agent
• Role:      Global routing & hashes

[🟢 TIER 1: COLD SENSORY ARCHIVE]
• Path:      01_raw_sources/
• Folders:   pdf/, media/, text/
• Operator:  Ingestion Pipeline
• Role:      Unaltered ground truth
• Invariant: Strictly Read-Only

[🟣 TIER 2: THE LLM WIKI LAYER]
• Path:      02_wiki_md/
• Folders:   concepts/, architectures/
            entities/, indexes/
• Operator:  Files Executive Agent
            (via OpenWiki TUI)
• Role:      Linked Markdown graph

[🟡 TIER 3: RECALL CACHE]
• Path:      03_recall_cache/
• Folders:   jsonl/, vectors/, kv_store/
• Operator:  Indexing Workers
• Role:      Tokenized machine buffer
• Invariant: Ephemeral & Rebuildable

[🔵 TIER 4: PROCEDURAL RUNTIME]
• Path:      04_skills_runtime/
• Folders:   prompt_skills/, runtimes/
            extracted_tools/, policies/
• Operator:  Compilation Engine
• Role:      SKILL.md & CLI .sh/.py tools

[🔴 TIER 5: EPISODIC STORE & AUDIT]
• Path:      05_episodic_logs/
• Folders:   daily_driver_sync/,
            trajectories/, rlvr_verifiers/
            cross_agent_audit/
• Operator:  Cross-Auditor & Cross Agent Auditor
• Role:      Tri-model logs & RLVR
• Invariant: Append-Only telemetry

Block 3: Daytime Ingestion & Context Flow
       [ 01_raw_sources/ ]
       (Raw Tech Assets)
               │
               ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
        │ Tokenize          │ Invocations
        ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
        │ RAG Chunks        ▲
        └───────────────────┘

Block 4: Nighttime Audit & RLVR Flow
      [ Daily Driver Runs ]
               │
               │ End-of-Day P2P Sync
               ▼
┌──────────────────────────────────────┐
│ 05_episodic_logs/ & HOME AUDITOR     │
│ 1. Aligns Tri-Model Traces           │
│ 2. Compiles Candidate Scripts        │
└──────────────────┬───────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│ 🛑 SANDBOXED CROSS AGENT AUDITOR             │
│ Isolated Ground-Truth Evaluation     │
└────────┬────────────────────┬────────┘
        │ PASS (+1.0)        │ FAIL (-1.0)
        ▼                    ▼
┌──────────────────┐ ┌─────────────────┐
│ GCS Cloud Bucket │ │ Sandbox Fail Log│
│ gs://<repo>-rlvr │ │ Tier 4 Policy   │
└────────┬─────────┘ └─────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│ GCP RLVR SCRIPTER APPLICATION        │
│ • Runs Automated AST & Verifiers     │
│ • Trains Model Weights & Prompts     │
└────────┬─────────────────────────────┘
        │
        └──► Deploy to Edge & Tier 4

Block 5: Verification Checklist (No-Table Format)
========================================
HUMAN OPERATOR VERIFICATION CHECKLIST
========================================

[CHECK 1: DISTRIBUTED MANIFESTS]
• Inspection: Root + all 5 tier folders
• Expected:   Active, non-empty
             manifest.jsonl in each tier

[CHECK 2: LLM WIKI GRAPH]
• Inspection: 02_wiki_md/ via OpenWiki
• Expected:   Zero broken [[wikilinks]]
             Frontmatter sources intact

[CHECK 3: DUAL EXTRACTION]
• Inspection: 04_skills_runtime/
• Expected:   New documentation yields
             both tools (.sh/.py) and
             skills (SKILL.md)

[CHECK 4: P2P SESSION SYNC]
• Inspection: 05_episodic_logs/sync/
• Expected:   Daily logs present with
             Query, Executor, and
             Frontier model trace tags

[CHECK 5: CROSS AGENT AUDITOR GATEKEEPER]
• Inspection: 05_episodic_logs/red/
• Expected:   Only VERDICT_APPROVED
             scripts reach cloud upload

[CHECK 6: CLOUD RLVR VERIFIERS]
• Inspection: 05_episodic_logs/rlvr/
• Expected:   Explicit +1.0 (pass) or
             -1.0 (fail with trace)
             recorded for each test