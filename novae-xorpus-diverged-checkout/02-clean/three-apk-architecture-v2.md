---
source: Three-APK Architecture (v2).pdf
cleaned: 2026-08-26
converter: pymupdf get_text()
source_pages: 4
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

VOICE STACK,
NAMED DIRECTLY
IN THE SOURCE
Silero VAD for mic-gating, a forked WhisperKit (MIT-licensed, safe to fork) or a
QNN-compiled whisper.cpp path for ASR, sherpa-onnx running Kokoro for local
TTS — fully offline.
GUI
Same bare-metal, low-graphics, one-to-two-tile treatment as Daemon 1 — for
local config and portability, not headless.
OPEN QUESTION, NOT YET RESOLVED
Whether the permission surface here is an SDK or an API — flagged during the original architecture
discussion, not settled either way.
terminal GUI
speech/vision front end
nano/smol-
agentquery/execute
shell access,no sandbox
Horizons UI(Presentation)
Daemon 1 · Shell 
Access(Accessibility 
Service)
Daemon 2 · Speech & 
Vision(Accessibility 
Service)
Device NPU + runtime
Horizons UI holds standard app-level device access on its own — the elevated, sandbox-bypassing tier
(shell, NPU/hardware execution) routes through one of the two daemons
Signage note, corrected: only horizons-ui has confirmed official branding from NovÆgenti Defined
(pt.1) — but the source document is not silent on daemon names, it's unreliable on them. Two different
naming attempts appear in it, neither ever confirmed: an earlier pass proposed NovusÆxenti Engine +
Æsop-Xi Vocal Daemon for the App 2 / App 3 split; a later pass proposed Æsc (root/shell) + Æyræ
(storm/execution) under an invented "Terminix 2.0" brand — which the document itself later reveals was built
on a voice-to-text mishearing of "Termux," never on anything the user actually said. The user rejected that entire
thread directly in the source ("you lost all fucking context of the entire goddamn conversation"), and the
document ends before any daemon name is re-established. This artifact uses functional labels (Shell Access,
Speech & Vision) for that reason — not because the source is silent, but because what it does say on this point
isn't trustworthy. Flagged per standing rule rather than silently dropped.

captured from session · reference material, not a build-out session on its own
