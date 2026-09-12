---
name: code-review
description: Review the changes since a fixed point along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?).
disable-model-invocation: true
---

# Code Review

Perform a dual-axis review comparing latest workspace diffs against coding standards and project specs.

## Process

1. **Pin Reference**:
   - Determine comparison base (`git diff <target>...HEAD`) and verify non-empty diff.

2. **Parallel Sub-Agent Review**:
   - **Standards Agent**: Audits changes for Fowler code smells, type safety, performance bugs, and adherence to `CODING_STANDARDS.md`.
   - **Spec Agent**: Audits diff against originating ticket/spec to confirm acceptance criteria are met without undocumented scope creep.

3. **Structured Reporting**:
   - Report findings categorized by severity: **Critical**, **Major**, **Minor**, or **Nitpick**.
   - Provide explicit file paths, line references, and runnable code patches for fixes.