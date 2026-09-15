---
source: Nova Corpus — Device Stack.html
cleaned: 2026-08-26
converter: pandoc html->plain (style/script stripped)
---
Nova Corpus — Device Stack

NOVA CORPUS · DEVICE STACK

modu14r_inc. · hardware mesh + network topology

NODE_ALPHA · ONLINE NODE_BETA · CONFIGURING NODE_GAMMA · CONFIGURING 2026-08-06

P2P MESH TOPOLOGY

TAILSCALE OVERLAY · ALL NODES

┌──────────────────────────────────────────────────────────────────────────────────────────┐ │ TAILSCALE OVERLAY — P2P MESH │ │ all nodes on the same network · NAT traversal · encrypted point-to-point │ └──────────────────────────────────────────────────────────────────────────────────────────┘ ┌───────────────────────────────────┐ │ NODE_ALPHA · Razr Ultra │ │ SM8750 · 16 GB · ~45 TOPS │ │ Hexagon HTP v79 │ │ ● Horizons UI (lifecycle core) │ │ ● novus-agenti · NovA-Claw │ │ ● CCR on-device sessions │ └──────────────┬────────────────────┘ │ │ Tailscale · WiFi │ ┌──────────────┴────────────────────┐ │ NODE_BETA · Jetson Orin Nano Super │ │ 8 GB · 512 GB DDR4 SSD · ~67 TOPS │ │ MAIN COMPUTE HUB · headless │ │ ● peer-agent (Hydra rotation) │ │ ● utilities-agent (housekeeping) │ │ ● inference server │ └──────────────┬────────────────────┘ │ │ HIGH-SPEED DATA CABLE (wired · direct) │ ┌──────────────┴────────────────────┐ │ NODE_GAMMA · Rubik Pi 3 / DragonWing │ │ 8 GB · ~128 GB SSD · ~14 TOPS │ │ VISUAL OS · dual monitor · keyboard │ │ ● desk display (VNC server) │ │ ● DragonWing SoC on-board │ └──────────────┬────────────────────┘ │ │ Tailscale · WiFi (to ALPHA / mesh) │ ┌──────────────┴────────────────────┐ │ THIN CLIENT (no compute node) │ │ Galaxy Tab S9 FE+ · Wi-Fi only │ │ · SSH → NODE_BETA (headless) │ │ · AVNC → NODE_BETA (desktop VNC) │ │ · Termux · SD card (Jetson flash) │ └───────────────────────────────────┘

NODE_ALPHA ACTIVE

Motorola Razr Ultra 2025

CHIPSM8750 · Snapdragon 8 Elite

RAM16 GB

STORAGE~512 GB

AI TOPS~45 TOPS

NPUHexagon HTP v79

FORMPhone · primary user node

SERVICES RUNNING

Horizons UI — lifecycle core; nothing lives without it

novus-agenti — phone agent, runtime manifests

NovA-Claw — execution surface (nova-skills)

CCR — claude.ai UI · on-device execution

ONNX/ORT + Sherpa-ONNX voice layer (in-process)

QAIRT/HTP inference (when models offloaded + bare metal)

NODE_BETA CONFIGURING

Jetson Orin Nano Super

CHIPJetson Orin Nano Super

RAM8 GB

STORAGE512 GB DDR4 SSD (added)

AI TOPS~67 TOPS

FORMHeadless · main compute hub

CONNECTTailscale WiFi ← ALPHA; wired → GAMMA

SERVICES RUNNING

peer-agent — twins with novus-agenti; Hydra cloud rotation

utilities-agent — housekeeping, load/unload operator agents

inference server — swappable backend (never hardcoded)

AVNC server — portable desktop from Galaxy Tab

GCP pipeline endpoint (files-inference-node secretary)

NODE_GAMMA CONFIGURING

Rubik Pi 3 · DragonWing SoC

CHIPDragonWing SoC (on-board)

RAM8 GB

STORAGE~128 GB built-in SSD

AI TOPS~14 TOPS

FORMDesk unit · dual monitor · keyboard

CONNECTwired ← BETA; Tailscale WiFi

SERVICES RUNNING

Visual OS — primary desk display output

Dual monitor hookup

Keyboard input layer

Jetson direct pipe — high-speed data cable

NETWORK LAYER

CONFIG IN aesop-xi-protocol/infrastructure/

JETSON ↔ DRAGONWING High-speed data cable · direct wired · no network hop

RAZR ↔ HOME NODE Tailscale over WiFi · encrypted P2P tunnel

MESH OVERLAY Tailscale — all three compute nodes on same virtual network; NAT traversal

ALL NODES P2P servers · each node is a server · no hub-and-spoke

LOOPBACK SHARED 127.0.0.1:8080 bound by app daemon · Termux shares loopback · NPU access no inversion needed

INBOUND LISTENER App needs listener for mic/voice/WebView-OAuth from Termux — not yet built ABSENT

CONFIG LOCATION Network config lives in aesop-xi-protocol/ — infrastructure/pathways layer

VOICE / NPU PATHWAY

OPERATOR CANON · AUG 2 2026

OPERATOR — NEURO MESH SESSION · AUG 2 2026

