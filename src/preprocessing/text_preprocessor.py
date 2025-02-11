import re
import unicodedata

class TextPreprocessor:
    def __init__(self):
        pass

    def normalize_text(self, text):
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        # Normalize Unicode characters
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
        # Convert to lowercase
        text = text.lower()
        return text

# Example usage
if __name__ == "__main__":
    text_preprocessor = TextPreprocessor()
    text = "नमस्ते, आपका स्वागत है! Welcome to our app."
    normalized_text = text_preprocessor.normalize_text(text)
    print(normalized_text)
