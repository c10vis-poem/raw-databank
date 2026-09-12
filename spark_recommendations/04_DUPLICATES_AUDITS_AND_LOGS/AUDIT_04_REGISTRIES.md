AUDIT-04-REGISTRIES.md
Audit & Extraction Report: Subfolder 4 of ___Lex-Novi-Æxentis-Copiæ (Registries)
Scope: Master system registries, repository bank, model registries, and anti-duplication ledgers.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/Registries (1JvzBZvukd6AtndLe7IrJTEfymv8FvWX0).
Status: All original files preserved 100% untouched.


________________


1. Purpose & The "Anti-Fork" Law (From CLAUDE.md)
In CLAUDE.md, the operational mandate for this folder is stated explicitly:


WHY: "60+ forks with no index is how the same repo got forked three times."
WHERE: The central registry of what exists, where it lives, and its verified build state.
WHEN: Consulted before cloning, forking, or generating any new tool, to prevent duplicate code sprawl.
Target Destination in the Master Corpus:
* Repository Registry: Codified into 02_wiki_md/entities/repo_registry.jsonl and 05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md.
* Model Registry: Codified into npu_manager.py (MODEL_REGISTRY) and 02_wiki_md/entities/model_profiles.md.


________________


2. Internal Structure & Subfolder Breakdown
Registries/


├── 📄 CLAUDE.md                             # W5+H State of the Union & anti-duplication rules


├── 📄 README.md                             # Human overview: "The index of what exists and where"


├── 📊 skill_manifest.json                   # Structured metadata declaring join conventions


├── 📄 llm_wiki.md                           # Machine-facing index


│


├── 📁 1. repo-data-bank/                    # Active specifications for core ecosystem repos


│   ├── omni-claw-blueprint.                 # The unified Claw runtime architecture


│   ├── Personal Agentic Operating Stack...  # Cognitive architecture stack taxonomy


│   ├── Five.layer-file／memory／skill-setup # Early 5-layer memory schema


│   ├── Final -memory-layer-p2p_             # P2P sync protocols between edge and home server


│   ├── FULL.MULTI .TIERED.MEMORY.LAYER...   # Multi-tier memory layer mapping


│   ├── Automated scripts for file mgmt...   # Automation scripts inventory


│   └── (1a)-Horizons.Ui-defined             # Horizons UI initial specification


│


└── 📁 2. old-repo-research/                 # Research on upstream tools & environment setups


    ├── edge-ai-hub-integration.md/.jsonl    # Qualcomm AI Hub model integration notes


    ├── ENVIRONMENT (Markor).md              # Termux/Android operational environment profiles


    └── README (Markor).md                   # On-device Markor editor conventions


________________


3. Detailed Technical Extractions
A. The Master Repository Manifest Pattern (skill_manifest.json)
* Extracted Schema:


{


  "name": "registries",


  "kind": "corpus-section",


  "conventions": {


    "axis": "domain",


    "document_artifacts": ["original", ".md", ".jsonl", "skills.md"],


    "join_key": "shared basename"


  }


}


* Action: Adopted as the join standard across all manifests in Master Spec 00 and Spec 02.
B. The Omni-Claw Blueprint (omni-claw-blueprint.)
* Content: Unifies the multi-APK mobile daemon framework with the Prime Agent execution loop, formalizing the interface between the user's touch/voice input and the background shell daemons.
* Action: Enveloped into novaexopia/ in 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md.
C. Cognitive Architecture Stack (Personal Agentic Operating Stack...)
* Content: Establishes the formal boundary separating Open Brain (OB1 static database proofs), Mem0 (dynamic in-session episodic memory), LLM Wiki (semantic knowledge graph), and Reasoning Bank (RLVR training ledger).
* Action: Codified directly into 02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md.


________________


4. What Was Combined & What Was Trimmed
* Fluff Trimmed:
   * Copy of LM llm Wiki or or Wiki llm - Google Search (28.3 MB raw web scrape PDF) and its markdown duplicate were bypassed. The useful Karpathy LLM-Wiki parameters were already extracted into README_DATA_VAULT.md.
   * Duplicate Markor environment copies (ENVIRONMENT (Markor) (1).pdf and .md) were consolidated into a single environment reference.
* Combined Specifications:
   * Merged the 7 sub-items in repo-data-bank into the master 05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md, establishing a clean single source of truth for all repository paths.


________________


5. Architectural Value
This folder provides the Indexical Glue for the entire ecosystem. It enforces that every repository, model, and script is cataloged in one place before work begins, preventing fragmented forks and redundant implementations.