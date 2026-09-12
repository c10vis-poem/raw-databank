AUDIT-08-DOT_CLAUDE.md
Audit & Extraction Report: Subfolder 8 of ___Lex-Novi-Æxentis-Copiæ (.Claude )
Scope: Claude Code CLI configuration, SuperClaude framework, cognitive personas, and prompt skill repositories.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/.Claude  (1ViB2jLZTI1IRcMF5_Yf6WXXj7IU3U0kk).
Status: All original files preserved 100% untouched.


________________


1. Purpose & System Role: The Mode A Prompt Architecture
This folder houses the Mode A (Claude Code CLI + Everything Claude Code) configuration framework:


* Standardizes slash commands, prompt personas, and custom development methodologies for terminal sessions.
* Separates prompt instruction wrappers from executable codebases per CLAUDE.md:


"WHERE: Documentation only. Code does not live here — the vendored checkouts were excised; each entry records what it is and where its source lives."


________________


2. Major Discovery: SuperClaude Framework
* c10vis-poem/SuperClaude_Framework (Forked from SuperClaude-Org):
   * Significance: A comprehensive configuration layer that supercharges Claude Code with:
      1. Specialized Slash Commands: Custom tools for repo analysis, pull-sync workflows, and confidence checking.
      2. Cognitive Personas: Tailored system prompt personas for architecture reviews, code generation, and test-driven development.
      3. Confidence-Check Skills: Pre-commit verification skills that force the agent to self-grade assertions before committing changes.
   * Action: Mined into 04_skills_runtime/prompt_skills/ and novaexopia/modular_harnesses/ecc-claude-code/.


________________


3. Subfolder Breakdown & Audit
.Claude /


├── 📄 CLAUDE.md                             # W5+H State of the Union for CLI tools


├── 📑 SuperClaude_Framework.pdf             # Documentation on custom commands & personas


│


├── 📁 1. Claude-Code_SKILLS_/               # Core skills library for Claude Code CLI


│   └── Mapped into: 04_skills_runtime/prompt_skills/


├── 📁 2. skills/                            # Community & custom skill definitions (.md)


├── 📁 3. CLAUDE_CODE-INFO/                  # Environmental notes on running Claude Code in mobile Termux


├── 📁 4. claude-ai/                         # Reference docs for web orchestration (claude.ai/code)


└── 📁 5. Llm Wiki/                          # CLI bridges connecting Claude Code to the Obsidian vault


________________


4. What Was Combined & What Was Trimmed
* Fluff Trimmed: Excluded raw GitHub web page dumps and pull request tracking PDFs, extracting only the active .claude/skills/ definitions.
* Combined Frameworks:
   * Unified the SuperClaude persona rules with Matt Pocock's developer skills framework into the master 03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md.