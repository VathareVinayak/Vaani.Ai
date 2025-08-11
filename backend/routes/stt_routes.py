from fastapi import APIRouter, Header, UploadFile, File, Request
from backend.services.stt_service import transcribe_audio
from backend.services.translation_service import translate_text
from backend.services.tts_service import text_to_speech_file
import os
import uuid
import aiofiles

router = APIRouter()

@router.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    saved_dir = os.path.join(backend_dir, "temp_audio")
    os.makedirs(saved_dir, exist_ok=True)
    saved_path = os.path.join(saved_dir, file.filename)

    async with aiofiles.open(saved_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    original_text = transcribe_audio(saved_path)
    translated_text = translate_text(original_text, target_lang="hi")

    audio_filename = text_to_speech_file(translated_text, lang="hi")
    audio_url = f"/static/tts_output/{audio_filename}"

    return {
        "transcription": original_text,
        "translation": translated_text,
        "audio_url": audio_url
    }
