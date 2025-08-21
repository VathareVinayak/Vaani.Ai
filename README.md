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

Got it 👍
Here’s your project structure **purely in Markdown format**:

````markdown

vaani.ai/
├── main.py                  # FastAPI app initialization
├── api/
│   └── routes.py            # API endpoints for STT, Translation, TTS, and Pipeline
├── services/
│   ├── stt_service.py       # Speech-to-Text functions
│   ├── translation_service.py # Text translation functions
│   └── tts_service.py       # Text-to-Speech functions
├── audio/                   # Generated audio files (ensure this folder exists)
├── requirements.txt         # Python dependencies
└── Dockerfile               # Docker configuration for containerization
````


## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VathareVinayak/Vaani.Ai.git
   cd Vaani.Ai
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv vaanienv
   source vaanienv/bin/activate   # On Linux/Mac
   ```

   On Windows (PowerShell):

   ```bash
   .\vaanienv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure the `audio/` directory exists** (for generated audio files):

   ```bash
   mkdir audio
   ```

---

## 🚀 Running the API

Start the FastAPI application with:

```bash
uvicorn main:app --reload
```

The API will be accessible at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger Docs will be available at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



# 🧪 API Endpoints

---

### 🎤 POST `/stt`
Converts uploaded audio to text.  

**Screenshot:**  
![STT](https://github.com/VathareVinayak/Vaani.Ai/blob/main/Test_APi/SpeechToText.png)

---

### 🌐 POST `/translate`
Translates provided text to Hindi.  

**Screenshot:**  
![Translate](https://github.com/VathareVinayak/Vaani.Ai/blob/main/Test_APi/TextToText.png)

---

### 🔊 POST `/tts`
Converts provided text to speech.  

**Screenshot:**  
![TTS](https://github.com/VathareVinayak/Vaani.Ai/blob/main/Test_APi/TextToSpeech.png)

---

### 🔄 POST `/pipeline`
Processes audio input through STT → Translation → TTS.  

**Screenshot:**  
![Pipeline](https://github.com/VathareVinayak/Vaani.Ai/blob/main/Test_APi/PipelineSpeechToSpeech.png)

---

📦 Docker Support

To run the application in a Docker container:

1. Build the Docker image:

```bash
docker build -t vaani-ai .
```

2. Run the Docker container:
```bash
docker run -p 8000:8000 vaani-ai
```


The API will be accessible at http://localhost:8000.


---

📌 Acknowledgments

**deep_translator** for translation services.

**edge_tts** for text-to-speech functionality.

**speech_recognition** for speech-to-text conversion.

---
Email : work.vinayakvathare@gmail.com
linkedIn : https://www.linkedin.com/in/vinayakvathare/
