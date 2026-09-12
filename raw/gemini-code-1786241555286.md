---
name: setup-matt-pocock-skills
description: Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo before using the other engineering skills.
disable-model-invocation: true
---

# Setup Matt Pocock Skills

Bootstrap the repository configuration required for the engineering workflow skills to interact with your codebase, issue tracker, and context files.

## Process

1. **Identify Tracker**:
   - Detect or ask whether issues live in GitHub (`gh`), GitLab (`glab`), or local Markdown files under `.scratch/issues/`.

2. **Configure Triage Vocabulary**:
   - Map canonical status roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) to repo-specific issue labels.

3. **Map Domain Context**:
   - Locate or generate `docs/agents/CONTEXT.md` to establish shared domain terminology and architectural conventions.

4. **Write Configuration**:
   - Save verified configuration to `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and project agent configs.