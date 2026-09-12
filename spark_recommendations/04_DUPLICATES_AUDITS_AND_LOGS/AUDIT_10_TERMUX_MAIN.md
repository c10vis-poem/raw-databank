AUDIT-10-TERMUX_MAIN.md
Audit & Extraction Report: Subfolder 11 of _Lex-Novi-Æxentis-Copiæ (--•🖥️_TERMUX[> ]_main.)
Scope: On-device Termux execution, DroidDesk cross-device workstation, post-reboot startup sequences, and GCP terminal authentication.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/--•🖥️_TERMUX_[>_ ]_main. (1XK7bRmY5yDJKDdUqwLtHw0dUmQ0zv-oq).
Status: All original files preserved 100% untouched.


________________


1. Purpose & System Role: Mobile Shell & Workstation Engine
This folder contains the concrete, battle-tested on-device deployment runbooks for Node Alpha (Phone) and your Samsung Galaxy Tab S9 FE:


* Standardizes the automated startup sequence that launches local models and speech daemons on boot.
* Establishes the DroidDesk / Termux:X11 dual-device architecture turning your phone into a headless compute server and your tablet into a desktop workstation.


________________


2. Major Technical Extractions & Discoveries
A. Post-Reboot Model & Voice Startup Sequence
Extracted directly from Getting the local LLM + voice pipeline working (every time after a reboot):


1. Step 1 (Launch Local Model):


bash ~/aesop/deploy/phone/boot.sh


Spawns a detached tmux session named llm running Qwen 3.5 9B on the Hexagon NPU. Prints AESOP Edge Online in ~20 seconds.


2. Step 2 (Launch OpenWiki TUI):


ow


Launches OpenWiki pointed at the local NPU. Binds native hotkeys: Ctrl+R to record voice, Ctrl+S to transcribe via Moonshine STT and speak via Kokoro TTS (zero cloud latency).


3. Step 3 (Claude Code Push-to-Talk): Tap ALT then K (sending Meta+K) to trigger Claude Code's built-in voice input, bypassing Android keyboard input eating.
* Action: Codified into 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md boot sequence.
B. The DroidDesk Tablet-to-Phone Workstation Pipeline
Extracted directly from Termux:X11 desktop install :


* The Tablet (Main Native Screen):
   * Runs Termux:X11 for lag-free, hardware-accelerated desktop rendering.
   * Runs DroidDesk (pkg install x11-repo && ./setup.sh) providing a clean PC desktop interface with app launchers.
* The Phone (Headless Server & Claude CLI):
   * Runs Debian via PRoot (proot-distro install debian).
   * Runs Node.js LTS and @anthropic-ai/claude-code.
   * Broadcasts its desktop locally via noVNC / websockify on port 8080:


vncserver :1


websockify --web /usr/share/novnc 8080 localhost:5901


* The Unified Workflow: The tablet opens a browser window inside DroidDesk pointing to http://<PHONE_IP>:8080/vnc.html, monitoring phone CLI tasks while multitasking natively.
* Action: Enveloped into 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md.
C. GCP $1,000 Vertex Credit Terminal Fast-Track
Extracted from Google cloud API hooks guide through termux.:


* Bypasses the complex Google Cloud IAM web console entirely.
* Enables APIs instantly via Cloud Shell:


gcloud services enable aiplatform.googleapis.com storage.googleapis.com documentai.googleapis.com


* Authenticates mobile Termux without JSON service keys using application default login:


gcloud auth application-default login


* Action: Ingested into 04_skills_runtime/extracted_tools/cli/gcs_sync.sh.
D. Verified Hardware Configs (ASSETS.txt)
* Mined real configuration parameters:
   * processor_config.json: Gemma4AudioFeatureExtractor spectrogram parameters (128 features, 750 seq length).
   * htp_backend_ext_config.json: QNN HTP configuration verified against Hexagon v79.
   * mcp.json: Configuration for agentmemory MCP server.
* Action: Codified into 02_wiki_md/architectures/snapdragon_npu.md.


________________


3. What Was Combined & What Was Trimmed
* Fluff Trimmed: Trimmed debugging logs from broken third-party audio packages (termux-tts-speak hangs and broken symlinks).
* Combined Runbooks:
   * Unified the 2026-08-28 GLM Setup Guide with the post-reboot startup sequence into a master operator runbook in 02_wiki_md/runbooks/.