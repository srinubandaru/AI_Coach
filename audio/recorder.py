import sounddevice as sd
import numpy as np
from config import FS, CHUNK_DURATION

def record_audio():
    print("Recording...")
    audio = sd.rec(int(CHUNK_DURATION * FS), samplerate=FS, channels=1, dtype='float32')
    sd.wait()
    return audio.flatten()
