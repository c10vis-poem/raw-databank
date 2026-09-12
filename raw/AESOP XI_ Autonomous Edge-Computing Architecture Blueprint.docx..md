<!-- Converted from AESOP XI_ Autonomous Edge-Computing Architecture Blueprint.docx..pdf — 7 pages -->

## Page 1

## 🌌 AESOP XI: Autonomous
## Edge-Computing Architecture Blueprint
## Heterogeneous System Orchestration, Asymmetric
## Routing, & Autonomous Agent Flywheels
### Specification Version: v2.2-Production-Ready | Target: Multi-Node
### Sovereign Mesh
### 1. Canonical Build Sequence & Execution Roadmap
Phase 1: Grill with Docs Master Architectural Planning & Repo Partitioning Phase 2: Global Knowledge Curation, File Parsing, & Universal JSONL Marker Indexing Phase 3: Tool Harness Ingestion (Pocock, Honey for Devs, Prime Agent, ECC, GSD) Phase 4: 3-APK Engine Deployment (Horizons UI + Shell Daemon + Media Daemon) Phase 5: Local Dual-Model Inference & Continuous Improvement RLVR Loop (GCP) Phase 6: Multi-Node Mesh Orchestration & Autonomous Agent Swarm (Jetson / Pi)
● Priority 1: "Grill with Docs" Master Architectural Session & Strategic Roadmap ○ The Orchestration Driver: Execute the master "Grill with Docs" session first to interrogate baseline documentation and establish the complete technical battle plan. ○ Repository & Directory Partitioning: Formulate the precise directory schemas, define strict repository isolation barriers, and assign individual agent manifests. ○ Skill-to-Agent Allocation: Map exactly which skills, harnesses, and tool endpoints are assigned to which agent runtimes (Node Alpha, Beta, Gamma, or Delta). ○ Data Tiering Strategy: Define explicit boundaries for what gets parsed, what stays on the active "hot plate" (mem0 context cache and local active reasoning ledgers), and what gets archived into the deep cold vault (Obsidian markdown vaults and Postgres OB1 vector stores). ● Priority 2: Global Knowledge Curation & Universal JSONL Marker Indexing ○ Assemble, clean, and partition core technical documentation: Qualcomm QAIRT/HTP SDK, Android Media/Accessibility APIs, Google Vertex AI Agent Builder, Llama Server, and Unsloth. ○ Attach dense JSONL marker schemes to every markdown file, tool repository, and skill guideline to allow direct KAG/RAG indexing without context bloat. ● Priority 3: Tool Harness Ingestion & Action Schemas ○ Transform static reference repositories into machine-executable skills. ○ Ingest developer harnesses: Matt Pocock Skills (Grill-Me, Spec, Ticket, TDD,

---

## Page 2

Code-Review), Honey for Devs, Prime Agent (RLM persistent REPL + Continual Harness with rollback snapshots), ECC, GSD (Get Shit Done), Claude Video, Reverse Skills, Code Review Graph, mem0, and OpenAI/Anthropic LocalAI Omni-Route bridges. ● Priority 4: 3-APK Native Android Deployment (Parallel with Priority 5) ○ Deploy the decoupled 3-APK Android execution suite: Horizons UI (Orchestrator), Shell Daemon APK (Termux-free OS assistant/accessibility access), and Media Daemon APK (Screen-vision + Silero VAD + Speech stack). ● Priority 5: Dual-Model On-Device Inference & Concierge Gateway ○ Deploy the dual-model tandem: Qwen 3.5 0.8B GGUF Q4_0 (Executor) and Qwen 3.5 9B GGUF Q4_0 (Query / Metaprompt compiler). ○ Wire the on-device Concierge Flow: Voice capture $\rightarrow$ Silero VAD $\rightarrow$ Screen Vision context $\rightarrow$ Synthesized clean markdown meta-prompt $\rightarrow$ User verification $\rightarrow$ Frontier Model / LocalAI $\rightarrow$ Kokoro TTS speech output. ● Priority 6: Network-Wide Integration & GCP Cloud Training Flywheel ○ Establish the continuous improvement training flywheel: Real-time inference triples aggregated locally by Home Assistant $\rightarrow$ Packaged for batch audit $\rightarrow$ Validated by Red Agent $\rightarrow$ Exported to GCS $\rightarrow$ GCP Vertex AI / Compute Instances run RLVR (GRPO/Unsloth) fine-tuning $\rightarrow$ Updated weights pushed back to edge. ○ Activate the multi-agent home node: Home Assistant Auditor & Housekeeper, Red Agent Batch Training Auditor, IT Help Desk & Manual Operator, Web Ingestion & News Monitor, and NPU Inference Manager.
### 2. Multi-Node Compute Infrastructure
Node ID Physical Primary Core Primary Platform Function Acceleration Software & & Compute Daemons
NODE Moto Razr Local Snapdragon 8 3-APK Unified ALPHA Ultra 2025 Orchestration Elite Stack & Concierge (Hexagon (Horizons + Hub NPU v79) Daemons), LocalAI, Moonshine/K okoro
NODE BETA Nvidia Jetson Headless Dedicated Postgres OB1 Orin Nano Home Server CUDA Core Protocol, Super & Vector Hub Array (60–70 Home TOPs) Assistant, Red

