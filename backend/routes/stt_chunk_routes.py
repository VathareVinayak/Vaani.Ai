from fastapi import APIRouter, Header, UploadFile, File, Request
from backend.services.stt_service import transcribe_audio
from backend.services.translation_service import translate_text
from backend.services.tts_service import text_to_speech_file
import os
import uuid
import aiofiles

router = APIRouter()

@router.post("/stt_chunk")
async def speech_to_text_chunk(request: Request, x_target_lang: str = Header(default="hi")):
    chunk_data = await request.body()

    backend_dir = os.path.dirname(os.path.abspath(__file__))
    saved_dir = os.path.join(backend_dir, "temp_audio")
    os.makedirs(saved_dir, exist_ok=True)

    chunk_filename = f"{uuid.uuid4()}.webm"
    chunk_path = os.path.join(saved_dir, chunk_filename)

    async with aiofiles.open(chunk_path, "wb") as f:
        await f.write(chunk_data)

    original_text = transcribe_audio(chunk_path)
    translated_text = translate_text(original_text, target_lang=x_target_lang)

    audio_filename = text_to_speech_file(translated_text, lang=x_target_lang)
    audio_url = f"/static/tts_output/{audio_filename}"

    return {
        "partial_transcription": original_text,
        "partial_translation": translated_text,
        "audio_url": audio_url,
    }