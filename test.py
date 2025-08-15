# testing.py 
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# 1. Speech to Text
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Speak something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = "Hello Dattaraj, I am the Vaani a voice translator created by Vinayak"
    #recognizer.recognize_google(audio, language="en")
    print(f"📝 Recognized Text: {text}")
except sr.UnknownValueError:
    print("❌ Could not understand audio")
    exit()
except sr.RequestError:
    print("❌ Could not request results from Google Speech Recognition service")
    exit()

# 2. Translate Text (English → Hindi)
try:
    translated_text = GoogleTranslator(source='en', target='hi').translate(text)
    print(f"🌐 Translated Text: {translated_text}")
except Exception as e:
    print(f"❌ Translation failed: {e}")
    exit()

# 3. Text to Speech (Hindi)
try:
    tts = gTTS(text=translated_text, lang="hi")
    output_file = "output.mp3"
    tts.save(output_file)
    print(f"🔊 Saved translated speech as {output_file}")

    # Play audio (Windows)
    if os.name == "nt":
        os.system(f"start {output_file}")
    else:
        os.system(f"mpg123 {output_file}")
except Exception as e:
    print(f"❌ TTS failed: {e}")