---

## Page 3

Agent Auditor, Multi-Agent Swarm
NODE Rubik Pi 3 Display Thundercom Dual-Monitor GAMMA (Dragonwing) Workstation & m / Display Helpdesk Qualcomm Engine, Gateway SoC (14+ System Log TOPs) Viewer, IT Manual Search
| NODE DELTA | Google Cloud | Asymmetric | Cloud TPUs / | Vertex AI |
|---|---|---|---|---|
|  | Platform | RAG & Heavy | A100/H100 | Agent Builder |
|  |  | RLVR Training | Instances | ($1,000 |
NODE DELTA Google Cloud
Credit Tier), GCS Buckets, Unsloth/Axolo tl GRPO
### 3. The 3-APK Unified Android Architecture
┌──────────────────────────────────────────────────────── ────────────────┐ │ APK 1: HORIZONS UI │ │ - Chromium Webview Sandbox & Websocket Bridge │ │ - LLM Chat Tile Interface & Terminal GUI Visualizer │ │ - Omni-Route Model Dispatcher (Local vs. OpenRouter Fallback) │ │ - NanoAgent / SmolAgent Inference Orchestration Daemon │ └──────────────────┬─────────────────────────────────┬─── ────────────────┘ │ │ ▼ (IPC / Local Service Bindings) ▼ ┌──────────────────────────────────────┐ ┌──────────────────────────────┐ │ APK 2: SHELL DAEMON │ │ APK 3: MEDIA DAEMON │ │ - OS Assistant / Accessibility Engine│ │ - Screen-Vision Frame Buffer │ │ - Android Sandbox Bypass Gateway │ │ - Silero VAD Ingress Loop │ │ - Raw Shell Tool Execution │ │ - Moonshine STT / Kokoro TTS │

---

## Page 4

│ - Native Termux Shell Replacement │ │ - Game SDK Real-Time Ingress │ └──────────────────────────────────────┘ └──────────────────────────────┘
### 4. End-to-End System Dataflow & Runtime Routing
[ USER VOICE / INTENT ] │ ▼ [ APK 3: MEDIA DAEMON ] ──► Screen Capture + Silero VAD Audio Intercept │ ▼ [ MOONSHINE ONNX STT ] ──► Compiles Raw Voice Transcription │ ▼ [ OMNI-ROUTE / LOCALAI ] ──► Anthropic / OpenAI Format Translation │
├───────────────────────────────────────────────────────┐ ▼ ▼ ┌───────────────────────────────────┐ ┌───────────────────────────────────┐ │ EXECUTOR CORE (0.8B Qwen 3.5) │ │ QUERY CORE (9B Qwen 3.5) │ ├───────────────────────────────────┤ ├───────────────────────────────────┤ │ • mem0 Context Cache (Hot Plate) │ │ • OB1 Vector Database (Postgres) │ │ • Reasoning Bank Ledger Paths │ │ • Universal JSONL Document Index │ │ • Task / Command Execution │ │ • Synthesizes Markdown Meta-Prompt│ └─────────────────┬─────────────────┘ └─────────────────┬─────────────────┘ │ │ └───────────────────┬───────────────────┘ ▼ [ APK 1: HORIZONS UI DISPLAY ] │ (User Verification / Intercept) │ ▼

---

## Page 5

[ FRONTIER MODEL / LOCAL CLOUD ] │ ▼ [ REASONING BANK / ACTIVE EXECUTION LEDGER ] │ ▼ [ HOME ASSISTANT: CROSS-AGENT AUDITOR & LOG COMPILER ] - Real-Time Live Inference Auditing Across Agents - Daily Execution Logs Deduplication & Script Aggregation - Accumulates Task-Output-Verdict Triples Locally │ (Context Reaches Training Threshold?) │ ▼ [ RED AGENT AUDITOR SANDBOX ] - Intercepts Accumulated Training Batches - Air-Gapped Validation Against Nope Data Bank - Certifies Ground-Truth Dataset for RLVR │ ┌────────────────┴────────────────┐ ▼ ▼ [ MATCHES NOPE ] [ PASSED AUDIT ] │ │ (Drop & Recover) ┌───────────────┴───────────────┐ ▼ ▼ [ VAULT / STORAGE ] [ GCP CLOUD STORAGE ] - Obsidian Markdown Vault - gs://business-secure-bucket - Local KAG Graphs - Verified Training Batches │ ▼ [ GCP TRAINING FLYWHEEL ] - Vertex AI Discovery Engine - Unsloth/Axolotl GRPO Jobs - New Weights Pushed to Edge
### 5. Multi-Agent Home Node Topology (Node Beta / Jetson)
● Home Assistant (Cross-Agent Auditor & Housekeeper): Manages real-time cross-agent auditing during live inference sessions, aggregates daily execution logs, compiles draft automation scripts, and packages raw telemetry pairs for downstream training. ● Red Agent Auditor (Batch Training Guardrail): Operates strictly when accumulated

