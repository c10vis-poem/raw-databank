---
name: tdd
description: Enforce test-driven development loop (red -> green -> refactor) focusing on behavior through public interfaces.
disable-model-invocation: true
---

# Test-Driven Development (TDD)

Execute feature construction using a strict Test-Driven Development loop.

## Loop Rules

1. **Planning**:
   - Define public interface boundaries and primary behavior list.

2. **RED**:
   - Write **one** failing integration/behavior test targeting public interfaces.
   - Confirm test fails for expected reason.

3. **GREEN**:
   - Write minimal implementation code necessary to pass the test.

4. **REFACTOR**:
   - Clean implementation details while staying strictly green. Never refactor on red.
   - Repeat loop per behavior slice.