# backend/routes/tts_routes.py
from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from backend.services.tts_service import text_to_speech_stream
import io

router = APIRouter()

@router.get("/tts")
async def tts_endpoint(
    text: str = Query(..., description="Text to convert to speech"),
    lang: str = Query("hi", description="Language code (default: Hindi)")
):
    """
    Convert text to speech and stream back as audio.
    """
    try:
        audio_data = text_to_speech_stream(text, lang)
        return StreamingResponse(
            io.BytesIO(audio_data),
            media_type="audio/mpeg"
        )
    except Exception as e:
        return {"error": str(e)}
