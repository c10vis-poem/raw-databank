AUDIT_LEX_NOVI_AGENT_ASSETS.md
Audit & Extraction Report: Subfolder 1 of ___Lex-Novi-Æxentis-Copiæ (Agent-Assets&Global-Documentation_Vault)
Scope: Detailed domain audit, W5+H mapping, and architectural extractions from the external vendor vault.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/Agent-Assets&Global-Documentation_Vault (1ksPO96a6y3IEl1awDuUE79nNWsSYqpX4).
Status: All original files preserved 100% untouched.


________________


1. Executive Summary & Core Purpose
Agent-Assets&Global-Documentation_Vault is the Sensory Ground Truth (Tier 1) and Immutable External Reference Library for all silicon, OS, and framework technologies powering the ecosystem.


It contains 13 dedicated domain subfolders and 4 root specifications describing external systems (Qualcomm, Google, Unsloth, Llama.cpp, and research foundations).
The Architectural Transition:
* Historical Rule Cataloged: The folder's CLAUDE.md contained the older four-artifact convention (name.pdf + name.md + name.jsonl + skills.md).
* Active Law Re-established: This document confirms that the four-artifact convention was superseded by the 5+1 Cognitive Memory Architecture, the 5 Manifest Document Types (Tool, Skill, Reference, Memory, Data), and the Living LLM Wiki standard.


________________


2. Domain-by-Domain Audit & Inventory
Domain Subfolder
	Item Count
	Core Technical Assets Mined
	Architectural Destination
	#QAIRT_main
	18 items
	Qualcomm AI Engine Direct SDK, QairtApi, HTP SDK, GenieX runtime flags, LiteRT C++ bindings, ExecuTorch CLIP.
	Enveloped into vendor-corpora/qualcomm-qairt-sdk/ & Spec 01.
	GOOGLE-DEV-DOCS
	10 items
	NDK ASharedMemory, Abstract UNIX domain sockets (\0), LMK shielding (FOREGROUND_APP_ADJ), GCP cross-account handshakes, Gemma 4 deployment.
	Enveloped into vendor-corpora/google-android-platform/ & Spec 01.
	unsloth-docs
	4 items
	Unsloth local UI, Llama-server OpenAI endpoint deployment guides (PDF & MD), GGUF export parameters.
	Enveloped into vendor-corpora/unsloth-docs/ & Spec 03.
	llama-docs
	2 items
	llama.cpp-npu and native C/C++ inference engine documentation.
	Enveloped into vendor-corpora/llama-docs/ & Spec 01.
	FraQAT
	12 items
	Fractional Quantization-Aware Training research papers, full Markdown transcriptions, and JSONL data banks.
	Enveloped into 03_recall_cache/ quantization specs.
	Continual harness
	1 item
	87KB full-text canonical research paper: Online Adaptation for Self-Improving Foundation Agents.
	Enveloped into Prime Agent Mode B specifications in Spec 03.
	Snapdragon NPU LLM
	6 items
	Proven benchmarks running LLMs on Hexagon DSP (verified 31 tok/s on older v69; informs 90 tok/s on v79).
	Ingested into 02_wiki_md/architectures/snapdragon_npu.md.
	KV-CACHE_quantization
	1 item
	TurboQuant guide for llama.cpp, cutting attention KV-cache RAM footprint by up to 60%.
	Ingested into 03_recall_cache/kv_store/.
	Readme-Notes
	4 items
	Historical readmes in .docx and .pdf formats.
	Retained untouched in place for historical provenance.
	Edge AI hub integration
	Subfolder
	Model compilation workflows for Qualcomm AI Hub.
	Ingested into vendor-corpora/qualcomm-qairt-sdk/.
	@ skill manifest jsonl
	Subfolder
	Manifest conventions linking document artifacts on shared_basename.
	Formalized into Master Spec 00 & Spec 02.
	#GOOGLE _AGENTIC-AI
	Subfolder
	Vertex AI Enterprise Agent Platform guides ($1,000 credit pipeline).
	Ingested into cloud fallback routes in Spec 03.
	Automated Build Android...
	Subfolder
	GitHub Actions configurations for building headless Android daemons.
	Ingested into repository CI/CD templates.
	

________________


3. Key Technical Insights Preserved
1. Direct GGUF Inference on Qualcomm NPU (GenieX):
   * Confirmed from #QAIRT_main: GenieX supports running GGUF Q4_0 directly on Snapdragon NPU via the GGML Hexagon backend without requiring offline x86 Linux compilation.
2. Zero-Copy Shared Memory (Google NDK):
   * Confirmed from GOOGLE-DEV-DOCS: ASharedMemory_create + mmap + abstract UNIX sockets (sun_path[0] = '\0') with SCM_RIGHTS bypasses Android's 1MB Binder IPC limit completely.
3. Reset-Free Agent Self-Correction:
   * Confirmed from Continual harness: Agents improve by updating prompt layers (/refine) over an immutable base prompt with automated rollback snapshots, eliminating catastrophic forgetting.