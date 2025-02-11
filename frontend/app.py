from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    voice_model = request.form['voice_model']
    emotion = request.form['emotion']
    speed = float(request.form['speed'])
    pitch = float(request.form['pitch'])

    # Call TTS engine
    tts_engine = TTSEngine(voice_model=voice_model, emotion=emotion, speed=speed, pitch=pitch)
    audio_path = tts_engine.generate_speech(text, output_format="mp3")

    return send_file(audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
