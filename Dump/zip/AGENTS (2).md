# AGENTS.md — Novaexopia [novaexopia]

## Operating Boundaries & Role Contracts
1. **Zero-Touch to Originals**: Never overwrite, rename, or delete canonical source documents.
2. **Deterministic Output**: All scripts and tools in `tools/` must return exit code 0 on success.
3. **Context Economy**: Load chunks from `chunk.jsonl` or `clean_md/` rather than raw dumps.
4. **Local Co-location**: Apply skills from `skills/` and tools from `tools/` directly within this repository scope.
