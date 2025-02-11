from flask import Flask, request, jsonify
from core.tts_engine import TTSEngine
from utils.config import Config

app = Flask(__name__)
tts_engine = TTSEngine()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get("text")
    voice_model = data.get("voice_model", Config.DEFAULT_VOICE_MODEL)
    emotion = data.get("emotion", Config.DEFAULT_EMOTION)
    speed = data.get("speed", Config.DEFAULT_SPEED)
    pitch = data.get("pitch", Config.DEFAULT_PITCH)
    output_format = data.get("output_format", "mp3")

    # Generate speech
    tts_engine.voice_model = voice_model
    tts_engine.emotion = emotion
    tts_engine.speed = speed
    tts_engine.pitch = pitch
    audio_path = tts_engine.generate_speech(text, output_format)

    return jsonify({"status": "success", "audio_url": audio_path})

if __name__ == '__main__':
    app.run(debug=True)
