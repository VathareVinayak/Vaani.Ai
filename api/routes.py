from fastapi import APIRouter, File, UploadFile, Form
import asyncio
from services.stt_service import recognize_speech
from services.translation_service import translate_text
from services.tts_service import text_to_speech

router = APIRouter()

@router.post("/stt")
async def stt_endpoint(audio: UploadFile = File(...), lang: str = Form("en")):
    text = recognize_speech(file=audio.file, source_lang=lang)
    return {"recognized_text": text}

# --- Translation ---
@router.post("/translate")
async def translate_endpoint(text: str = Form(...), src: str = Form("en"), dest: str = Form("hi")):
    translated = translate_text(text, source_lang=src, target_lang=dest)
    return {"translated_text": translated}

# --- Text to Speech ---
@router.post("/tts")
async def tts_endpoint(text: str = Form(...), voice: str = Form("en-US-AriaNeural")):
    filename = "output.mp3"
    await text_to_speech(text, voice=voice, filename=filename)
    return {"message": "Audio generated", "file": filename}

# --- Full Pipeline ---
@router.post("/pipeline")
async def pipeline_endpoint(
    audio: UploadFile,
    src: str = Form("en"),
    dest: str = Form("hi"),
    voice: str = Form("hi-IN-SwaraNeural")
):
    # Step 1: STT
    text = recognize_speech(file=audio.file, source_lang=src)

    # Step 2: Translate
    translated = translate_text(text, source_lang=src, target_lang=dest)

    # Step 3: TTS
    filename = "translated.mp3"
    await text_to_speech(translated, voice=voice, filename=filename)

    return {
        "recognized_text": text,
        "translated_text": translated,
        "audio_file": filename
    }
