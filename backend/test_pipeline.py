from backend.services.translation_service import translate_text
from backend.services.tts_service import text_to_speech

# Example: Translate English to Hindi and speak
text = "Hello, how are you?"
translated = translate_text(text, target_lang="hi")
print("Translated:", translated)

# Speak the translated text
text_to_speech(translated, lang="hi")
