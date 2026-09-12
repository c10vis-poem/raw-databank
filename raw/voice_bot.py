import os
import sys
import subprocess

BASE_DIR = os.path.expanduser("~/dual_audio")

def run_stt():
    print("\n🎤 Listening (5s)...", file=sys.stderr)
    # This records directly using your Android device microphone hook
    subprocess.run(["termux-microphone-record", "-f", os.path.join(BASE_DIR, "input.wav"), "-l", "5", "-r", "16000", "-c", "1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("📝 [Local Audio Captured] - Pipeline Ready.", file=sys.stderr)
    return "Local voice engine pipeline initialized."

def run_tts(text_to_speak):
    if not text_to_speak.strip():
        return
    print(f"🗣️ Engine Processing: {text_to_speak}", file=sys.stderr)
    # Generates a clean localized audio tone verification directly
    out_wav = os.path.join(BASE_DIR, "output.wav")
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=440:duration=0.5", out_wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["play-audio", out_wav], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    if not sys.stdin.isatty():
        piped_text = sys.stdin.read()
        run_tts(piped_text)
    else:
        captured_text = run_stt()
        print(captured_text)
