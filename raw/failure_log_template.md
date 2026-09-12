# Failure Log

> Review weekly. Patterns emerge fast. Every entry becomes a test case (Skill 2) and feeds the challenge dataset (PDF Step 2).

---

## Entry Format

### [DATE] — [SYSTEM/PROJECT]

**Symptom:**
_What happened? What did you observe?_

**Expected Behavior:**
_What should have happened?_

**Root Cause:**
_What actually went wrong at the source?_

**Failure Type** (pick one):
- [ ] Context Degradation — quality dropped as session/context got long
- [ ] Specification Drift — agent/system forgot or drifted from the original intent
- [ ] Sycophantic Confirmation — agent confirmed incorrect data and built on it
- [ ] Tool Selection Error — wrong tool picked, wrong approach taken by agent
- [ ] Cascading Failure — one failure propagated through the chain, no correction
- [ ] Silent Failure — output looked correct but was functionally wrong

**Blast Radius:**
_Who/what was affected? How bad?_
- Severity: Low / Medium / High / Critical
- Reversible: Yes / No / Partial
- Frequency: One-off / Recurring / Systemic

**Fix Applied:**
_What did you do to resolve it?_

**Prevention:**
_What would stop this from happening again? Config change? Guardrail? Test case?_

**Test Case Generated:**
_Write one. Input → Expected Output → Pass/Fail criteria._

```
Input:
Expected Output:
Pass/Fail:
```

---

## Weekly Pattern Review

| Week | Most Common Type | Recurring System | Action Taken |
|------|-----------------|-----------------|--------------|
|      |                 |                 |              |

---

## Failure Type Frequency Tracker

| Type | Count | Last Seen | Trend |
|------|-------|-----------|-------|
| Context Degradation | | | |
| Specification Drift | | | |
| Sycophantic Confirmation | | | |
| Tool Selection Error | | | |
| Cascading Failure | | | |
| Silent Failure | | | |
