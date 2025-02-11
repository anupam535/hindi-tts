import torch
from models.fastspeech2 import FastSpeech2
from models.wavenet import WaveNet
from utils.text_preprocessing import preprocess_hindi_text
from utils.audio_processing import save_audio
from utils.config import Config

class TTSEngine:
    def __init__(self, 
                 voice_model=Config.DEFAULT_VOICE_MODEL, 
                 emotion=Config.DEFAULT_EMOTION, 
                 speed=Config.DEFAULT_SPEED, 
                 pitch=Config.DEFAULT_PITCH):
        """
        Initializes the TTS Engine with specified parameters.

        Args:
            voice_model: Path to the voice model checkpoint.
            emotion: Emotion level for speech synthesis.
            speed: Speech speed factor.
            pitch: Pitch factor for speech synthesis.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
        self.fastspeech2 = FastSpeech2(device=self.device).to(self.device)
        self.fastspeech2.load_state_dict(torch.load(voice_model, map_location=self.device)) 
        self.wavenet = WaveNet(device=self.device).to(self.device)
        self.wavenet.load_state_dict(torch.load(Config.WAVENET_MODEL_PATH, map_location=self.device)) 
        self.emotion = emotion
        self.speed = speed
        self.pitch = pitch

    def generate_speech(self, text, output_format="mp3"):
        """
        Generates speech from input text.

        Args:
            text: Input Hindi text.
            output_format: Output audio format (mp3/wav).

        Returns:
            Path to generated audio file.
        """
        try:
            processed_text = preprocess_hindi_text(text)
            mel_spec = self.fastspeech2.generate_mel(processed_text, 
                                                   emotion=self.emotion, 
                                                   speed=self.speed, 
                                                   pitch=self.pitch)
            waveform = self.wavenet.generate_waveform(mel_spec)
            output_path = f"output/audio_{hash(text)}_{os.getpid()}.{output_format}" 
            save_audio(waveform, output_path, output_format)
            return output_path
        except Exception as e:
            print(f"Error generating speech: {e}")
            return None
