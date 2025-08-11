from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Mount the frontend folder as static files
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve the index.html directly
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# Import your STT routes
from backend.routes import stt_routes, stt_chunk_routes

app.include_router(stt_routes.router, prefix="/api")
app.include_router(stt_chunk_routes.router, prefix="/api")
