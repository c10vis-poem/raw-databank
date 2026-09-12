# Weekly Master Thread Audit — Standard Protocol

*Deploy in the master thread once weekly before consolidation/handoff.*
*Reusable. Lives in artifacts panel as static reference.*

---

## PURPOSE

Master threads accumulate context, files, and decisions over a week. Without disciplined weekly audit, threads become heavy, context degrades, and the launchpad role breaks down. This protocol consolidates the week's work, surfaces patterns, generates the carry-forward briefing, and prepares the thread for archival.

---

## AUDIT CHECKLIST (Run in order)

### Step 1 — Failure Log Review

Walk through the week's work. For every notable failure, generate a Failure Log entry using the standard template:

- **Symptom** (what happened)
- **Expected behavior** (what should have happened)
- **Root cause** (what actually went wrong at source)
- **Failure type** (one or more: Context Degradation / Specification Drift / Sycophantic Confirmation / Tool Selection Error / Cascading Failure / Silent Failure)
- **Blast radius** (severity, reversibility, frequency)
- **Fix applied**
- **Prevention** (config, guardrail, or test case)
- **Test case generated** (input → expected output → pass/fail)

Consolidate failures into a single weekly entry file in /mnt/user-data/outputs/ (e.g., `failure_log_week_YYYY-MM-DD.md`). Append to running failure log archive.

### Step 2 — Prompt & Response Quality Review

Walk through the week's notable Claude outputs. For each significant interaction:

- **What worked:** prompts that hit cleanly, responses that delivered value with minimal back-and-forth
- **What didn't:** prompts that needed multiple retries, responses that drifted from intent, output that required heavy correction
- **Pattern:** is the failure on Derek's prompt construction side, or on Claude's response side? Both?
- **Improvement:** specific phrasing, scope changes, or structure adjustments to try next week

Tie observations back to Nate B Jones 7-skill framework where relevant (specification precision, evaluation, decomposition, failure recognition, trust/security, context architecture, token economics).

### Step 3 — History Consolidation

Inventory everything created this week in this master thread:

- **Artifacts rendered to sidebar** (list by name, confirm they actually appeared)
- **Output files saved** (list paths in /mnt/user-data/outputs/)
- **Resume prompts drafted** (list, note which were deployed)
- **Decisions made** (architecture, routing, scope changes)
- **Side threads spun up or referenced**

Flag for each:
- **KEEP** — carries forward to next master thread, stays referenced
- **ARCHIVE** — saved but not active reference, store in personal archive
- **DELETE** — superseded, redundant, or no longer relevant

### Step 4 — Frequency Tracker Update

Update the failure type frequency tracker:

| Type | Count This Week | Total | Last Seen | Trend |
|------|-----------------|-------|-----------|-------|
| Context Degradation | | | | |
| Specification Drift | | | | |
| Sycophantic Confirmation | | | | |
| Tool Selection Error | | | | |
| Cascading Failure | | | | |
| Silent Failure | | | | |

Note any failure type trending up — that's where to focus prevention work next week.

### Step 5 — Handoff Markdown for Next Master Thread

Generate `handoff_YYYY-MM-DD.md` containing:

- **Active project status** (one paragraph each: RazrPi build, Pivot 2026, NO.VA, Vascu14R, Brain Trust, side threads, tracker thread)
- **Recent decisions** (architecture, routing, scope — last 7 days)
- **Pending action items** (what Derek needs to execute, in priority order)
- **Open questions** (unresolved decisions, blocked items)
- **Updated artifact list** (current sidebar inventory + brief description of each)
- **Active connector status** (which integrations are live and verified working)
- **This week's failure patterns** (top 1-3 from frequency tracker, with prevention notes)
- **Skill score self-assessment** (Nate's 7 skills, current ratings, where the work happened this week)

This file is what gets uploaded into the next master thread alongside the resume prompt.

---

## DELIVERABLES (End of Audit)

1. `failure_log_week_YYYY-MM-DD.md` — output file
2. `prompt_quality_review_YYYY-MM-DD.md` — output file (optional, only if patterns worth noting)
3. `handoff_YYYY-MM-DD.md` — output file, dual-delivered (artifact + file)
4. Updated artifact inventory list (verbal/inline, not a separate file)
5. Routing decisions for next week (which side threads need attention, which need new resume prompts)

---

## DECISION POINT (After Audit Completes)

**Three options:**

1. **Continue in current master thread** — if context budget healthy and no major architecture shifts, keep going. Re-audit in 7 days.

2. **Archive and spin fresh master thread** — if thread is heavy, context is degrading, or major project pivot occurred. Deploy Master Thread Resume Prompt + paste handoff_YYYY-MM-DD.md into new thread. Old thread can be deleted after personal archive saved.

3. **Pause and consolidate further** — if audit surfaced more work than expected (multiple high-priority routing decisions, major spec changes pending). Run a focused work session, then re-audit before deciding option 1 or 2.

---

## NOTES

- Audit cadence: weekly minimum. Trigger early if any of: thread feels heavy, weekly Claude usage approaching 50%, major architectural decision pending, multiple silent failures observed.
- Audit duration target: 30-60 minutes. If consistently exceeding 90 minutes, the audit scope has bloated or the underlying work needs decomposition.
- Audit is for the master thread layer only. Side threads have their own consolidation rhythms and don't get audited from here.
- Derek runs audit; Claude facilitates. Final calls on KEEP/ARCHIVE/DELETE belong to Derek.
