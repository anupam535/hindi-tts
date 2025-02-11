import torch
from models.fastspeech2 import FastSpeech2
from models.wavenet import WaveNet
from utils.text_preprocessing import preprocess_hindi_text
from utils.audio_processing import save_audio
from utils.config import Config

class TTSEngine:
    def __init__(self, voice_model=Config.DEFAULT_VOICE_MODEL, emotion=Config.DEFAULT_EMOTION, speed=Config.DEFAULT_SPEED, pitch=Config.DEFAULT_PITCH):
        self.voice_model = voice_model
        self.emotion = emotion
        self.speed = speed
        self.pitch = pitch
        self.fastspeech2 = FastSpeech2()
        self.wavenet = WaveNet()

    def generate_speech(self, text, output_format="mp3"):
        """
        Generate speech from input text.
        :param text: Input Hindi text
        :param output_format: Output audio format (mp3/wav)
        :return: Path to generated audio file
        """
        # Preprocess text
        processed_text = preprocess_hindi_text(text)

        # Generate mel-spectrogram using FastSpeech2
        mel_spec = self.fastspeech2.generate_mel(processed_text, emotion=self.emotion, speed=self.speed, pitch=self.pitch)

        # Generate waveform using WaveNet
        waveform = self.wavenet.generate_waveform(mel_spec)

        # Save audio file
        output_path = f"output/audio.{output_format}"
        save_audio(waveform, output_path, output_format)
        return output_path
