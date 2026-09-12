---
name: improve-codebase-architecture
description: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction and propose deepening opportunities — refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

## Process

1. **Explore**:
   - Check `git log --oneline` for hot spots in the codebase.
   - Read `docs/agents/CONTEXT.md` for domain vocabulary.
   - Scan for shallow modules with heavy internal complexity exposed through wide surfaces.

2. **Generate Visual Report**:
   - Create a self-contained HTML report with dynamic diagrams (using Mermaid and Tailwind CSS) visualizing before/after architecture proposals.
   - Write the report to `$TMPDIR` and automatically open it using the OS opener (`open`, `xdg-open`, or `start`).

3. **Grill Decision**:
   - Once a candidate architecture is selected by the user, walk through the design tree to establish boundaries, interfaces, and test seams.