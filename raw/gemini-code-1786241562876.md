---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
disable-model-invocation: true
---

# Grill Me

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Process

1. **Iterative Questioning**:
   - Ask questions **one at a time**.
   - For every question, include your recommended answer.
   - If a question can be answered by inspecting the codebase, inspect the codebase directly instead of asking.

2. **Branch Resolution**:
   - Track unanswered assumptions as an open frontier.
   - Do not move to implementation until all critical decision branches are resolved.