# Manifest — Horizons salvage

**Source:** `c10vis-poem/horizons-ui` @ `2c647964efe1375a12c14179e7c04ef2ed13350a`
**Date:** 2026-09-06
**Source repo size:** 222 files · 75 Kotlin · 9 C++/headers · ~9 MB

| | Count |
|---|---|
| Files salvaged | **148** |
| Kotlin salvaged | **53 / 75** |
| Kotlin left to die | **22** |
| Folders created | 4 |

---

## 1. SURVIVED — pulled into `raw-databank`

### `Aesc-Terminal-APK/` — 38 files

The daemon APK. Not headless: gets its own terminal UI, chat interface, settings,
about/build page.

| Sub | Files | What |
|---|---|---|
| `assistant/` | 5 | `HorizonsVoiceInteractionService`, `…Session`, `…SessionService`, `HorizonsRecognitionService`, `HorizonsAccessibilityService` |
| `agent/` | 14 | `AgentLoop`, `AgentTool`, `AgentToolParser`, `AgentSystemPrompt`, `AgentNotificationListener` + 9 tools: Alarm, App, Calendar, Clipboard, Contacts, Device, Media, Notification, SystemInfo |
| `ui-panels/` | 3 | `TerminalPanel` (1,079 ln), `ChatPane` (610), `SettingsPane` (832) |
| `diag/` | 6 | `FailureMonitor`, `Breadcrumb`, `FileTail`, `CrashRecorder`, `InteractionLogger` |
| `permissions/` | 3 | `AndroidManifest.xml`, `accessibility_service_config.xml`, `voice_interaction_service.xml` |
| `perf/` | 2 | `GameModeBoost`, `PerfHintSession` |
| `tiles/` | 1 | `TerminalTile` |
| `specs/` | 5 | Router/Monitor/Terminal spec, GenieX daemon plan, FAILURES ledger, GPT daemon reference, NPU runtime paths |

### `Aeyre-Media-APK/` — 18 files

Voice and vision. Everything Android-media, moved out of Æsc.

| Sub | Files | What |
|---|---|---|
| `audio/` | 6 | `AudioRecorder`, `VoiceLoopController`, `SileroVadDetector`, `RmsVadDetector`, `VadDetector`, `VadFactory` |
| `tts/` | 4 | `HorizonsTtsService`, `KokoroModelManager`, `SherpaOnnxTtsClient`, `DaemonTtsClient` |
| `stt/` | 3 | `SttEngine`, `MoonshineSttEngine`, `DaemonSttClient` |
| `screen/` | 2 | `ScreenshotCapture`, `ScreenShareService` |
| `specs/` | 2 | `tts_engine.xml`, `ime_method.xml` |

### `Horizons-UI/` — 50 files

The product UI, rebuilt from scratch. Design survives; structure does not.

| Sub | Files | What |
|---|---|---|
| `design/` | 31 | `HOME-REDESIGN-SPEC.md`, 24 reference images, 2 device screenshots, `FEATURE-SPEC.md`, tile-hub architecture, fusebox conversation + its contradiction warning |
| `ui-reference/` | 8 | `HomeGrid` (1,394 ln), `PaneBackgrounds`, `Screensaver`, `HorizonsTheme`, `HorizonsPane`, `ArtifactsPane`, `MonitorPane`, `RouterPane` — **reference, not cargo** |
| `brand/` | 11 | Orbitron + Google Sans Code `.ttf` with OFL licenses, 5 drawable XMLs, `colors.xml`, `themes.xml` |

### `Skills-Tools-Assets/` — 42 files

Framework- and app-independent.

| Sub | Files | What |
|---|---|---|
| `skills/` | 3 | `project-memory`, `horizons-wiki`, `termux-mobile-dev` |
| `agent-defs/` | 4 | `omni-claws-master.agent.yaml`, `sub-agent.agent.yaml`, `sub-agent.system.md`, `build-runner.yaml` |
| `rules/` | 4 | `AT_BAT_PROTOCOL`, `GIT_HYGIENE`, `AAR_DECOMPILE`, README |
| `knowledge/` | 24 | Omni Claw blueprint + synthesis, workbench conversations, device inventory, daemon reference, Gemini query transcripts (Qwen 3.5 9B compile/quant), prompt-caching notes, proofs |
| `compile/` | 3 | **`compile_qwen3_5_9b.py` (33 KB)**, `manifest.yaml`, requirements |
| `claude-config/` | 3 | settings + session hooks |
| root | 1 | `failures.sh` |

