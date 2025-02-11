from telebot import types
from core.tts_engine import TTSEngine
from utils.config import Config

tts_engine = TTSEngine()

def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to Hindi TTS Bot! Send me some text to convert it to speech.")

    @bot.message_handler(commands=['set_emotion'])
    def set_emotion(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        items = ['happy', 'sad', 'angry', 'suspenseful', 'narrator', 'neutral', 'professional']
        markup.add(*items)
        msg = bot.reply_to(message, 'Choose an emotion:', reply_markup=markup)
        bot.register_next_step_handler(msg, process_emotion_step)

    def process_emotion_step(message):
        try:
            chat_id = message.chat.id
            emotion = message.text
            tts_engine.emotion = emotion
            bot.send_message(chat_id, f'Emotion set to {emotion}.')
        except Exception as e:
            bot.reply_to(message, 'Oops! Something went wrong.')

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        text = message.text
        audio_path = tts_engine.generate_speech(text, output_format="mp3")

        with open(audio_path, 'rb') as audio_file:
            bot.send_voice(message.chat.id, audio_file)
