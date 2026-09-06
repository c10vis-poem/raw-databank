# Horizons salvage — three destinations

Parts stripped off `c10vis-poem/horizons-ui` before that repo gets torched.

**Source:** `c10vis-poem/horizons-ui` @ `2c647964efe1375a12c14179e7c04ef2ed13350a`
**Pulled:** 2026-09-06

This is a salvage yard. Nothing here is canonical or finished. Sorted by **where
each piece is going**, not by where it came from.

| Folder | Destination |
|---|---|
| `Aesc-Terminal-APK/` | The daemon APK — NPU manager, UNIX-socket terminal access, small on-device assistant, maybe MCP server, maybe model loading. Has its own UI (terminal, chat, settings, about/build). |
| `Horizons-UI/` | The product UI, rebuilt from scratch in Flutter or Genie app builder + Jetpack Compose + Material 3. |
| `Skills-Tools-Assets/` | Skills, agent definitions, rules, the knowledge corpus, compile tooling. Framework- and app-independent. |

---

## The NPU runtime is NOT here — deliberately

`RuntimeDefStore`, `RouterConfigStore`, `CliffordService`, `NpuClient`,
`DaemonLauncher`, `NativeBinaryInstaller`, and the whole C++ `daemon/` directory
were **all dropped**. That layer gets built from the ground up.

Keeping the post-mortem, not the code, because the failure is worth not
repeating:

**What went wrong:** the GenieX migration was half finished. `RuntimeDefStore`
had the right abstraction — runtimes as user-definable records with name, binary,
port, health path. GenieX was registered there on `:18181`, and three UI surfaces
displayed it. But `CliffordService` / `DaemonLauncher` / `NativeBinaryInstaller`
never learned that abstraction existed. They stayed hardcoded to
`ENGINE_BINARY = "ort_engine"` on port `8080` — the architecture the project had
already decided against. **The app could describe GenieX in three places and had
no code path able to start it.**

Meanwhile `assets/` never contained an engine binary at all. CI built
`ort_engine` and shipped it as a loose release artifact expecting a manual
`adb push` to `/data/local/tmp/`, while the installer looked inside the APK's own
assets. Two different places, never wired together.

**Why nobody noticed for months:** every failure path swallowed its exception.

| Call | Swallowed as |
|---|---|
| `extractAsset` | `catch { false }` — missing binary looked identical to a failed copy |
| `applyOomImmunity` | `catch {}` — used `su -c`, so on a non-rooted phone it failed *every single time*, silently |
| `daemonHealthCode` | `catch { -1 }` — network error and "not running" collapsed into one value |
| `acquireNpuPerfLock` | caught, logged at `debug` — invisible in release builds |

Add a watchdog explicitly tuned never to crash-loop, and the result is a system
excellent at not thrashing and structurally incapable of reporting that nothing
ever started. The thing built to protect it is what made the failure invisible.

**Rule for the rebuild: a failed precondition is loud and terminal.**
`BinaryMissing` should have crashed a debug build on first launch, not been a
steady state the app lived in for months.

Two more tripwires from that code, worth knowing even though it's gone:

- Liveness was `pidof <binaryName>` — the *only* liveness signal in the system.
  `/proc/<pid>/comm` truncates at 15 chars. `ort_engine` is 10, so it worked by
  luck. Any binary name ≥16 chars would have silently never matched, and the
  watchdog would have concluded "dead forever."
- The claim that `sh -T-` reparenting preserves FGS-level `oom_score_adj` was
  **stated as fact and never measured.** It's also what made the daemon invisible
  to the app that spawned it.

---

## Also not salvaged

| Dropped | Why |
|---|---|
| `daemon/` (C++ `ort_engine`, 8 files + CMake + CI step) | Old architecture. Also has an open bug: `http_server.cpp` truncates payloads >8 KB — single `recv()` into a fixed buffer instead of reading to `Content-Length`. |
| `su -c` / root paths | Dead on a non-rooted device. |
| Port `8080` / `ort_engine` constants | Docs said GenieX on 18181, code said 8080. Don't port the disagreement. |
| The file tree / panel decomposition / navigation structure | Way-station. Not the final structure. |
| `release/debug.keystore` | **Left in the old repo on purpose.** Signing material doesn't belong in a salvage dump. Grab it directly if you actually need consistent debug signing. |

---

## Overlap to resolve before building

`Aesc-Terminal-APK/audio/` (AudioRecorder, Silero + RMS VAD, VadFactory,
VoiceLoopController) **overlaps Æyre**, which owns voice and vision. Decide which
APK owns audio before either starts, or it gets maintained twice.

---

## Unverified

Nothing here was built or run — no emulator, no device. Critical paths were read
in full; the ~6,900 lines of Compose were surveyed, not read line by line.

---

## Vendor docs — already carried over, not duplicated here

`knowledge/qairt-sdk/` (9 files: api, backend, context, graph, htp, tensor,
overview + htp.jsonl), `knowledge/fragmented-qat/` (FraQAT paper + jsonl),
`knowledge/google-dev-docs/` and `knowledge/research-npu/` were **removed from
this dump** — they already live in the vendor workspaces. Grab them there, not
from here.

What's left under `Skills-Tools-Assets/knowledge/` is the project-specific
material only: Omni Claw architecture and blueprint, the workbench design
conversations, device inventory, daemon reference, the Gemini query transcripts
on Qwen 3.5 9B compilation/quantization, prompt-caching notes, and the proofs.
