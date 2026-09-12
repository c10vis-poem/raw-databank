README.md — Project __NovÆxorpus(NÆX) & Lex-Novi-Æxentis-Copiæ
Master Ecosystem Overview, Federated Multi-Corpora Architecture & Operational Guide
Motto: Xçineribus, in-variis-nunquam-varius, Novi-Æxentis-Copiæ, Vincent
(From the ashes, unwavering in the midst of adversity, new forces of abundance conquer)
Living Core: Æsc & Æyre — The central body representing the living truth of the system; decoupled native APKs forming the on-device execution foundation alongside Horizons UI.
Universal Memory Engine: #d.u.m.b.a.s.s. (Database & Universal Memory Bank Across Split Services)


________________


1. Executive Overview
Project __NovÆxorpus(NÆX) and ___Lex-Novi-Æxentis-Copiæ establish a sovereign, multi-tier cognitive agent architecture spanning edge mobile hardware (Snapdragon 8 Elite Hexagon HTP), dedicated compute servers (NVIDIA Jetson Orin Nano Super), visual terminal workstations (Rubik Pi 3 Dragonwing), and enterprise cloud training pipelines.


This repository serves as the Federated Master Corpus Root, organizing codebases, documentation, memory banks, and procedural tool suites into a coherent, self-improving cognitive operating system.


________________


2. Core Taxonomy & Brand Ligatures
* Horizons UI (horizons-ui): The primary presentation shell and concierge frontend. Built as an Android Chromium WebView with persistent WebSocket bridges to native daemons.
* Æsc (aesc) APK: The native System Terminal & Shell Daemon APK. Serves as a complete replacement for Termux by registering as an OS Accessibility Service and Assistant. Hosts the local ADB loopback on 127.0.0.1:5555 to execute shell commands with UID 2000 (shell) permissions without root.
* Æyre (aeyre) APK: The native Sensory Ingress & Media Daemon APK. Runs bare-metal Silero VAD (Voice Activity Detection), Moonshine Small ONNX STT, Kokoro-82m / Sherpa ONNX TTS, and Video Game SDK screen capture.
* NovusÆxenti (novus-aexenti): The cognitive Multi-Agent MoE brain, coordinating the 0.8B Qwen triage model and 4B/9B query/reasoning models.
* NovÆxopia (novaecopia): "The Claw" — the tool harness runtime, OpenWiki TUI, and MCP capability bridge.
* Æsop-Xi (aesop-xi): Agentic Execution Split Operations Protocol — the tactical orchestration, ethical safety, and behavioral policy governance layer.
* NovÆxorpus (novae-xorpus): The hardened, immutable universal database, LLM wiki vault, and ground-truth repository.
* #d.u.m.b.a.s.s.: Database & Universal Memory Bank Across Split Services ("It isn't 'dumbass-proof' if it hasn't been '#d.u.m.b.a.s.s.' proven").


________________


3. The Federated Multi-Corpora Architecture
Instead of forcing an identical file layout onto fundamentally different data types, the ecosystem organizes into a Federation of Specialized Repositories:


novae-xorpus/ (FEDERATED MASTER CORPUS ROOT & LIVING TRUTH)


│


├── 📜 README.md                             # Global Ecosystem ReadMe & Bootstrap Guide


├── 📜 MAP.md                                # Top-level human navigation ontology


├── 📊 master_manifest.jsonl                 # Federated hash table linking all child repos


│


├── 📁 aesop-xi/                             # 1. CORE ORCHESTRATION & ETHICAL REPO


│   ├── manifest.jsonl


│   ├── arbitration/                         # Resource allocation & priority arbitration logic


│   ├── policies/                            # Hard boundaries, permissions, and tool guardrails


│   └── .incognito_red_sandbox/              # Sealed shadow validation sandbox


│


├── 📁 novus-aexenti/                        # 2. COGNITIVE REASONING & MEMORY REPO


│   ├── manifest.jsonl


│   ├── dual_agent_router/                   # 0.8B Triage vs. 9B Query handshake logic


│   ├── mem0_episodic/                       # In-session habit keys and rolling preferences


│   └── reasoning_bank/                      # System Flywheel (RLVR state tracking & recovery)


│


├── 📁 novaexopia/                           # 3. HARNESS RUNTIMES & 3-APK NATIVE REPO


│   ├── manifest.jsonl


│   ├── horizons-ui/                         # APK 1: Chromium WebView frontend & UI tiles


│   ├── aesc/                                # APK 2: Terminal daemon, ADB loopback (port 5555)


│   ├── aeyre/                               # APK 3: Media daemon, Silero VAD, Moonshine, Kokoro


│   ├── openwiki-tui-harness/                # Terminal user interface (File Admin / Help Desk)


│   ├── modular_harnesses/                   # Swarm extensions (Prime Agent RLM, ECC skills)


│   └── mcp_connectors/                      # Node.js Filesystem MCP, SQLite MCP, Postgres MCP


│


├── 📁 vendor-corpora/                       # 4. VENDOR KNOWLEDGE BASES (IMMUTABLE LIBRARIES)


