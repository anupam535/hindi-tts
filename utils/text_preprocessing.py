import re

def preprocess_hindi_text(text):
    """
    Preprocess Hindi text for TTS.
    :param text: Input Hindi text
    :return: Processed text
    """
    # Normalize Unicode characters
    text = text.strip()

    # Handle borrowed English terms
    text = re.sub(r'\b([A-Za-z]+)\b', lambda x: x.group(1).lower(), text)

    # Add pauses for punctuation
    text = re.sub(r'[.,!?]', r' \g<0> ', text)

    return text
