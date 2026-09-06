# Horizons-UI Salvage

Parts pulled off `c10vis-poem/horizons-ui` before that repo gets torched.

**Source commit:** `2c647964efe1375a12c14179e7c04ef2ed13350a`
**Pulled:** 2026-09-06
**Nature of this folder:** salvage yard. Nothing here is canonical, nothing here
is finished, and nothing here should be trusted as current architecture. It's
parts on a bench.

---

## Read this first — what Horizons actually becomes

Two different things come out of this, and they are **not** the same app.

### 1. The daemon APK — has its own UI, is not headless

What the old APK turns into:

- NPU manager daemon / backend
- UNIX-socket terminal access (replacing the old ADB debug loopback)
- A small on-device assistant
- Possibly the MCP server itself
- Possibly model loading

**And its own front end:** a terminal UI, a chat interface, settings, and an
about/build page. Not fully specced yet. So this APK is a real app with a real
UI — just a utilitarian one, scoped to running and inspecting the daemon.

### 2. The Horizons UI — rebuilt from scratch, separately

The designed product UI. Flutter, or Genie app builder with Jetpack Compose +
Material 3 (every tile Material 3 once opened). The old structure is **not** the
final structure and doesn't carry over.

**Consequence for this folder:** the Compose in `04-ui-reference/` splits two
ways. `TerminalPanel`, `ChatPane` and `SettingsPane` map onto the daemon APK's
own UI and are directly useful there. `HomeGrid`, the tile system, and the
visual identity belong to the separate Horizons rebuild, which starts from
`01-design/` rather than from that code.

This folder is sorted by **where each piece is going**, not by where it came from.

---

## Layout

| Folder | What | Survives into |
|---|---|---|
| `01-design/` | `HOME-REDESIGN-SPEC.md`, 24 reference images, 2 device screenshots | **The UI rebuild** — framework-agnostic. Works whether the target is Flutter or Compose. |
| `02-specs/` | Router/Monitor/Terminal spec, feature spec, GenieX daemon plan, failure ledger | **The reasoning.** Keep the thinking, drop the implementation. |
| `03-backend-source/` | Kotlin that maps onto the daemon APK | **The backend.** See breakdown below. |
| `04-ui-reference/` | The Compose UI, ~6,900 lines | **Splits two ways.** `TerminalPanel` (1,079), `ChatPane` (610), `SettingsPane` (832) map onto the daemon APK's own UI — directly useful. `HomeGrid` (1,394), `PaneBackgrounds`, `Screensaver`, `HorizonsTheme` and the tile system belong to the separate Horizons rebuild, which starts from `01-design/` rather than this code. Already on Material 3 (`androidx.compose.material3`), so tokens and component choices port to a Compose target; only the spec and images port to Flutter. |
| `05-provenance/` | Source commit SHA | — |

### `03-backend-source/` breakdown

| Sub | Files | Why it's worth keeping |
|---|---|---|
| `assistant/` | 4 `assist/` services + accessibility service | Android assistant-role and accessibility integration is fiddly, badly documented, and easy to get wrong. This is done and working. Highest value per line in the whole repo. |
| `agent/` | `AgentLoop`, `AgentTool`, `AgentToolParser`, `AgentSystemPrompt` + 9 tools (Alarm, App, Calendar, Clipboard, Contacts, Device, Media, Notification, SystemInfo) | The 9 tools are real, self-contained Android integrations. Rewriting them buys nothing. This is the "small on-device assistant." |
| `npu-runtime/` | `RuntimeDefStore`, `RouterConfigStore`, `CliffordService`, `NpuClient` | The NPU manager. **See the warning below — take the ideas, not the wiring.** |
| `permissions/` | `AndroidManifest.xml`, accessibility + voice-interaction configs | The full-stack permission surface, already declared: assistant, accessibility, foreground-service types, media projection, microphone. Worth having as a reference sheet. |
| `audio/` | `AudioRecorder`, `RmsVadDetector`, `SileroVadDetector`, `VadFactory`, `VoiceLoopController` | **Overlaps Æyre.** Decide which APK owns audio before using this, or it gets maintained twice. |
| `diag/` | `FailureMonitor`, `Breadcrumb`, `CrashRecorder`, `FileTail` | Working adb-pullable failure-report pipeline. Better than what it was diagnosing. |
| `perf/` | `GameModeBoost`, `PerfHintSession` | The Android performance-hint / Game Mode path. Small, done. |

---

## Warning on `npu-runtime/` — read before reusing

These four files contain both the best idea in the repo and the bug that killed
it.

**The good idea:** `RuntimeDefStore` is a proper abstraction — runtimes are
user-definable records carrying `name`, `binaryName`, `port`, and health-endpoint
notes. GenieX is registered there on `:18181`. The Router "fuse" rule is also
good: nothing auto-launches until the user explicitly engages a runtime.

**The bug:** `CliffordService` (and the `DaemonLauncher` / `NativeBinaryInstaller`
that are deliberately **not** in this folder) never learned that
`RuntimeDefStore` exists. They stayed hardcoded to `ENGINE_BINARY = "ort_engine"`
on port `8080` — an architecture the project had already decided against. The app
could describe GenieX in three UI surfaces and had no code path able to start it.

**So:** `CliffordService` is here for its *state machine only* — the backoff, the
strike cap, the re-arm-on-model-change, and the rule that a live process is never
relaunched. Its launch mechanism is dead. The new orchestrator supervises
**whatever the RuntimeDef names**. That missing join is the entire bug and it's a
small thing to build.

---

## Deliberately NOT salvaged

| Dropped | Why |
|---|---|
| `daemon/` (C++ `ort_engine`, 8 files + CMake + CI step) | Old architecture. The project decided on GenieX; this is what it decided against. Also has an open bug: `http_server.cpp` truncates payloads >8 KB (single `recv()` into a fixed buffer instead of reading to `Content-Length`). Do not port, do not fix, do not build. |
| `DaemonLauncher`, `NativeBinaryInstaller` | Exist only to install and launch `ort_engine`. Neither knows `RuntimeDefStore` exists. |
| `su -c` / root paths | Dead on a non-rooted device. `applyOomImmunity` failed silently on every call. |
| Port `8080` / `ort_engine` constants | The README says GenieX on `18181`; the code said 8080. Don't port the disagreement. |
| The `sh -T-` detach + oom-inheritance theory | Stated as fact, never measured. It's also why the daemon was invisible to the app that spawned it. |
| The file tree / panel decomposition / navigation structure | Way-station. Not the final structure. |

---

## The lesson worth carrying

Every failure in the old build was **silent by construction**:

- `extractAsset` → `catch { false }` — a missing binary looked identical to a failed copy
- `applyOomImmunity` → `catch {}` — no root, every call failed, nothing said so
- `daemonHealthCode` → `catch { -1 }` — network error and "not running" collapsed to one value
- `acquireNpuPerfLock` → caught, logged at `debug` (invisible in release)

Combine that with a watchdog explicitly tuned never to crash-loop, and you get a
system excellent at not thrashing and incapable of reporting that nothing ever
started. The thing built to protect it is what made the failure invisible.

**In the new build, a failed precondition should be loud and terminal.**
`BinaryMissing` should have crashed a debug build on first launch — not been a
steady state the app lived in for months.

---

## Unverified

Nothing here was built or run. No emulator, no device. The critical paths
(`CliffordService`, `DaemonLauncher`, `NativeBinaryInstaller`, manifest, CI) were
read in full; the ~6,900 lines of Compose in `04-ui-reference/` were surveyed,
not read line by line.
