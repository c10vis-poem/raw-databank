# Æyre — media salvage

Voice and vision. Everything Android-media from the old Horizons repo lands here
rather than in `Aesc-Terminal-APK/`, resolving the overlap.

**Source:** `c10vis-poem/horizons-ui` @ `2c647964efe1375a12c14179e7c04ef2ed13350a`

| Folder | Contents |
|---|---|
| `audio/` | `AudioRecorder`, `VoiceLoopController`, and the VAD stack — `SileroVadDetector`, `RmsVadDetector`, `VadDetector` interface, `VadFactory` |
| `stt/` | `SttEngine` interface, `MoonshineSttEngine`, `DaemonSttClient` |
| `screen/` | `ScreenshotCapture` — the vision-side capture path |
| `specs/` | `tts_engine.xml`, `ime_method.xml` — the TTS engine and IME service declarations |

## Carry these two facts forward

**Moonshine STT has a ~10 second hard input ceiling.** Past roughly 9.5–10s it
fails **silently** — no exception, no truncation notice, no warning. You get
wrong or empty output and nothing tells you why. Chunk before the limit; build
the chunking in from the start rather than bolting it on.

**The proot audio bridge needed two fixes, not one.** Missing ALSA-over-Pulse
routing *and* client-side SHM disabled. Fixing either alone still looks like
total failure, which is how it stayed broken. Moot once this is native AAudio,
but worth knowing why the old setup was fragile.

Both are documented in the `aesop-voice-pipeline` skill.

## Status of the working pipeline

Confirmed end-to-end via `--demo` — TTS → speaker → STT round-trip, text matched.
**The live mic loop has never been verified.** Only `--demo` has run. Don't trust
the mic path blind.

## Note on the rewrite

The working implementation runs under Termux + Debian proot with PulseAudio. The
APK has neither — it has AAudio/Oboe and Android's own stack. **That is a
rewrite, not a port.** What carries over is the decisions (10s chunking rule, VAD
thresholds that worked, model choices, the round-trip verification method), not
the code.
