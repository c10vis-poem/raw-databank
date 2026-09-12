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
     ├── 🛑 red_audit_sandbox/
     ├── ⚖️ rlvr_verifiers/
     └── 🧹 hygiene_reports/






🧩 Compact Tier Summary
⚪ Root Index: MAP.md (human links) & manifest.jsonl (global hashes).
🟢 Tier 1 (01_raw_sources/): Raw PDFs, media, and text. Strictly read-only.
🟣 Tier 2 (02_wiki_md/): The LLM Wiki. Managed via OpenWiki TUI by the Files Executive Agent.
🟡 Tier 3 (03_recall_cache/): Tokenized .jsonl chunks & vectors. Ephemeral machine buffer.
🔵 Tier 4 (04_skills_runtime/): SKILL.md prompts + extracted .sh/.py CLI tools.
🔴 Tier 5 (05_episodic_logs/): Tri-model trajectory logs, red audits & RLVR verifiers.


















🧩 Compact Tier Summary
⚪ Root Index: MAP.md (human links) & manifest.jsonl (global hashes).
🟢 Tier 1 (01_raw_sources/): Raw PDFs, media, and text. Strictly read-only.
🟣 Tier 2 (02_wiki_md/): The LLM Wiki. Managed via OpenWiki TUI by the Files Executive Agent.
🟡 Tier 3 (03_recall_cache/): Tokenized .jsonl chunks & vectors. Ephemeral machine buffer.
🔵 Tier 4 (04_skills_runtime/): SKILL.md prompts + extracted .sh/.py CLI tools.
🔴 Tier 5 (05_episodic_logs/): Tri-model trajectory logs, red audits & RLVR verifiers.












🔄 Data Flow 1: Daytime Ingestion & Context
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












[
 Daily Driver Runs ]
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
│ 🛑 SANDBOXED RED AUDITOR             │
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