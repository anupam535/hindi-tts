import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEFAULT_VOICE_MODEL = os.getenv("DEFAULT_VOICE_MODEL", "default")
    DEFAULT_EMOTION = os.getenv("DEFAULT_EMOTION", "neutral")
    DEFAULT_SPEED = float(os.getenv("DEFAULT_SPEED", 1.0))
    DEFAULT_PITCH = float(os.getenv("DEFAULT_PITCH", 1.0))
