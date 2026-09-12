# NeuroOmni / Horizons UI — Antigravity CLI Build Pack

**Target:** Razr Ultra (Snapdragon 8 Elite) · Native Kotlin + Jetpack Compose
**Agent:** Antigravity CLI (`agy`) in Google Cloud Shell
**Build/APK:** GitHub Actions (NOT Cloud Shell)
**Principle:** Each session ends at a committed, pushed, CI-green checkpoint that produces an installable APK. Never leave a wall half-framed.

---

## Why the workflow is split this way

| Job | Where | Why |
|---|---|---|
| Write code, commit, push | `agy` in Cloud Shell | Source tree is tiny (KB–MB). Fits the 5 GB cap with room to spare. |
| Compile + assemble APK | GitHub Actions | Runner has the Android SDK preinstalled + 14 GB disk. Free: unlimited mins on public repo, 2,000/mo private. |
| Verify | CI build log | Agent does NOT run `gradlew` locally. CI is the source of truth. Keeps Cloud Shell light and avoids the 5 GB wall. |
| Install | Download APK artifact to Razr | Debug APK is directly installable. |

**Rule for the agent, every session:** do not install the Android SDK or run a local Gradle build. Write code, commit, push, read the CI result, fix if red.

---

## Corrections baked in (vs the Gemini plan)

