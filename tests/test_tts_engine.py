import unittest
from core.tts_engine import TTSEngine
from utils.config import Config

class TestTTSEngine(unittest.TestCase):
    def setUp(self):
        self.tts_engine = TTSEngine(
            voice_model=Config.DEFAULT_VOICE_MODEL,
            emotion=Config.DEFAULT_EMOTION,
            speed=Config.DEFAULT_SPEED,
            pitch=Config.DEFAULT_PITCH
        )

    def test_generate_speech(self):
        text = "नमस्ते दुनिया"
        output_format = "mp3"
        audio_path = self.tts_engine.generate_speech(text, output_format)
        self.assertTrue(os.path.exists(audio_path))

if __name__ == '__main__':
    unittest.main()
