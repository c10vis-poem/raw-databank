AUDIT-05-HORIZONS-UI.md
Audit & Extraction Report: Subfolder 5 of ___Lex-Novi-Æxentis-Copiæ (--•🌄HORIZONS_UI_🌐)
Scope: Master frontend presentation shell (APK 1), Four Rooms & Seven-Tile architecture, and WebSocket client bridges.
Parent Source: ___Lex-Novi-Æxentis-Copiæ/--•🌄HORIZONS_UI_🌐 (19IfkuOMOGRiuLANHEg3fU9gjhMu5sbQs).
Status: All original files preserved 100% untouched.


________________


1. Purpose & System Role: The Presentation Concierge (APK 1)
Horizons UI is the primary visual interface and concierge shell for the entire ecosystem.
The Decoupled Invariant:
* Horizons UI contains zero heavy inference runtimes or bash command executors inside its own process.
* It operates as an Android Chromium WebView hosting an HTML5/React workspace.
* It connects via local WebSockets to the background daemons:
   * ws://127.0.0.1:8080/shell ➔ Connects to Æsc APK for terminal I/O.
   * ws://127.0.0.1:8765 ➔ Connects to Æyre APK for real-time speech and VAD audio events.


________________


2. The Four Rooms & Seven-Tile Modular Architecture
Extracted directly from 4. Surface level spec: The Four Rooms & Seven-Tile Modular Architecture:


┌────────────────────────────────────────────────────────────────────────┐


│                        HORIZONS UI FRONTEND                            │


├────────────────────────────────────────────────────────────────────────┤


│ 1. The Four Rooms (Contextual Viewports):                              │


│    • The Room of Thought     ➔ Model reasoning, planning, and prompts  │


│    • The Room of Action      ➔ Terminal execution, bash runs, tool I/O │


│    • The Room of Observation ➔ Screen vision, sensory feeds, and logs  │


│    • The Room of Knowledge   ➔ Obsidian living wiki & graph navigator  │


├────────────────────────────────────────────────────────────────────────┤


│ 2. The Seven Functional Tiles:                                         │


│    [1. Chat Interface]       [2. Terminal Stream]    [3. Model Picker] │


│    [4. File Browser / RAG]   [5. Voice / VAD Canvas] [6. Hardware NPU] │


│                        [7. AST Code Graph View]                        │


└────────────────────────────────────────────────────────────────────────┘


________________


3. Subfolder Breakdown & Audit
1. 📁 (*8-5) What_it_IS_/What_it_DOES-Horizons _Ui:
   * Houses the core architectural specifications: The Four Rooms & Seven-Tile Modular Architecture, The Horizons Workbench, and Horizons App: Comprehensive Architectural Blueprint.
   * Action: Codified into novaexopia/horizons-ui/ in 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md.
2. 📁 Th.GOLDEN-TICKET🎫:
   * Contains QNN/QAIRT-System Design: half Gemini slop/ half useful info.
   * Extraction: Mined the FastRPC JNI bindings and buffer handover routines connecting the UI to the Qualcomm HTP kernel.
   * Action: Enveloped into README_VENDOR_CORPORA.md.
3. 📁 DesignXorpus & themes:
   * Visual styling parameters, dark-mode CSS tokens, and accessibility contrast standards for mobile OLED and outdoor field monitors.
   * Action: Preserved in novaexopia/horizons-ui/app/src/main/assets/web/themes/.
4. 📁 build-jha & Reference archives:
   * Historical build scripts and discussion transcripts detailing early Android packaging issues.
   * Action: Retained untouched in place for historical provenance.


________________


4. What Was Combined & What Was Trimmed
* Fluff Trimmed: Removed speculative discussions about Flutter vs. React Native (the decision is firmly locked on Chromium WebView + native Kotlin background services).
* Combined Specifications:
   * Synthesized the Four Rooms & Seven-Tile architecture directly with the WirelessAdbBridgeService.kt WebSocket specs, creating a unified frontend-to-daemon bridge.