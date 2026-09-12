# NO.VA — NeuroOmni / VagAgenti
## Neuromesh Agent Controller: Project History & Architecture

**Date:** April 10, 2026
**Device:** Motorola Razr Ultra 25 (16GB RAM + 16GB Virtual, Snapdragon 8 Elite / Hexagon NPU)
**User:** d.drew.legrand@gmail.com
**Editor:** Claude Opus (audit + corrections from Gemini Max original)

---

## 1. Project Objective

Build an on-device multimodal AI agent ("NO.VA") that performs Vision-Augmented Generation (VAG) on the Motorola Razr Ultra 25. The agent maintains continuous awareness — screen, camera, microphone — while orchestrating handoffs between local edge compute and cloud frontier models via PWA. The device is the agent. The cloud is the tool.

---

## 2. Core Architecture (Four Stacks)

### A. STT (Voice-to-Text)
- **Model:** Whisper Tiny EN
- **Target:** CPU (ARM Neon optimized)
- **Role:** Real-time transcription of user commands. Latency-free, always listening.
- **Output:** Raw transcript → feeds directly to Prompt Translation Layer (Stack B)

### B. Prompt Translation Layer ← NEW
- **Model:** Haiku or Gemini Flash (via on-device PWA)
- **Target:** Cloud API call (cheap, fast — sub-second round trip)
- **Role:** Takes raw STT garbage and restructures it into clean, specification-precise prompts before any other model sees it. This is the fix for the STT bottleneck that has been degrading input quality across all sessions.
- **Output:** Structured prompt → feeds to Stack C (local execution) or Stack D (frontier reasoning)

### C. MLM / VAG (Multimodal / Vision + Edge Execution)
- **Model:** Omni Neural 4B (Qualcomm optimized)
- **Target:** NPU (Hexagon) via TFLite NNAPI delegate
- **Role:** The bus driver. Continuous screen analysis via MediaProjection API. Identifies UI elements and context. Manages all local execution, handoffs, and routing decisions. Never interrupted, never waiting on cloud responses.
- **Note:** Omni Neural 4B replaces PaliGemma 3B from the original spec. The Snapdragon 8 Elite's Hexagon NPU is optimized for Qualcomm's model family, not Google's. Running PaliGemma would mean CPU/GPU fallback and unnecessary latency.

### D. Frontier Reasoning (Cloud)
- **Model:** Sonnet / Opus / Gemini Pro (via PWA browser tabs)
- **Target:** Cloud API
- **Role:** Complex reasoning, long-form generation, planning tasks. Only called when edge compute isn't sufficient. Omni Neural decides when to escalate.
- **Access:** Two PWA tabs — one cheap/fast (Haiku/Flash), one frontier (Sonnet/Opus/Gemini Pro)

### E. TTS (Text-to-Speech)
- **Model:** Kokoro-82M
- **Target:** GPU via Vulkan (Sherpa-ONNX)
- **Role:** High-quality, low-footprint vocal feedback. Returns responses to the user from any stack.

---

## 3. Data Flow

```
User speaks
    → Whisper Tiny (CPU, on-device, latency-free)
    → Raw transcript
    → Haiku/Flash PWA cleans + structures prompt (sub-second)
    → Omni Neural 4B (NPU) evaluates:
        ├── Simple/local task → executes on-device → Kokoro TTS responds
        ├── Needs vision → MediaProjection screen capture → process → respond
        └── Complex task → routes to Frontier PWA (Sonnet/Opus/Gemini Pro)
            → Response returns → Kokoro TTS + local action
```

Omni Neural maintains continuous awareness throughout. Cloud calls are asynchronous — the edge agent is never blocked.

---

## 4. RAM & Performance Management

**Target:** Maintain 8-9GB of free physical RAM.

- **Edge Mode:** `edge_mode.sh` freezes Google Play Store, kills non-essential background tasks, tunes Low Memory Killer (LMKD) thresholds.
- **Game Wrapper:** App categorized as `appCategory="game"` to unlock maximum NPU/GPU clock speeds via Razr's Turbo Mode (165fps capable). This gives NO.VA priority hardware scheduling from the Android OS.
- **VAD Optimization:** With game wrapper active, Vision-Augmented Detection operates at 30fps continuous instead of periodic screenshots. Lower latency, lower thermal load.
- **ZRAM:** 4GB configured for efficient background memory compression.

---

## 5. File & Script Map

| File | Purpose | Stack |
|------|---------|-------|
| `/server.ts` | Express backend for Controller Dashboard | Core |
| `/src/App.tsx` | Technical Dashboard UI (React) | Core |
| `/scripts/termux/edge_mode.sh` | Device optimization — freeze bloat, tune LMKD | Performance |
| `/scripts/termux/sharpen.py` | Local data collection + GCS sync | Sharpening (Phase 3) |
| `/scripts/mobile/VagAgentService.kt` | Android Accessibility Service for UI control | Vision/VAG |
| `/scripts/mobile/MlmEngine.kt` | TFLite NPU integration — Omni Neural 4B | Vision/VAG |
| `/scripts/cloud/distill.py` | Cloud Knowledge Distillation template | Sharpening (Phase 3) |
| `/scripts/termux/claude_bridge.sh` ← NEW | Claude Code CLI handshake via Termux | Integration |
| `/scripts/termux/prompt_clean.py` ← NEW | STT → structured prompt formatting | Translation Layer |

