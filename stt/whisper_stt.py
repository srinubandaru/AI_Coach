import whisper
import ssl
from config import MODEL_SIZE

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model(MODEL_SIZE)

def transcribe(audio_array):
    result = model.transcribe(audio_array)
    return result["text"]
