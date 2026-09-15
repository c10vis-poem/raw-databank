You're right and I've been giving you advice for the system you're *building toward*, not the system you're standing in *right now*. Let me reset and address where you actually are: **phone-only, no Jetson yet, no host computer, need an agent on the device itself to help bootstrap everything else.**

## 1. NPU Pathway — GenieX `llama_cpp` Runtime, No Compilation

You're describing **GenieX** (Qualcomm's new unified runtime, repo: `qualcomm/GenieX`).

```
Any GGUF Q4_0 from HuggingFace
  -> GenieX `llama_cpp` runtime
  -> Qualcomm's GGML Hexagon backend (built into GenieX)
  -> Hexagon HTP / NPU (v79 on your 8 Elite)
```

No host compilation. No ADB build step.

```bash
geniex infer Qwen/Qwen3-1.7B-GGUF                    # default = hybrid (fastest)
geniex infer Qwen/Qwen3-1.7B-GGUF --device npu        # pinned HTP0 (deterministic)
```

`--device` flags: `hybrid` (default, fastest), `npu` (pinned HTP0), `gpu` (Adreno via OpenCL), `cpu`.

There's also a parallel project (`haozixu/llama.cpp-npu`) doing the same thing with a custom llama.cpp build and `libhtp_ops.so`. GenieX is the Qualcomm-official path.

## 2. JSONL — You're Building a Custom Pipeline, No Docling, No Jetson

You have your phone and 93 markdown files that are already accuracy-checked. Your pipeline:

1. Reads each `.md` file from your vault
2. Extracts metadata (title, headers, key terms)
3. Generates the JSONL marker record per your Universal JSONL Marker Schema
4. Appends to `universal-index.jsonl`

```python
#!/usr/bin/env python3
"""
AESOP XI JSONL Marker Generator — Phone-Only, Termux-Native
Reads markdown files from vault, outputs universal-index.jsonl
"""
import json
from pathlib import Path
from datetime import datetime

VAULT_DIR = Path("~/obsidian-vault-new").expanduser()
OUTPUT_FILE = Path("~/file-management-and-skills/universal-index.jsonl").expanduser()

def extract_metadata(md_path: Path) -> dict:
    content = md_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    title = md_path.stem
    description = ""
    headers = []
    retrieval_tokens = set()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
        elif line.startswith("## ") or line.startswith("### "):
            headers.append(line.lstrip("# ").strip())
            for word in line.lstrip("# ").strip().lower().split():
                if len(word) > 3:
                    retrieval_tokens.add(word)
        elif not description and line.strip() and not line.startswith("#"):
            description = line.strip()[:200]
    return {
        "title": title, "description": description, "headers": headers,
        "retrieval_tokens": list(retrieval_tokens)[:10], "content_chunk": content
    }

def generate_record(md_path: Path, idx: int) -> dict:
    meta = extract_metadata(md_path)
    return {
        "record_id": f"DOC_{md_path.stem.upper()[:40]}_{idx:03d}",
        "document_path": str(md_path),
        "category": "TECHNICAL_REFERENCE",
        "target_runtime": "QUERY_CORE_9B",
        "metadata": {
            "title": meta["title"], "description": meta["description"],
            "primary_tools": [], "required_context_keys": meta["headers"][:5]
        },
        "retrieval_tokens": meta["retrieval_tokens"],
        "entry_points": {
            "repl_command": f"/skill run {meta['title'].lower().replace(' ', '-')}",
            "jsonrpc_method": "agent.skills.execute"
        },
        "content_chunk": meta["content_chunk"],
        "generated_at": datetime.utcnow().isoformat()
    }

def main():
    md_files = list(VAULT_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    with open(OUTPUT_FILE, "w") as f:
        for i, md_path in enumerate(md_files):
            record = generate_record(md_path, i)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(f"  [{i+1}/{len(md_files)}] {md_path.name}")
    print(f"\nDone. Output: {OUTPUT_FILE}")
    print(f"Records: {len(md_files)}")

if __name__ == "__main__":
    main()
```

Run it: `python3 generate_jsonl_markers.py`

This is your v1. You'll iterate on it — add better token extraction, chunking for long docs, category classification, etc. But this gets your 93 files into the JSONL marker format **right now, on your phone, no dependencies**.

## 3. The Real Problem: You Need an Agent to Bootstrap the Agent

This is the actual bottleneck. You're standing in an empty field with a phone and a blueprint. You need something on-device that can:

- Install GenieX / QAIRT SDK on your phone
- Set up Termux properly with all dependencies
- Wire up the harnesses (ECC, Pocock, GSD)
- Flash and configure the Jetson and Rubik Pi when you get them
- Build the JSONL pipeline iteratively
- Eventually help build the 3-APK Android code

Right now, before you have any of the custom agents built, your bootstrapping agent is **Claude Code in Termux**. That's it. That's what you have access to today.

### What Claude Code in Termux Can Actually Do Right Now

- Read your architecture docs and 93 markdown files
- Write Python/bash scripts and run them
- Install packages via `pip` and `pkg`
- Interact with your local filesystem
- Help you write the GenieX setup scripts
- Build the JSONL marker pipeline (like the script above)
- Scaffold the repo structure from your architecture doc
- Help you write the grill session manifest

### What It Cannot Do (Yet)