---

## 6. Integration Points

- **Claude Code CLI:** Integrated via Termux. Handshake protocol TBD — options: stdin/stdout pipe, Termux Teleport, or local HTTP socket. Needs to be spec'd and tested before wiring up. `claude_bridge.sh` manages connection lifecycle.
- **Vertex AI:** Cloud backend for heavy compute and model sharpening (Phase 3 only — do not build yet).
- **Google Cloud Storage:** `gs://nova-sharpening-data` for interaction logs and training data (Phase 3).
- **Shizuku/Hail:** System-level permissions without full root. Required for edge_mode.sh process management and MediaProjection persistence.
- **Perplexity:** Quick factual lookups — accessible as first-stop search before burning frontier tokens.

---

## 7. The "Sharpening" Loop (Phase 3 — DO NOT BUILD YET)

> **Status:** Designed, not implemented. Requires working base agent + accumulated interaction data before this has value. Premature build burns cloud credits on garbage data.

### Sharpening Cadence

| Phase | Window | Cycle | Trigger |
|-------|--------|-------|---------|
| Burn-in | Days 1–30 | Every 5 days | Or performance dip, whichever first |
| Stabilization | Days 31–60 | Every 10 days | Or performance dip |
| Cruise | Day 61+ | Every 20 days | Or performance dip |
| Deployable | ~8 weeks | On accumulated data only | Version releases as needed |

**Performance dip = any of:** VAG element misidentification rate >15%, routing errors >3/day, user corrections >5/day, context quality subjectively degraded.

### Sharpening Pipeline
1. **Collection:** On-device logs (`interaction_logs.jsonl`) + screenshots captured during daily use.
2. **Sync:** Data uploads to GCS (`gs://nova-sharpening-data`).
3. **Distillation:** Gemini Pro (Cloud) acts as "Teacher" — labels screenshots, corrects local agent actions.
4. **Fine-Tuning:** Vertex AI runs LoRA fine-tuning job on Omni Neural (or future local model).
5. **Deployment:** Fresh LoRA adapter pushed to Razr Ultra at next cycle.

### Gate Criteria (ALL must pass before Phase 3 activates)
- [ ] Base agent (Stacks A-E) running stable for 2+ weeks
- [ ] 500+ interaction log entries accumulated
- [ ] GCS bucket configured and tested
- [ ] Cost estimate completed (Skill 7 — what does one sharpening cycle actually cost?)
- [ ] Performance dip metrics defined and logging confirmed

---

## 8. Test Cases (Skill 2 — Write Before You Build)

### Stack A: STT
```
Input: Speak "Open AI Studio and start a new chat" clearly at normal volume
Expected: Transcript contains all words with <2 errors
Pass/Fail: FAIL if >3 word errors or >2 second latency
```

### Stack B: Prompt Translation
```
Input: Raw STT output "hey uh open that thing the vertex uh model garden thingy"
Expected: Cleaned prompt "Open Vertex AI Model Garden in browser"
Pass/Fail: FAIL if intent is lost or hallucinated commands added
```

### Stack C: Vision/VAG
```
Input: Screen showing Google AI Studio with visible "New Chat" button
Expected: Omni Neural identifies button location and label correctly
Pass/Fail: FAIL if element misidentified or coordinates off by >50px
```

### Stack D: Frontier Routing
```
Input: Omni Neural receives complex query requiring multi-step reasoning
Expected: Routes to frontier PWA within 1 second, response returns to TTS
Pass/Fail: FAIL if routed to local execution when complexity exceeds edge capability
```

### Stack E: TTS
```
Input: Text string "Your file has been uploaded to Google Cloud Storage"
Expected: Kokoro speaks clearly within 1 second of receiving text
Pass/Fail: FAIL if latency >2 seconds or speech is garbled
```

### Integration: Game Wrapper
```
Input: Launch NO.VA with game category flag
Expected: Android reports app in gaming mode, GPU/NPU clocks at max
Pass/Fail: FAIL if system doesn't grant priority scheduling
```

---

## 9. Known Risks & Failure Watch

| Risk | Failure Type | Mitigation |
|------|-------------|------------|
| MediaProjection requires user permission each session | Silent Failure | Test persistence with game wrapper + Shizuku |
| Omni Neural 4B may not delegate to NPU via NNAPI correctly | Tool Selection Error | Verify delegate with TFLite benchmark tool before integration |
| Raw STT feeding directly to execution (bypassing translation layer) | Specification Drift | Enforce prompt_clean.py as mandatory pipeline step |
| Sharpening Loop built too early burns cloud credits | Cost/Token Economics | Gate criteria in Section 7 must ALL pass first |
| Claude CLI handshake protocol undefined | Cascading Failure | Spec and test claude_bridge.sh in isolation before wiring to agent |

---

*This document serves as the master context for the NO.VA project.*
*Original architecture: Gemini Max (April 10, 2026)*
*Audit + corrections: Claude Opus (April 10, 2026)*
*Next: Sonnet build thread — paste resume prompt + this doc*