1. **VoxSherpa package name.** Gemini used `CodeBySonu95.VoxSherpa` (the dev's GitHub handle). The real Android applicationId is **`com.CodeBySonu.VoxSherpa`**. Wrong name = silent bind failure.
2. **TTS binding method.** VoxSherpa registers as a *system* TTS engine. Bind it with the standard `TextToSpeech(context, listener, "com.CodeBySonu.VoxSherpa")` 3-arg constructor — not a custom intent. Engine package is configurable so you can fall back to system default.
3. **Edge model is a swappable slot, not hardcoded.** OmniNeural-4B is CC BY-NC 4.0 (non-commercial). Fine for your personal build now; a problem only when you ship a sold unit (months out). So the model sits behind an `EdgeModel` interface. Swap the implementation later without touching the app.
4. **The build stage exists.** Gemini assumed the APK appears. It doesn't. The GitHub Actions workflow below is the missing piece.
5. **Auth nit.** Skip the `GOOGLE_API_KEY` export unless your agent specifically needs AI Studio. `agy` authenticates via your Google account OAuth.

---

## SESSION 0 — Prerequisites (you, by hand, ~10 min)

Do these manually. The agent can't click OAuth consent screens or create accounts.

1. **Blank GitHub repo.** Create a new repo named `NeuroOmni`. Do **not** add a README, .gitignore, or license — leave it completely empty. Copy the HTTPS URL.
2. **NEXA_TOKEN.** Free signup at nexa.ai → copy your token. You'll only need it on-device, not in CI.
3. **GCP Project ID.** Note your actual project ID (e.g. `neuro-omni-123456`), not the display name.

Then in Cloud Shell:

```bash
# Set your project
gcloud config set project YOUR_PROJECT_ID

# OAuth login — click the link it prints, sign in, paste the code back
gcloud auth application-default login
```

Install the Antigravity CLI:

```bash
# Installs the `agy` binary into ~/.local/bin
curl -fsSL https://antigravity.google/install.sh | bash   # confirm exact URL from docs at install time
export PATH="$HOME/.local/bin:$PATH"
agy --version
```

> If the install URL differs, grab the current one-liner from the Antigravity CLI docs. The binary is named `agy`, drops in `~/.local/bin`, and is SSH-aware so it'll hand you an auth URL to open in your phone browser.

**Checkpoint 0:** `agy --version` prints, `gcloud` is authed, blank repo exists.

---

## SESSION 1 — Scaffold + prove the pipeline

Goal: empty Compose app that CI can build into an APK. Prove the pipe before writing real code.

Launch `agy` in an empty working dir, then paste these one at a time. Wait for each to finish.

**Prompt 1.1 — Context injection (read-only, no code yet)**

> Read the attached files `N0_V4_ARCHITECTURE_v3.md` and `HORIZONS_UI_SPEC_v3.md`. I'm building a native Android app in Kotlin + Jetpack Compose targeting a Snapdragon 8 Elite device (NOT a web app or PWA). Act as my senior Android architect. Reply ONLY with: (a) the 4 primary UI panels, (b) the 3 execution layers, (c) confirmation you understand the target platform. Do not write code yet.

**Prompt 1.2 — Scaffold + push**

> Create a native Android Kotlin project named `NeuroOmni` with an empty Jetpack Compose activity. Set minSdk to 27 and targetSdk to current. Add dependencies for Jetpack Compose, OkHttp, and Android's TextToSpeech (framework, no extra dep). Initialize git, add a standard Android `.gitignore`, commit, and push to `https://github.com/<you>/NeuroOmni.git`. Do NOT run a local Gradle build — we build in CI. Do NOT install the Android SDK locally.

**Prompt 1.3 — CI workflow (the missing piece)**

> Create `.github/workflows/build.yml` that builds a debug APK on every push and uploads it as an artifact. Use the workflow below verbatim, then commit and push it.
>
> ```yaml
> name: Build APK
> on:
>   push:
>     branches: [ "**" ]
>   workflow_dispatch:
> jobs:
>   build:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>       - uses: actions/setup-java@v4
>         with:
>           distribution: temurin
>           java-version: '17'
>       - name: Grant gradlew permission
>         run: chmod +x ./gradlew
>       - name: Build debug APK
>         run: ./gradlew assembleDebug --no-daemon
>       - name: Upload APK
>         uses: actions/upload-artifact@v4
>         with:
>           name: NeuroOmni-debug-apk
>           path: app/build/outputs/apk/debug/*.apk
> ```

**Checkpoint 1:** Push triggers the Action. Action goes green. Download `NeuroOmni-debug-apk` from the run, sideload it to the Razr, confirm the empty app launches.
*(If the build is red, paste the CI log into `agy` and have it fix — that's the loop for every session.)*

---

## SESSION 2 — Horizons UI shell

**Prompt 2.1**

> Modify `MainActivity.kt` to build the Horizons UI v3.0 layout: four panels — Chat, Router, Terminal, Diagnostics. Implement a dark theme. Add a state variable `instanceProfile` with values Personal, RedAgent, Collab. Panels can be simple column/row placeholders, EXCEPT the Chat panel which needs: a text input field, a scrolling message list, and a toggle switch for the active provider. Commit and push. Do not run a local build.

**Checkpoint 2:** CI green. APK installs. Four panels render, dark theme, chat input + provider toggle present.

---

## SESSION 3 — Edge model slot (swappable, NOT hardcoded)

This is the license-proofing. The app talks to an interface; the OmniNeural implementation is just one plug.

**Prompt 3.1 — Define the interface + a CI-safe stub**

> Create an `EdgeModel` Kotlin interface with: `suspend fun initialize(): Result<Unit>`, `fun generateStream(prompt: String): Flow<String>`, `fun release()`. Create a `StubEdgeModel` implementation that returns a canned streamed response (so CI and emulators run with no model file and no token). Wire the Chat panel to call the currently-selected EdgeModel and stream tokens into the message list. Default to StubEdgeModel. Commit and push.

**Prompt 3.2 — Real implementation behind the interface**

> Add a `NexaOmniNeuralEdgeModel` implementing `EdgeModel`, using the Nexa Android SDK. Read the NEXA_TOKEN from `local.properties` exposed via BuildConfig — never hardcode it in source, never commit it. Initialize with `NexaSdk.getInstance().init(context)`, then build a VLM with `model_name = "omni-neural"`, the model path under the app's files dir, and `plugin_id = "npu"`. Implement `generateStream` over `generateStreamFlow(...)`. Add a build flag or runtime check that falls back to StubEdgeModel when the token or model file is absent, so CI stays green. Commit and push.

> Add `local.properties` and `*.nexa` model files to `.gitignore`. Add `NEXA_TOKEN=` to `local.properties` locally only.

**Checkpoint 3:** CI green using StubEdgeModel (no token needed in CI). On the Razr with token + model present, chat streams from OmniNeural on the NPU. Swapping models later = one new `EdgeModel` class, zero UI changes.

---

## SESSION 4 — Voice out (VoxSherpa TTS, corrected)

**Prompt 4.1**

> Create a `LocalVoiceEngine` class. Use Android's native `TextToSpeech` 3-arg constructor to bind a specific engine package, defaulting to `"com.CodeBySonu.VoxSherpa"` but make the package name a configurable constructor parameter so it can fall back to the system default engine. In the onInit callback set language to US English. Add `fun speak(agentOutputText: String)` that queues with `QUEUE_ADD` and a unique utterance id. Note in a code comment that Kokoro-82M synthesis latency on-device can be high; expose speed/pitch as parameters. Wire a "speak" button in the Chat panel to `speak(...)` the latest agent message. Commit and push.

**Checkpoint 4:** CI green. On the Razr (with VoxSherpa installed), the speak button produces audio. If VoxSherpa isn't installed, it falls back to system TTS instead of failing silently.

---

## SESSION 5+ — Execution layers

The 3 execution layers (API / Shell / Browser-automation) come next, one per session, same checkpoint discipline. Pick the order based on what you want working first — that's the next decision, not part of this pack.

---

## Running milestones in parallel (your "5 agents" instinct)

Do Sessions 0 → 1 → 2 strictly in order — they're the foundation and everything depends on the scaffold + green pipeline. After that, Sessions 3 (edge model) and 4 (voice) are independent and can run as **async subagents** in parallel (`agy` supports background subagents that return diffs). Merge each only after its own CI run is green. Don't parallelize before Checkpoint 2 — you'll get merge chaos on a foundation that isn't proven yet.

---

## The session checklist (tape this to the wall)

Every session, before you close it:

1. Code committed.
2. Pushed to GitHub.
3. CI run is **green**.
4. APK artifact downloaded and the new thing confirmed on the Razr.
5. If red: paste the CI log into `agy`, fix, repeat — do not start the next milestone on a red build.

That's your export/upload endpoint. Nothing is ever lost mid-wall.
