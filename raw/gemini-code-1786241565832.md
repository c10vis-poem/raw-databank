---
name: to-spec
description: Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
disable-model-invocation: true
---

# To Spec

Synthesize conversation context and codebase state into a structured spec without interviewing the user.

## Process

1. **Context Synthesis**:
   - Extract problem statements, user requirements, and technical context directly from conversation history.

2. **Seam Identification**:
   - Identify existing test seams or define minimal high-level seams needed to test the behavior.

3. **Spec Output**:
   - Generate spec matching the template structure:
     - **Problem Statement**
     - **Solution**
     - **User Stories** (extensive numbered list)
     - **Implementation Decisions** (modules, interfaces, schema)
     - **Testing Decisions**
     - **Out of Scope**
   - Publish to configured issue tracker with `ready-for-agent` label.