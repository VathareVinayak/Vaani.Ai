import speech_recognition as sr
import tempfile
import os

recognizer = sr.Recognizer()

def recognize_speech(file=None, source_lang="en"):
    if file:
        # Save uploaded file to a temp WAV (safer for sr.AudioFile)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
            tmp_wav.write(file.read())
            tmp_wav.flush()
            tmp_path = tmp_wav.name

        try:
            with sr.AudioFile(tmp_path) as source:
                audio = recognizer.record(source)
        finally:
            os.remove(tmp_path)  # cleanup
    else:
        # From microphone
        with sr.Microphone() as source:
            print(f"🎤 Speak something in [{source_lang}]...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio, language=source_lang)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
