import edge_tts
import os
import platform
import subprocess

async def text_to_speech(text: str, voice: str, filename="output.mp3"):
    if not text:
        return None

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)
    print(f"🔊 Saved speech to {filename}")

    # --- BLOCKING PLAYBACK ---
    if platform.system() == "Windows":
        subprocess.run(["cmd", "/c", "start", "/wait", filename])
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["afplay", filename])
    else:  # Linux / Raspberry Pi
        subprocess.run(["mpg123", filename])
