import telebot
from core.tts_engine import TTSEngine
from hindi_tts_app.core.tts_engine import TTSEngine
from utils.config import Config
import os

bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)
tts_engine = TTSEngine()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Hindi TTS Bot! Send me some text to convert it to speech.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    audio_path = tts_engine.generate_speech(text, output_format="mp3")

    if audio_path: 
        with open(audio_path, 'rb') as audio_file:
            bot.send_voice(message.chat.id, audio_file)
    else:
        bot.reply_to(message, "Error generating speech. Please try again.")

if __name__ == '__main__':
    bot.polling()
