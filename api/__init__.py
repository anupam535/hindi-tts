from flask import Flask
from .tts_api import tts_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tts_bp, url_prefix='/api')
    return app
