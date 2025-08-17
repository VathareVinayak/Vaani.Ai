from deep_translator import GoogleTranslator

def translate_text(text: str, source_lang="en", target_lang="hi") -> str:
    if not text:
        return ""
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    return translated
