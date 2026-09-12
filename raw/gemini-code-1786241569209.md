---
name: to-tickets
description: Break a plan, spec, or conversation into a set of tickets — tracer-bullet vertical slices, each declaring the tickets that block it.
disable-model-invocation: true
---

# To Tickets

Slice a specification into ordered, tracer-bullet vertical work units ready for parallel or sequential execution.

## Process

1. **Vertical Slicing**:
   - Break functionality into thin vertical slices cutting through schema, API, UI, and tests.
   - Avoid horizontal layer splits (e.g., "write all DB schemas first").

2. **Dependency Graphing**:
   - Explicitly declare `Blocked by:` edges for each ticket.
   - Ensure unblocked frontier tickets can be picked up immediately by fresh agents.

3. **Publishing**:
   - Write as local Markdown under `.scratch/issues/` or push to remote tracker with native blocking links.