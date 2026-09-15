---
name: aesop-wiki
description: "Aesop on-device deploy stack — Termux daemons, llama-server supervision, WebSocket bridge, voice pipeline, and model management for Snapdragon 8 Elite."
---

# Aesop Wiki

## What Aesop Is

Aesop is the **deploy and runtime stack** for on-device AI running in Termux on Snapdragon 8 Elite. It owns the GGML inference plane (llama-server with Gemma 4 12B), the WebSocket bridge to the Horizons app, daemon supervision via runit/termux-services, and the voice pipeline wiring.

Repo: `c10vis-poem/aesop`. Termux operational knowledge is in the `termux-helper` skill.

## Repo Structure

```
deploy/phone/daemons/
├── llamad-run          — runit run script for llama-server
├── aesopd-run          — runit run script for WebSocket bridge
└── install-daemons.sh  — symlinks services into termux-services
protocol/
└── bridge-protocol.md  — aesopd wire spec (JSON over RFC 6455)
skills/
└── termux-helper/      — canonical copy of the termux-helper skill
```

## llamad — The GGML Plane

llama-server on port 8081, supervised by runit.

**Model:** Gemma 4 12B IT QAT, Q4_0 quant. Runtime-repacks into i8mm/dotprod on SD 8 Elite. K-quants don't get that optimization.

**Memory:** mmap ON (reclaimable pages), `-fa -ctk q8_0 -ctv q8_0`, `-t 6` (big cores only). Resident: ~7GB model + ~0.5-1GB KV cache.

**Backend ladder:** Adreno 830 via OpenCL → CPU big cores. **NOT on the ladder: Hexagon DSP.**

## aesopd — The Bridge

WebSocket on 8765. Routes `llm.generate` to GGML (:8081) or NPU (:8080) based on `backend` field.

llama-server applies the GGUF's embedded chat template server-side.

## Recent History

| Commit | Change |
|--------|--------|
| `f28c303` | Version-controlled termux-helper; corrected NPU architecture |
| `08cb9f9` | Dropped Hexagon-from-Termux framing, named real HTP path |
| `49a958a` | Full accelerator offload (-ngl) + honest backend-ladder docs |
| `dc80402` | Q4_0 preference, mmap + q8_0 KV cache for tight-RAM survival |

## Credit

Mer0vin8ian Production — Cl0vis/Claude collab.