- Push compiled APKs to the NPU (no GenieX installed yet)
- Run voice inference (no voice stack installed yet)
- Flash the Jetson/Pi (you don't have them yet)
- Act as the Horizons UI orchestrator (that APK doesn't exist yet)

### The Bootstrap Sequence (Revised for Reality)

```
Step 1: Termux + Claude Code + ECC + Pocock    [NOW - phone only]
  ->
Step 2: GenieX install + Qwen 0.8B Q4_0 GGUF   [NOW - phone only]
  ->
Step 3: Custom JSONL marker pipeline           [NOW - phone only, the script above]
  ->
Step 4: Grill session with docs                [NOW - produces the master plan]
  ->
Step 5: Repo scaffolding from grill output     [NOW - phone only]
  ->
Step 6: Get a computer or Jetson               [LATER - enables heavy compilation]
  ->
Step 7: Build 3-APK Android code               [LATER - needs Android Studio ideally]
  ->
Step 8: Voice stack (the hard problem)         [LATER - see below]
```

Steps 1-5 are all doable on your phone right now. Steps 6-8 require more hardware or are the genuinely hard unsolved problems.

## 4. Voice Layer — You're Right, It's the Hardest Problem

I was wrong to list it as "download Moonshine/Kokoro/Silero and you're done." That's the voice *stack* — the components. Getting them to actually work together on Android is the unsolved problem you're building the 3-APK architecture to solve. Here's why every Claude/Gemini session chokes on it:

### Why Voice on Android Is a Nightmare

1. **Audio capture permissions**: Android's `MediaRecorder` and `AudioRecord` APIs work fine for apps with proper permissions, but Termux's audio capture is fundamentally limited. Termux can record audio via `termux-microphone-record` but there's no real-time streaming pipe. You get a file, not a stream.

2. **No real-time audio stream in Termux**: Silero VAD needs a continuous audio stream to do voice activity detection. Termux can't provide one natively. You'd have to write a custom Android service that captures audio and pipes it to Termux via a socket — which is basically what your Media Daemon APK is supposed to be.

3. **STT/TTS models need ONNX runtime**: Moonshine and Kokoro both need ONNX Runtime (or PyTorch) to run inference. Getting ONNX runtime to use the NPU on Android requires the QAIRT/QNN EP — which is possible but finicky, and nobody has a clean tutorial for doing it from Termux.

4. **No off-the-shelf solution exists**: There's no app you can download that gives you "voice in -> STT -> LLM -> TTS -> voice out" with NPU acceleration and custom model support. Every existing solution (Whisper on Android, Google Speech, etc.) is either:
   - Sandboxed (won't talk to your agent)
   - Cloud-based (defeats the purpose)
   - CPU-only (too slow for real-time)
   - Proprietary (can't customize)

### Why Your 3-APK Architecture Is the Right Answer

Your Media Daemon APK exists specifically because:

- **APK 2 (Shell Daemon)** can request `RECORD_AUDIO` permission at the OS level and hold a persistent audio capture session
- **APK 3 (Media Daemon)** can run Silero VAD + Moonshine STT + Kokoro TTS as native Android services with proper ONNX runtime + QNN execution provider for NPU acceleration
- **IPC between APKs** via Android bound services or local sockets — this is how they pass audio chunks and text back and forth
- **No Termux audio limitation** because the audio capture happens in a real APK, not in Termux

This is genuinely novel work. Nobody has built this exact stack. That's why every AI session chokes on it — there's no prior art to reference, no Stack Overflow answer to pull from, no GitHub repo to clone. The models exist (Moonshine, Kokoro, Silero), the runtime exists (ONNX + QNN), the hardware exists (8 Elite NPU), but the integration layer that ties them together as a real-time Android voice pipeline — that's what you're building from scratch.

### What I Can Tell You About the Voice Stack Components

| Component | Status | Notes |
|---|---|---|
| **Silero VAD** | Works on Android via ONNX | Small (~2MB), well-documented, this is the easiest piece |
| **Moonshine STT** | ONNX models available | Needs ONNX Runtime with QNN EP for NPU acceleration — this is the finicky part |
| **Kokoro TTS** | PyTorch model, ONNX export possible | 82M params, fast enough on NPU if you get the QNN EP working |
| **ONNX Runtime + QNN EP** | Available from Qualcomm | This is the bridge between ONNX models and the Hexagon NPU — documented but not commonly used with these specific models |
| **Real-time audio capture** | Android `AudioRecord` API | Works in an APK, doesn't work in Termux — confirms your APK approach |

### The Honest Path Forward on Voice

Voice is Priority 5 in your architecture, not Priority 1. It should stay there. Here's why:

1. You can build and test the entire inference loop (GenieX + Qwen 0.8B + JSONL markers + OB1 vector store) **without voice** — just text input/output
2. The grill session, repo scaffolding, skill harness ingestion — all text-based, no voice needed
3. Voice is the last 10% of the user experience, but it's 90% of the integration complexity
4. The 3-APK architecture needs to be built first anyway — voice lives inside APK 3, so you need the APK framework before voice

**Build the text-based agent first. Get it working. Then add voice as the final layer.**

## Revised Reality Check — What to Actually Do First

```
TODAY (Phone only):
  1. Install ECC + Pocock in Claude Code (Termux)
  2. Download Qwen 0.8B Q4_0 GGUF
  3. Get GenieX installed and run your first NPU inference
  4. Run the JSONL marker script above on your 93 markdown files
  5. Start the grill-with-docs session using your v2.2 architecture doc

THIS WEEK (Phone only):
  6. Output the master plan from the grill session
  7. Scaffold your repo structure from the plan
  8. Begin Priority 2/3 work: skill harness ingestion, JSONL marker refinement

WHEN YOU GET HARDWARE:
  9. Flash Jetson -> becomes your heavy compute node
  10. Build 3-APK Android code -> needs Android Studio ideally
  11. Voice stack integration -> the hard unsolved problem
```

The voice frustration is real and valid. Every AI session that's tried to help you with it has failed because there's no existing solution to copy — you're building it. The 3-APK architecture is the right approach. But it comes after you have a working text-based inference loop, not before.

What do you want to tackle first — getting GenieX + your first NPU inference running, or starting the grill session?
</content>