"my APK already ships on device with an stt / TTS layer that's running a ONNX/ORT through a llama server. this also allows the model inside of my Termux to utilize the QAIRT model path that allows a GGUF model to run through llama to ggml to kotlin kernel and librc runtimes to land directly on the NPU through the HTP SDK net pathway — I said that pathway will only be utilized when my on device models or my on-device agent through the Horizons UI is offloaded and the APK is running bare metal"

STT / TTS (in-process · always) ONNX/ORT ── llama server ── Sherpa-ONNX Moonshine STT (in-process on AAR) · Kokoro TTS (in-process) NPU CHAIN (only when Horizons UI offloaded + bare metal) GGUF → llama → ggml → Kotlin kernel → librc runtimes → Hexagon HTP SDK → NPU QAIRT model path · HTP pathway · Snapdragon 8 Elite · ~45 TOPS DESIGN CONSTRAINT never hardcode inference backend — keep swappable across all phases

[ STT ] BROKEN MID-CHAIN — points at 127.0.0.1:8091, nothing binds it. Fix: Moonshine in-process on AAR already shipping UNVERIFIED ON DEVICE

[ TTS ] works in-process — Sherpa AAR · Kokoro

[ LLM ] falls to llmRuntime.streamAudio — looks like model problem, is STT problem

CCR ON-DEVICE EXECUTION

TERMUX → CLAUDE.AI

NODE_ALPHA (Razr Ultra) Termux ── start `claude` ────────────────────────────────────────────── session spawns │ claude.ai = user interface (phone browser / app) execution environment = on-device container (not cloud) │ repo access · Drive MCP · GitHub MCP · all tool calls run on device

When claude runs in Termux, the session is an on-device container. The user's phone is both the UI and the execution host. Drive MCP, file reads/writes, git pushes — all run on NODE_ALPHA. The claude.ai web interface is just the chat layer.

THIN CLIENT — NO COMPUTE NODE

SETUP DOCS IN home-node/jetson-orin/ · termux-environment/

DEVICE Samsung Galaxy Tab S9 FE+ · Wi-Fi only · no SIM

ROLE SSH into NODE_BETA · AVNC into NODE_BETA for portable desktop from couch

CONNECT NODE_BETA only — Rubik Pi 3 handles desk, Tab handles couch/portable via VNC

TOOLS Termux (installed) · SD card used to flash Jetson Nano

CONFIG DOCS home-node/jetson-orin/ (VNC server config) · termux-environment/ (AVNC client setup)

MESH TOTALS

TOTAL AI TOPS~126 TOPS combined

TOTAL RAM32 GB across 3 nodes

TOTAL STORAGE~1.1 TB (SSD + NVMe + flash)

COMPUTE NODES3 active · all P2P servers

THIN CLIENTS1 · Galaxy Tab S9 FE+

REPOS ON THIS STACK

horizons-uic10vis-poem/Horizons-UI

novus-agentic10vis-poem/novus-agenti

aesop protocolc10vis-poem/aesop

nova-skillsc10vis-poem/nova-skills

home-node/Jetson + DragonWing · configs

termux-env/Termux scripts · CLI

node-gamma-rubik-pidevice node (name confirmed)

BUILD ROADMAP (IN ORDER)

DESIGN CONSTRAINT: NEVER HARDCODE INFERENCE BACKEND

1

Home node running on all cylinders CURRENT PHASE

NODE_BETA + NODE_GAMMA configured · Tailscale mesh stable · voice layer closed (Moonshine in-process) · Termux backend listener built · runtime params first-class

2

AEC application — communications + safety layer DESIGNED

Communications workflow · software bridging · safety layer protocol. Target: prototype in 6–8 months

3

ARM64 + commercial GPU DESIGNED

Modular TBD form factor — PCIe attach or external enclosure. GOAL: home node replaces the laptop. Operator's own custom design.

4

Broader modular hardware ecosystem PRIVATE

Metamaterials designs · novel thermal management systems. At least 2 potentially patentable designs. ⚠ NOT documented in any public or shared repo until filed.

BUILD LEDGER · DEVICE STACK

RULE 6 · DESIGNED ≠ BUILT

[ALPHA] built-verified Razr Ultra hardware + Horizons UI APK

[ALPHA] built-verified Sherpa-ONNX Kokoro TTS in-process

[ALPHA] built-verified Tailscale node — mesh enrolled

[ALPHA] built-unverified Moonshine STT in-process on AAR (CI green · not device-tested)

[ALPHA] built-unverified NPU HTP pathway (QAIRT/HTP chain · bare metal only)

[ALPHA] absent Termux inbound listener (mic/voice/OAuth)

[ALPHA] absent runtime params first-class (temperature/verbosity/cores)

[BETA ] built-verified Jetson Orin Nano Super hardware + DDR4 SSD

[BETA ] built-unverified Tailscale enrollment · mesh connectivity to ALPHA

[BETA ] absent peer-agent deployment

[BETA ] absent utilities-agent deployment

[BETA ] absent AVNC server config (for Tab access)

[GAMMA] built-verified Rubik Pi 3 hardware · DragonWing SoC

[GAMMA] built-unverified high-speed data cable to BETA

[GAMMA] absent visual OS fully configured · dual monitor active

[NET ] built-verified Tailscale overlay — all three nodes enrolled

[NET ] absent full mesh routing verified (all paths tested)
