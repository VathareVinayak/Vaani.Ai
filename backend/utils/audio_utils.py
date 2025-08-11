# audio_utils - Handles saving uploaded audio files and converting them if needed

import os
from pydub import AudioSegment

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_audio_file(file, filename):
    """
    Saves an uploaded audio file to the uploads directory.
    """
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(file)
    return file_path

def convert_to_wav(input_path):
    """
    Converts an audio file to WAV format (if not already).
    """
    if input_path.endswith(".wav"):
        return input_path
    
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path