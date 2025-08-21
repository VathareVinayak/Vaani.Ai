# Vaani.Ai - Speech Translation API

Vaani.Ai is a backend service built using FastAPI that integrates Speech-to-Text (STT), Translation, and Text-to-Speech (TTS) pipelines. The API enables seamless, real-time language conversion between Multiple Lanuages, facilitating applications in voice assistants, multilingual communication tools, and accessibility solutions.

---

## 🛠️ Features

- **Speech-to-Text (STT):** Converts spoken English audio into text using the `speech_recognition` library.
- **Translation:** Translates the recognized text from English to Hindi using the `deep_translator` library.
- **Text-to-Speech (TTS):** Converts the translated Hindi text back into speech using Microsoft's Edge TTS engine.
- **Pipeline Endpoint:** A single endpoint that processes audio input through STT, Translation, and TTS, returning the translated speech file.

---

## 📁 Project Structure

vaani.ai/ ├── main.py                     # FastAPI app initialization ├── api/ │   └── routes.py               # API endpoints for STT, Translation, TTS, and Pipeline ├── services/ │   ├── stt_service.py          # Speech-to-Text functions │   ├── translation_service.py  # Text translation functions │   └── tts_service.py          # Text-to-Speech functions ├── audio/                      # Generated audio files (ensure this folder exists) ├── requirements.txt            # Python dependencies └── Dockerfile                  # Docker configuration for containerization

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VathareVinayak/Vaani.Ai.git
   cd Vaani.Ai

2. Create and activate a virtual environment:

python3 -m venv vaanienv
source vaanienv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install the required dependencies:

pip install -r requirements.txt


4. Ensure the audio/ directory exists to store generated audio files:

mkdir audio




---

🚀 Running the API

To start the FastAPI application:

uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000.


---

🧪 API Endpoints

POST /stt

Converts uploaded audio to text.

Request:

audio: Audio file (e.g., .wav, .mp3)

lang: Language code (default: en)


Response:

{
  "recognized_text": "Hello, how are you?"
}

POST /translate

Translates provided text to Hindi.

Request:

text: Text to translate

src: Source language code (default: en)

dest: Destination language code (default: hi)


Response:

{
  "translated_text": "नमस्ते, आप कैसे हैं?"
}

POST /tts

Converts provided text to speech and saves it as an audio file.

Request:

text: Text to convert

voice: Voice model (default: en-US-AriaNeural)


Response:

{
  "message": "Audio generated",
  "file": "output.mp3"
}

POST /pipeline

Processes audio input through STT, Translation, and TTS.

Request:

audio: Audio file

src: Source language code (default: en)

dest: Destination language code (default: hi)

voice: Voice model for TTS (default: hi-IN-SwaraNeural)


Response:

{
  "recognized_text": "Hello, how are you?",
  "translated_text": "नमस्ते, आप कैसे हैं?",
  "audio_file": "translated.mp3"
}


---

📦 Docker Support

To run the application in a Docker container:

1. Build the Docker image:

docker build -t vaani-ai .


2. Run the Docker container:

docker run -p 8000:8000 vaani-ai



The API will be accessible at http://localhost:8000.


---

📌 Acknowledgments

deep_translator for translation services.

edge_tts for text-to-speech functionality.

speech_recognition for speech-to-text conversion.




