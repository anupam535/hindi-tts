import unittest
from api import create_app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_generate_speech(self):
        response = self.app.post('/api/generate', json={
            "text": "नमस्ते दुनिया",
            "voice_model": "male",
            "emotion": "happy",
            "speed": 1.0,
            "pitch": 1.0,
            "output_format": "mp3"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("audio_url", data)

if __name__ == '__main__':
    unittest.main()
