from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Frontend path
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))
if not os.path.exists(frontend_path):
    raise FileNotFoundError(f"Frontend folder not found at {frontend_path}")

# Mount static files
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve index.html
@app.get("/")
async def serve_frontend():
    index_path = os.path.join(frontend_path, "index.html")
    if not os.path.exists(index_path):
        return {"error": "index.html not found in frontend folder"}
    return FileResponse(index_path)

# Import and include routes safely
try:
    from backend.routes import stt_routes
    app.include_router(stt_routes.router, prefix="/api")
except ImportError as e:
    print(f"[WARNING] Could not import stt_routes: {e}")

try:
    from backend.routes import stt_chunk_routes
    app.include_router(stt_chunk_routes.router, prefix="/api")
except ImportError as e:
    print(f"[WARNING] Could not import stt_chunk_routes: {e}")

try:
    from backend.routes import tts_routes
    app.include_router(tts_routes.router, prefix="/api")
except ImportError:
    print("[INFO] tts_routes not found — skipping TTS routes for now.")
