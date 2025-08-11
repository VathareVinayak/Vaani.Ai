from transformers import pipeline
import torch
from backend.config import TRANSLATION_MODEL

# Select device automatically
device = 0 if torch.cuda.is_available() else -1
print(f"Device set to use {'GPU' if device == 0 else 'CPU'}")

# Load translator once at startup
translator = pipeline("translation", model=TRANSLATION_MODEL, device=device)

def translate_text(text, target_lang="hi"):
    """
    Translate text to the target language.
    """
    # Adjust the prefix for target language if model is multilingual
    if target_lang != "en":
        text = f">>{target_lang}<< {text}"

    result = translator(text)
    return result[0]['translation_text']