---

## 2. CREATED — did not exist before

| File | Purpose |
|---|---|
| `README-SALVAGE.md` | Top-level index. Carries the **NPU post-mortem** — the half-finished GenieX migration, the CI/installer path mismatch, the four swallowed exceptions. |
| `MANIFEST.md` | This file. |
| `Aeyre-Media-APK/README.md` | The 10s Moonshine ceiling, the two-part proot audio fix, the unverified mic loop, rewrite-not-port. |
| `Horizons-UI/design/WARNING-fusebox-file-contradicts-itself.md` | Flags that the operator's rejection is buried under a formal block reinstating what he rejected. Plus the adopted/candidate/superseded/transcript labels. |

Folder structure itself is new — the source repo had no such organization.

---

## 3. SET FOR ANNIHILATION — dies with `horizons-ui`

### The NPU runtime layer — deliberate, gets rebuilt from the ground up

```
fgs/CliffordService.kt          the watchdog
fgs/CliffordBootReceiver.kt
core/shell/DaemonLauncher.kt    pidof-based liveness, sh -T- detach, su -c
core/shell/NativeBinaryInstaller.kt
core/llm/NpuClient.kt
core/llm/LlmRuntime.kt
core/llm/CloudLlmRuntime.kt
core/state/RuntimeDefStore.kt   the right abstraction, wrong wiring
core/state/RouterConfigStore.kt
daemon/                         11 files — C++ ort_engine + CMake
```

### App shell — structure is a way-station, not final

```
HorizonsApplication.kt
MainActivity.kt
ModelImportActivity.kt
provider/SettingsStore.kt
core/state/AppStateStore.kt · ArchiveStore.kt · ChatHistoryStore.kt · SavedCommandStore.kt
fgs/LiveChatService.kt
ui/browser/BrowserPane.kt
core/shell/ManualStore.kt · SecureResourceRelay.kt · TaskerBridge.kt
```

### Build + infra

```
.github/workflows/  3 files — build-apk (builds ort_engine), failure-monitor, disabled colab
gradle/ · build.gradle.kts · settings.gradle.kts · gradle.properties
release/debug.keystore   left deliberately — signing material doesn't belong in a dump
EXECUTIONS.md · CLAUDE.md · README.md · sub-agent.agent.yaml (root copy)
wiki/  BUILD-ACTION-PLAN, BUILD-STATUS, COMPILE-PIPELINE, JOB_EXECUTION_LOG,
       MASTER-SESSION, originals/, research/
```

### Vendor docs — removed as duplicates, already carried over

```
knowledge/qairt-sdk/          9 files
knowledge/fragmented-qat/     FraQAT paper + jsonl
knowledge/google-dev-docs/
knowledge/research-npu/
```

---

## 4. Grab before you torch it

| Item | Why |
|---|---|
| `release/debug.keystore` | Not salvaged on purpose. If you want consistent debug signing across the rebuilds, pull it directly — it's gone after. |
| `wiki/originals/`, `wiki/research/` | Not enumerated in this pass. Unknown contents. Worth 60 seconds before deletion. |
| Git history | 22 Kotlin files die with the repo. History is the only record they existed. If any turn out to be needed, they're unrecoverable after. |

---

## 5. Unverified — stated plainly

- Nothing here was built or run. No emulator, no device.
- Critical paths read in full: `CliffordService`, `DaemonLauncher`,
  `NativeBinaryInstaller`, `AndroidManifest.xml`, `build-apk.yml`,
  `project-memory/SKILL.md`, `omni-claws-master.agent.yaml`.
- The ~6,900 lines of Compose were surveyed by size and name, **not read line by
  line.** If something load-bearing hides in `ArtifactsPane` or `MonitorPane`, I
  would not have caught it.
- `wiki/originals/` and `wiki/research/` were never opened.
- Counts in this manifest come from `find` against the working tree, not from
  reading each file.