│   ├── qualcomm-qairt-sdk/                  # Qualcomm QAIRT, HTP v79 FastRPC specs & headers


│   └── google-android-platform/             # Android OS Foreground Services, LMK, Media SDK


│


├── 📁 skills-and-capabilities/              # 5. GENERAL CAPABILITIES & CODE GRAPH REPO


│   ├── manifest.jsonl


│   ├── code-review-graph/                   # PyGraphify / Graphify AST dependency mappings


│   ├── notebook-lmpy/                       # Deep corpus analytical query scripts


│   └── obsidian-skills/                     # Vault hygiene and graph-sync definitions


│


└── 📁 data_vault/                           # 6. THE LIVING LLM WIKI & DATA VAULT


    ├── manifest.jsonl


    ├── 01_raw_sources/                      # Cold archive (immutable ground truth)


    ├── 02_wiki_md/                          # Semantic memory (Zettelkasten conceptual notes)


    ├── 03_recall_cache/                     # Working memory accelerator (JSONL & SQLite KV)


    ├── 04_skills_runtime/                   # Procedural memory (prompt_skills/ & extracted_tools/)


    └── 05_episodic_logs/                    # Episodic telemetry (trajectories & RLVR verifiers)


________________


4. The 5+1 Unified Cognitive Memory Standard
Tier
	Directory
	Cognitive Faculty
	Operational Role
	Root
	MAP.md & manifest.jsonl
	Metacognition
	Master index, global hash registry, cross-tier entity resolution.
	Tier 1
	01_raw_sources/
	Sensory Perceptual Store
	Immutable ground truth: whitepapers, manuals, transcripts (pdf/, media/, text/).
	Tier 2
	02_wiki_md/
	Semantic Memory
	Human- and AI-readable Markdown graph governed via OpenWiki TUI.
	Tier 3
	03_recall_cache/
	Working Memory Accelerator
	High-speed machine recall: pre-tokenized JSONL, vectors, and embedded SQLite.
	Tier 4
	04_skills_runtime/
	Procedural Memory
	Modular prompt skills (prompt_skills/) and deterministic code tools (extracted_tools/).
	Tier 5
	05_episodic_logs/
	Episodic Telemetry
	Trajectory logs, daily driver syncs, RLVR verifiers, and .incognito_red_sandbox/.
	

________________


5. Dual Operational Modes
1. Mode A: Developer Terminal Sessions (Claude Code CLI):
   * Governing Harness: ECC (Everything Claude Code).
   * Tool Suite: honey-crush (large doc ingestion), nexus-mapper (AST code mapping), ecc-planner, and Matt Pocock engineering skills (spec, ticket, tdd, code-review).
   * Prime Agent does not intervene in this mode.
2. Mode B: Sovereign Edge Assistant (On-Device Local Weights):
   * Governing Harness: Prime Agent (from Prime Intellect).
   * Loop Mechanism: Recursive Language Model (RLM) running inside a persistent Python REPL.
   * Inference: Qwen 3.5 models running on Snapdragon 8 Elite Hexagon HTP via Qualcomm GenieX.
   * Continual Harness: Reset-free online adaptation updating prompt state and memories with automated rollback snapshots.
   * Inter-Mode Bridge: Prime Agent calls the claude CLI strictly as an external subprocess tool without nested harness wrapping.


________________


6. Master Documentation Index in Google Drive
* 📄 00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md: Full 10-section canonical master system specification.
* 📄 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md: Decoupled 3-APK framework, ADB loopback, and DroidDesk workstation mode.
* 📄 02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md: #d.u.m.b.a.s.s. division of labor (mem0, OB1, OmniRoute, Reasoning Bank, SQLite, Postgres).
* 📄 03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md: Operational modes, MCP runtime servers, and PyGraphify code graphs.
* 📄 04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md: W5+H System Matrix, clean Markdown pipeline, and JSONL marker extraction.
* 📄 RESUME.md: Comprehensive session state and handoff ledger.


________________


7. Standalone Production Tools Index in Google Drive
* ⚙️ system_housekeeper.sh: Zero-trust Obsidian, Markor, Drive, and Git hook boundary sweeper.
* ⚙️ agent_panel.sh: Interactive terminal control panel menu for the Æsc daemon.
* ⚙️ compile_manifest.py: Universal JSONL manifest compiler and SHA256 checksum generator.
* ⚙️ doc_to_skill_and_tool.py: Automated dual extraction engine converting docs into SKILL.md rules and executable tools.
* ⚙️ npu_manager.py: Snapdragon NPU hot-swap manager over UNIX domain sockets (/dev/socket/npu_manager.sock).
* ⚙️ export_drive_docs.js: Google Apps Script exporting Drive Docs to clean Markdown and JSONL (no PDFs).
* ⚙️ log_builder.py: Mobile episodic telemetry logger appending to agent_logs.jsonl.
* ⚙️ convert_raw_to_markdown.py: On-device doc normalizer stripping web HTML and adding YAML frontmatter.
* ⚙️ generate_jsonl_markers.py: Lightweight JSONL marker generator for low-memory RAG index caches.