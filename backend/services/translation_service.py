# backend/services/translation_service.py
from googletrans import Translator

translator = Translator()

def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translate the given text to the target language using Google Translate.
    """
    if not text.strip():
        return ""
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"[Translation Error]: {e}")
        # Return the original text if translation fails
        return text
