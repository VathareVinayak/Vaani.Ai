# stt_service.py - Speech-to-text service using Whisper

import whisper
from backend.config import WHISPER_MODEL_SIZE

# Load the model once when the service starts (on CPU)
model = whisper.load_model(WHISPER_MODEL_SIZE, device="cpu")

def transcribe_audio(file_path):
    # Transcribes audio to text using OpenAI Whisper.
    result = model.transcribe(file_path, language="en")  # Change if you want auto-detect
    return result["text"]
