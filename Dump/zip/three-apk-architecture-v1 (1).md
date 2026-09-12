---
source: Three-APK Architecture (v1).pdf
cleaned: 2026-08-26
converter: pymupdf get_text()
source_pages: 3
---
NOVÆ-CORPUS / PRESENTATION LAYER — 2026-08-14
One UI, two daemons it
can't function without
Not three independent apps sharing a repo pattern. One orchestrator
front end, and two bare-metal daemon services — not headless, each
carries its own low-graphics 1-2 tile UI — it depends on to reach the
device beyond Android's sandbox.
PRESENTATION
Horizons UI
repo: horizons-ui · branding: Horizons UI™ — "the ever-expanding canopy"
The orchestrator app — the only one of the three a user actually touches directly.
TRANSPORT
WebSocket layer connecting to the two daemons and whatever backend the
model router selects.
BROWSER
Embedded Chromium WebView, hosting the UI surface itself.
CHAT
LLM chat tile interface.
TERMINAL
Terminal GUI, surfacing the shell daemon's access.
ROUTING
Model router with file picker / uploader, cloud front-end hooks, and a fallback to
an OpenRouter server if the primary path fails.
AGENT
Houses the nano/smol-agent (model not yet chosen) running the dual
query/execute tandem against the device NPU and runtime.
Flagged, not resolved: Horizons UI's own model router (with OpenRouter fallback) is a separate
routing layer from OmniRoute. Worth deciding whether this router calls OmniRoute or duplicates its
job before all three APKs exist — cheaper to settle now than after.

Horizons UI is not self-sufficient — but it isn't device-blind either. As a standard Android APK it already
holds normal app-level access (file picker/uploader, storage, network/WebSocket) — that's baseline, not
something it borrows. What it doesn't hold is the elevated tier: Accessibility Service / Device Assistant
class privileges that bypass the app sandbox entirely. That specific escalation — sandbox-level shell
access and NPU/hardware execution — is what routes through the two daemons below.
DAEMON 1
Shell Access
repo: not yet named in official signage
Not a Termux replacement — Termux itself, elevated. It keeps its built-in terminal/emulator; what
changes is the privilege tier it runs at, so it stops being treated as a sandboxed app.
MECHANISM
Registers as an Accessibility Service / on-device assistant, escalated with Device
Assistant and Media Server privileges — the combination that grants shell-level
access outside the normal app sandbox.
NPU GUARD
Houses the small "housekeeper" model (nano/smol/TurboQuant-class) that acts
as a traffic cop over the Hexagon NPU, queuing tool calls so the executive model
and tooling models don't collide on the same tensor registers.
MEMORY ROUTING
Sits in front of the memory pipeline the user described directly this session:
OmniRoute (SQL/routing) → Reasoning Bank (RLVR trajectories) → OB1 →
Mem0, front to back.
GUI
Bare-metal, low-graphics — one or two tiles. Not headless: built for local
configuration and portability.
CONSUMER
Horizons UI's terminal GUI is the front end for this daemon's access.
DAEMON 2
Speech & Vision
repo: not yet named in official signage
Fronts the device agent's speech and vision layer — same permission class as the shell daemon.
MECHANISM
Same accessibility-service / OS-level permission class as Daemon 1.
f
f
(
f
f
)

captured from session · reference material, not a build-out session on its own
