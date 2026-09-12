AUDIT-06-NOVUS_AEXENTI_NOVAECOPIA.md
Audit & Extraction Report: Subfolder 6 of ___Lex-Novi-Æxentis-Copiæ (--• 🦁 NovusÆxenti🌳NovÆcopia🕸️• ~)
Scope: Cognitive MoE Brain (NovusÆxenti), "The Claw" Agent Swarm Harnesses (NovÆxopia), and on-device Qwen weight registries.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/--• 🦁 NovusÆxenti🌳NovÆcopia🕸️• ~  (1uiLHrw-sPJAv0PgaDRI5XhCa6-pIKtWH).
Status: All original files preserved 100% untouched.


________________


1. Purpose & System Roles: The Brain & The Claw
This folder establishes the dual-engine core:


* NovusÆxenti (novus-aexenti/): The Cognitive MoE Brain. Coordinates the asymmetric tandem: Qwen 0.8B intent triage vs. Qwen 9B deep reasoning, integrating with mem0 and the Reasoning Bank.
* NovÆxopia (novaecopia/): "The Claw". The execution harness layer that hosts autonomous CLI swarms (OpenWiki, Hermes 3, Aider, Claude Code Android) and binds them to local MCP servers.


________________


2. Major Discovery: Active On-Device Model Weights
Inside subfolder #QWEN_MODELS:


* Qwen3.5-2B-Q4_0.gguf (File Size: 1.21 GB): Live, pre-quantized GGUF binary ready for direct loading on the Snapdragon 8 Elite Hexagon NPU via GenieX.
* Mer0vin8ian/Qwen3.5-9B-GGUF: Hugging Face repository specifications for your primary 9B executor model.
* Qwen3-4B-Thinking-2507-IQ4_NL.gguf: Specialized reasoning model checkpoint with explicit <think> scratchpads.


Action: Registered into MODEL_REGISTRY in npu_manager.py and codified into README_NOVUS_AEXENTI.md.


________________


3. Subfolder Audit & Swarm Breakdown
--• 🦁 NovusÆxenti🌳NovÆcopia🕸️• ~ /


│


├── 📁 1. #QWEN_MODELS/                      # On-device weight binaries & quantization guides


│   ├── Qwen3.5-2B-Q4_0.gguf (1.21 GB)       # Live binary weights for edge inference


│   ├── Mer0vin8ian/Qwen3.5-9B-GGUF          # Primary 9B executor target


│   └── Qwen3-4B-Thinking-2507-IQ4_NL        # Thinking / reasoning variant


│


├── 📁 2. CLIS-AND-AGENTS/                   # The Swarm Harnesses ("The Claw")


│   ├── open-wiki/                           # LangChain OpenWiki CLI (GLM 5.2 repo cleaner)


│   ├── hermes/                              # Nous Research Hermes 3 function-calling agent


│   ├── aider/                               # Git-tracked autonomous code editor CLI


│   ├── github-mcp/                          # MCP bridge for GitHub repository operations


│   ├── claude-code-android/                 # Termux/Android integration for Claude Code


│   └── Linxr and pockr/                     # Matt Pocock developer skills framework


│


├── 📁 3. On-device_Model-Guide/             # RAM boundaries (keeping active weights under 5GB)


├── 📁 4. Agent-Builds&Guidelines/           # Autonomous persona directives & tool schemas


└── 📁 5. #GOOGLE _AGENTIC-AI/               # Vertex AI Agent Builder cloud fallback configs


________________


4. What Was Combined & What Was Trimmed
* Fluff Trimmed: Bypassed duplicate Google Search PDF dumps (Qwen3-4B-Thinking... - Google Search.pdf [6.2 MB]). The underlying quantization parameters were extracted into MODEL_REGISTRY.
* Combined Harnesses:
   * Synthesized Hermes 3, Aider, and OpenWiki into the unified modular harness directory under novaexopia/modular_harnesses/.
   * Unified the Qwen 2B and 9B configurations into the dual-agent routing logic in 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md.