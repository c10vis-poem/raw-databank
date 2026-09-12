import onnxruntime as ort
import numpy as np
import json
import subprocess
import scipy.io.wavfile

def phonemize(text, language='en-us'):
    """
    Converts text to a list of phoneme IDs using espeak.
    """
    # Use espeak to get the phonemes in IPA format
    process = subprocess.run(
        ['espeak', '-q', '--ipa', '-v', language, text],
        capture_output=True,
        text=True
    )
    ipa = process.stdout.strip()

    # This is a simplified mapping and might need to be expanded
    # based on the exact phonemes your Kokoro model was trained on.
    phoneme_map = {
        ' ': 0, 'X': 1, 'ə': 2, 'e': 3, 'I': 4, 'k': 5, 't': 6, 's': 7, 'n': 8,
        'o': 9, 'a': 10, 'd': 11, 'm': 12, 'l': 13, 'r': 14, 'i': 15, 'p': 16,
        'h': 17, 'b': 18, 'z': 19, 'w': 20, 'v': 21, 'u': 22, 'f': 23, 'ɡ': 24,
        'ŋ': 25, 'ʃ': 26, 'j': 27, 'ɔ': 28, 'ð': 29, 'θ': 30, 'ɛ': 31, 'ʒ': 32,
        'æ': 33, 'ʊ': 34, 'aɪ': 35, 'aʊ': 36, 'dʒ': 37, 'eɪ': 38, 'oʊ': 39,
        'ɔɪ': 40, 'tʃ': 41, 'ʌ': 42
    }
    
    # Simple tokenization - a better approach would handle multi-character phonemes
    tokens = []
    for p in ipa:
        if p in phoneme_map:
            tokens.append(phoneme_map[p])

    return np.array(tokens, dtype=np.int64).reshape(1, -1)


def synthesize(text, voice_name='am_adam', model_path='kokoro-v1.0.onnx', voices_path='voices.json'):
    """
    Synthesizes speech from text using the Kokoro model.
    """
    # 1. Phonemize the input text
    phoneme_ids = phonemize(text)

    # 2. Load the voice embedding
    with open(voices_path, 'r') as f:
        voices = json.load(f)
    
    if voice_name not in voices:
        raise ValueError(f"Voice '{voice_name}' not found in {voices_path}")

    voice_embedding = np.array(voices[voice_name], dtype=np.float32).reshape(1, -1)

    # 3. Run the ONNX model
    session = ort.InferenceSession(model_path)
    inputs = {
        'input_ids': phoneme_ids,
        'style_embedding': voice_embedding,
    }
    
    # Some Kokoro models also have a 'speed' input
    if 'speed' in [inp.name for inp in session.get_inputs()]:
        inputs['speed'] = np.array([1.0], dtype=np.float32)

    result = session.run(None, inputs)
    audio_out = result[0]

    # 4. Save the output as a .wav file
    scipy.io.wavfile.write("output.wav", 24000, audio_out.squeeze())
    print("Audio saved to output.wav")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python kokoro_tts.py \"<text to synthesize>\" [voice_name]")
        sys.exit(1)
    
    text_to_synthesize = sys.argv[1]
    voice = sys.argv[2] if len(sys.argv) > 2 else 'am_adam'
    
    synthesize(text_to_synthesize, voice)
