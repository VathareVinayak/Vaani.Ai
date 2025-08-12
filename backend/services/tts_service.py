# backend/services/tts_service.py
import os
from gtts import gTTS
import uuid

TTS_OUTPUT_DIR = os.path.join("backend", "static", "tts_output")
os.makedirs(TTS_OUTPUT_DIR, exist_ok=True)

def text_to_speech_file(text: str, lang: str = "hi") -> str:
    try:
        filename = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join(TTS_OUTPUT_DIR, filename)

        tts = gTTS(text=text, lang=lang)
        tts.save(file_path)
        return filename
    except Exception as e:
        print(f"[TTS Error]: {e}")
        raise RuntimeError("Failed to convert text to speech") from e
