# AESOP Full Reference Guide
### Android Edge-Pi System Operations Platform
*Voice AI · Edge Inference · Claude API · Multi-Device Stack*

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [File Directory](#2-file-directory)
3. [First-Time Setup](#3-first-time-setup)
4. [Launching AESOP](#4-launching-aesop)
5. [Device Profiles](#5-device-profiles)
6. [Module Reference](#6-module-reference)
7. [Edge Model Guide](#7-edge-model-guide)
8. [Voice Commands](#8-voice-commands)
9. [Editing Artifacts & Skills](#9-editing-artifacts--skills)
10. [Troubleshooting](#10-troubleshooting)
11. [Script File Log](#11-script-file-log)

---

## 1. Project Overview

AESOP runs as a voice-first AI assistant inside a Ubuntu container on your Android device. You speak → AESOP transcribes → builds a structured prompt → routes to Claude API → speaks the response. On the Razr Ultra, intent parsing runs locally on the Hexagon NPU before hitting the cloud.

```
[You speak]
     ↓
Voice Interface (VAD → STT)
     ↓
Meta-Prompt Engine (intent classify → structure)
     ↓             ↘ OmniNeural NPU (Razr Ultra only)
Claude API (claude-sonnet or haiku)
     ↓
Voice Interface (sentence-stream → TTS with interrupt)
     ↓
[You hear response]
```

---

## 2. File Directory

```
~/local-ai-os/
├── aesop_core.py          Main orchestrator — start here
├── voice_interface.py     STT + TTS + VAD + interruption engine
├── meta_prompt_engine.py  Concierge layer — intent, routing, meta-prompts
├── tts_engine.py          Low-level TTS wrapper (termux-tts-speak)
├── browser_agent.py       Web scraper and doc navigator
├── setup_models.sh        One-time model download script
├── CLAUDE.md              Architecture index (machine-readable)
└── profiles/
    ├── razr_ultra.env     Razr Ultra 2025 — full NPU stack
    ├── tab_s9_fe.env      Tab S9 FE — Moonshine + Claude
    ├── s21.env            Galaxy S21 — Moonshine + Claude
    └── base.env           Any device — Termux STT/TTS only

~/autostart.sh             Container launch script (tmux)
~/.shortcuts/launch_ai.sh  Termux Widget / volume-key shortcut
```

**Model files (downloaded by setup_models.sh):**

```
~/kokoro-v1.0.onnx         Kokoro TTS model (~180 MB)
~/voices-v1.0.bin          Kokoro voice pack (~150 MB)
~/.cache/moonshine/        Moonshine STT cache (auto, 26–57 MB)
~/models/OmniNeural-4B/    OmniNeural NPU model (Razr Ultra only)
```

---

## 3. First-Time Setup

### Step 1 — Install system packages (inside Termux, not root)
```bash
pkg install proot-distro tmux python
proot-distro install ubuntu
```

### Step 2 — Enter the Ubuntu container
```bash
proot-distro login ubuntu
```

### Step 3 — Set up environment (inside Ubuntu)
```bash
mkdir -p $HOME/.tmp
echo 'export CLAUDE_CODE_TMPDIR=$HOME/.tmp' >> ~/.bashrc
echo 'which() { type -p "$@"; }' >> ~/.bashrc
echo 'export -f which' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Step 4 — Download models
```bash
cd ~/local-ai-os
bash setup_models.sh

# Razr Ultra only — add OmniNeural:
INSTALL_OMNI=1 bash setup_models.sh
```

### Step 5 — Set your Claude API key
```bash
export ANTHROPIC_API_KEY=sk-ant-...
# Make permanent:
echo 'export ANTHROPIC_API_KEY=sk-ant-...' >> ~/.bashrc
```

### Step 6 — Launch
```bash
source profiles/tab_s9_fe.env    # choose your device
python3 aesop_core.py
```

---

## 4. Launching AESOP

### Via Termux Widget (home screen)
1. Install **Termux:Widget** from F-Droid
2. Long-press home screen → Widgets → Termux:Widget
3. The widget will show `launch_ai.sh` — tap it

### Via volume key (after widget is set up)
- Assign the widget shortcut to a volume key via Android Accessibility

### Manually from Termux
```bash
proot-distro login ubuntu -- bash /root/autostart.sh
```

### From inside the container
```bash
bash ~/autostart.sh
# or directly:
cd ~/local-ai-os && source profiles/tab_s9_fe.env && python3 aesop_core.py
```

### tmux session controls
| Action | Keys / Command |
|---|---|
| Detach (keep running) | `Ctrl+B` then `D` |
| Re-attach | `tmux attach -t ai_core` |
| List sessions | `tmux ls` |
| Kill session | `tmux kill-session -t ai_core` |

---

## 5. Device Profiles

Profiles set all backend env vars. Source one before launching.

| Profile | Device | STT | TTS | Delegation |
|---|---|---|---|---|
| `razr_ultra.env` | Razr Ultra 2025 | Moonshine base | Kokoro | OmniNeural NPU |
| `tab_s9_fe.env` | Tab S9 FE | Moonshine tiny | Kokoro | Claude API |
| `s21.env` | Galaxy S21 | Moonshine tiny | Termux | Claude API |
| `base.env` | Any Android | Termux STT | Termux TTS | Claude API |

**Usage:**
```bash
source profiles/razr_ultra.env && python3 aesop_core.py
```

**Key environment variables:**

| Variable | Options | Default |
|---|---|---|
| `STT_BACKEND` | `termux`, `moonshine`, `vosk` | `termux` |
| `TTS_BACKEND` | `termux`, `kokoro` | `termux` |
| `DELEGATION_BACKEND` | `claude`, `omni` | `claude` |
| `MOONSHINE_SIZE` | `tiny`, `base` | `tiny` |
| `KOKORO_VOICE` | `af_heart`, `af_bella`, `am_adam`, ... | `af_heart` |
| `VAD_THRESHOLD` | integer (RMS energy) | `600` |
| `MAX_TOKENS` | integer | `512` |
| `CLAUDE_MODEL` | any Claude model ID | `claude-sonnet-4-6` |

---

## 6. Module Reference

### aesop_core.py
Entry point. Wires all modules together.

| Symbol | Purpose |
|---|---|
| `AESOPCore` | Main class |
| `.run()` | Start the voice loop |
| `_ClaudeClient` | Manages Claude API + conversation history |
| `.chat(meta, on_sentence)` | Send prompt; streams sentences to TTS |
| `.clear_history()` | Reset conversation memory |

**Run directly:**
```bash
python3 aesop_core.py
```

---

### voice_interface.py
STT + TTS + VAD + interruption.

| Symbol | Purpose |
|---|---|
| `VoiceInterface` | Main class |
| `.speak(text, allow_interrupt)` | TTS; returns `True` if user interrupted |
| `.listen(prompt_text)` | VAD-gated STT; returns transcribed string |
| `.run_loop(on_input)` | Standalone voice loop with callback |
| `_MoonshinSTT` | Moonshine ONNX backend |
| `_KokoroTTSBackend` | Kokoro ONNX backend |
| `_TermuxSTT` | Android on-device STT |
| `_TermuxTTSBackend` | termux-tts-speak |
| `_VADWatcher` | Background mic monitor for interruption |

**Embed in your own script:**
```python
from voice_interface import VoiceInterface
vi = VoiceInterface()
text = vi.listen()           # one listen
vi.speak("Hello")            # one speak
vi.run_loop(my_callback)     # full loop
```

---

### meta_prompt_engine.py
Intent classification and prompt structuring.

| Symbol | Purpose |
|---|---|
| `MetaPromptEngine` | Main class |
| `.build(raw_speech)` | Returns a `MetaPrompt` object |
| `MetaPrompt` | Dataclass: `intent`, `system_prompt`, `user_message`, `context_tags` |
| `.to_api_messages()` | Returns Claude-ready messages list |
| `_OmniNeuralBackend` | OmniNeural-4B on Hexagon NPU (Razr Ultra) |

**Intent types:** `file_op`, `web`, `system`, `calendar`, `code`, `summarize`, `compose`, `converse`

**Test it:**
```bash
python3 meta_prompt_engine.py
```

---

### tts_engine.py
Low-level TTS with state broadcast.

| Symbol | Purpose |
|---|---|
| `TTSEngine` | Main class |
| `.speak(text)` | Blocking TTS |
| `.speak_async(text)` | Non-blocking thread |
| `.announce(text, title)` | TTS + popup dialog |
| `.stop()` | Kill active TTS process |
| `read_state()` | Returns `{speaking, last, ts}` from any script |

---

### browser_agent.py
Web scraping and tutorial execution.

| Symbol | Purpose |
|---|---|
| `BrowserAgent` | Main class |
| `.scrape(url)` | Fetch page → `{title, text, saved_to}` |
| `.crawl_docs(url, max, pattern)` | Follow internal links |
| `.run_tutorial_steps(steps)` | Run shell commands, log results |

---

## 7. Edge Model Guide

### Moonshine STT
- **Size:** 26 MB (tiny) · 57 MB (base)
- **Install:** `pip install useful-moonshine-onnx`
- **Model:** auto-downloads to `~/.cache/moonshine/` on first use
- **Set:** `STT_BACKEND=moonshine MOONSHINE_SIZE=tiny`
- **Accuracy:** Better than Whisper Large V3 at fraction of size

### Kokoro TTS
- **Size:** ~330 MB total (model + voices)
- **Install:** `pip install kokoro-onnx soundfile`
- **Models:** Downloaded by `setup_models.sh`
- **Set:** `TTS_BACKEND=kokoro KOKORO_VOICE=af_heart`
- **Voices:** `af_heart` (warm F), `af_bella` (clear F), `am_adam` (M), `am_michael` (M)
- **Quality:** High — near human at 82M params

### OmniNeural-4B (Razr Ultra only)
- **Chip required:** Qualcomm Snapdragon 8 Elite (Gen 4)
- **Install:** `INSTALL_OMNI=1 bash setup_models.sh`
- **SDK:** Nexa SDK (`pip install nexaai`)
- **Set:** `DELEGATION_BACKEND=omni`
- **Role:** Parses intent + refines prompts on NPU before Claude API

---

## 8. Voice Commands

Say these during a session:

| You say | AESOP does |
|---|---|
| *(speak naturally)* | Transcribes, routes, responds |
| *(speak while AESOP is talking)* | Interrupts immediately, listens |
| **"stop"** / **"quit"** / **"exit"** | Ends the session |
| **"clear history"** / **"reset"** | Wipes conversation memory |
| **"goodbye"** | Graceful shutdown |

---

## 9. Editing Artifacts & Skills

### Edit a Python module
```bash
cd ~/local-ai-os
nano voice_interface.py       # or vi, or open in VS Code via SSH
```

### Change your API key
```bash
nano ~/.bashrc
# Edit the ANTHROPIC_API_KEY line
source ~/.bashrc
```

### Change your device profile
```bash
nano ~/local-ai-os/profiles/tab_s9_fe.env
# Edit any variable, save, then:
source profiles/tab_s9_fe.env && python3 aesop_core.py
```

### Add a new intent type
1. Open `meta_prompt_engine.py`
2. Add a regex pattern to `INTENT_PATTERNS`
3. Add a system prompt addendum to `_INTENT_ADDENDUM`
4. No restart needed — reload the module

### Swap Kokoro voice
```bash
export KOKORO_VOICE=am_adam    # male voice
python3 aesop_core.py
```
Available voices: `af_heart`, `af_bella`, `af_nicole`, `am_adam`, `am_michael`

### Adjust VAD sensitivity
If AESOP triggers too easily (loud room):
```bash
export VAD_THRESHOLD=900       # raise the threshold
```
If AESOP misses your speech:
```bash
export VAD_THRESHOLD=400       # lower the threshold
```

### Add AESOP to a new script
```python
from aesop_core import AESOPCore
# or just the voice layer:
from voice_interface import VoiceInterface
from meta_prompt_engine import MetaPromptEngine
```

---

## 10. Troubleshooting

### "ANTHROPIC_API_KEY not set"
```bash
export ANTHROPIC_API_KEY=sk-ant-...
echo 'export ANTHROPIC_API_KEY=sk-ant-...' >> ~/.bashrc
```

### No audio / sounddevice error
- Check Android mic permissions: Settings → Apps → Termux → Permissions → Microphone
- Try: `python3 -c "import sounddevice; print(sounddevice.query_devices())"`

### Moonshine model not found
The model downloads automatically on first use. If it fails:
```bash
python3 -c "from moonshine_onnx import MoonshineOnnxModel; MoonshineOnnxModel('moonshine/tiny')"
```

### Kokoro TTS silent / error
Check model files exist:
```bash
ls -lh ~/kokoro-v1.0.onnx ~/voices-v1.0.bin
# If missing: bash setup_models.sh
```

### OmniNeural won't load
- Confirm device: must be Snapdragon 8 Elite (Razr Ultra 2025, S25 Ultra)
- Check: `INSTALL_OMNI=1 bash setup_models.sh`
- System falls back to local rule-based parsing automatically

### tmux session missing
```bash
tmux ls                        # list sessions
bash ~/autostart.sh            # create new session
```

### termux-speech-to-text returns empty
- Check Termux:API is installed from F-Droid
- Grant microphone permission to Termux:API app

### "Cannot run pkg as root"
Run pkg commands in your normal Termux session (not inside PRoot Ubuntu):
- Open a new Termux tab without `proot-distro login`

---

## 11. Script File Log

| File | Location | Purpose | Last Updated |
|---|---|---|---|
| `aesop_core.py` | `~/local-ai-os/` | Main AESOP orchestrator | 2026-05-13 |
| `voice_interface.py` | `~/local-ai-os/` | STT + TTS + VAD + interrupt | 2026-05-13 |
| `meta_prompt_engine.py` | `~/local-ai-os/` | Intent routing, OmniNeural | 2026-05-13 |
| `tts_engine.py` | `~/local-ai-os/` | Low-level TTS + state | 2026-05-13 |
| `browser_agent.py` | `~/local-ai-os/` | Web scrape + doc crawl | 2026-05-13 |
| `setup_models.sh` | `~/local-ai-os/` | Download edge models | 2026-05-13 |
| `CLAUDE.md` | `~/local-ai-os/` | Machine-readable arch index | 2026-05-13 |
| `autostart.sh` | `~/` | tmux session launcher | 2026-05-13 |
| `launch_ai.sh` | `~/.shortcuts/` | Termux widget shortcut | 2026-05-13 |
| `profiles/razr_ultra.env` | `~/local-ai-os/profiles/` | Razr Ultra device config | 2026-05-13 |
| `profiles/tab_s9_fe.env` | `~/local-ai-os/profiles/` | Tab S9 FE config | 2026-05-13 |
| `profiles/s21.env` | `~/local-ai-os/profiles/` | S21 config | 2026-05-13 |
| `profiles/base.env` | `~/local-ai-os/profiles/` | Fallback config | 2026-05-13 |
| `AESOP_Launch_Tutorial.md` | `/sdcard/Download/` | Basic launch guide | 2026-05-13 |
| `AESOP_Full_Reference.md` | `/sdcard/Download/` | This file | 2026-05-13 |

---

*AESOP — Android Edge-Pi System Operations Platform*
*Claude API · Moonshine STT · Kokoro TTS · OmniNeural-4B NPU*