---

## Page 6

context reaches the training compilation threshold, conducting air-gapped safety verification against the Nope Data Bank before datasets are shipped to GCP. ● IT Help Desk & Manual Operator Agent: Indexes local technical documentation, tool schemas, and hardware specs to debug operational failures and suggest system repairs. ● Web Ingestion & News Monitor Agent: Tracks breaking updates in local open-weight models, new tools, and upstream repository changes. ● NPU / Local Inference Manager: Balances weight offloading between Snapdragon Hexagon NPU, Jetson CUDA cores, and fallback cloud APIs.
### 6. GCP Cross-Account IAM Handshake & RLVR Loop
● Business / Contractor Resource Tier: Houses proprietary data in gs://business-secure-vault-bucket/ and grants read-only roles/storage.objectViewer to the personal consumer service account. ● Personal Developer Tier ($1,000 Credit Pool): Vertex AI Discovery Engine (service-PERSONAL_PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount. com) points directly to the business bucket without copying data, absorbing 100% of RAG query costs. ● The RLVR Training Loop: Home Assistant packages verified task triples, Red Agent approves the batch, and the dataset streams to GCS. GCP instances run scheduled GRPO fine-tuning jobs on fixed base weights (Qwen/Llama) using Unsloth/Axolotl, returning fine-tuned GGUF weights back down to Node Alpha and Beta.
### 7. Decentralized Multi-Repository Map
📁 master_workspace/ ├── 📁 file-management-and-skills/ # Master Canonical Docs, JSONL Markers, Tool Schemas (Priority 1 Core)[cite: 1, 4] ├── 📁 horizons-ui-v2.0/ # Kotlin/Java APK 1: Orchestration GUI, Webview, Chat Tile[cite: 8, 9] ├── 📁 nova-daemon-shell/ # Kotlin/Java APK 2: OS Assistant & Accessibility Sandbox Bypass[cite: 8, 9] ├── 📁 nova-daemon-media/ # Kotlin/Java APK 3: Screen Vision, Moonshine STT, Kokoro TTS[cite: 1, 8, 9] ├── 📁 agent-harness-hub/ # Prime Agent (RLM), Pocock Skills, Honey for Devs, ECC, GSD[cite: 1, 7] ├── 📁 localai-omni-route/ # Modality Routing, OpenAI/Anthropic Translation Endpoints[cite: 1, 6] ├── 📁 obsidian-knowledge-vault/ # Graphify Networks, KAG/RAG Markdown Trees, NotebookLM Hooks[cite: 1] ├── 📁 red-agent-auditor/ # Air-gapped Batch Training Verification, Nope Data Bank[cite: 1]

---

## Page 7

├── 📁 node-beta-jetson/ # Postgres OB1 Vector Store, CUDA Inference Servers[cite: 1] └── 📁 gcp-training-flywheel/ # RLVR Export Scripts, Cross-Account IAM Handshake, GRPO Pipelines[cite: 3, 5]
### 8. Universal JSONL Marker Schema
Every markdown documentation file and skill repository includes an attached .jsonl schema block to enable rapid, low-token search indexing across local agents and Vertex AI Discovery engines:
JSON { : "record_id" "SKILL_POCOCK_GRILL_001", : "document_path" "agent-harness-hub/pocock-skills/grill-me.md", : "category" "SKILL_HARNESS", : "target_runtime" "PRIME_AGENT_RLM", "metadata": { : "title" "Grill-Me Architectural Interview Harness", : "description" "Interactive question-driven prompt for technical planning", : [ , , "primary_tools" "claude-code" "open-wiki-cli" "prime-agent"], : [ , "required_context_keys" "repo_scope" "target_architecture"] }, : [ , , , , "retrieval_tokens" "grill" "spec" "architecture" "audit" "pocock"], "entry_points": { : "repl_command" "/skill run grill-me", "jsonrpc_method": "agent.skills.execute" } }