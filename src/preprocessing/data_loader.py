import os
import pandas as pd
import librosa
from pydub import AudioSegment

class DataLoader:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_audio(self, file_path, target_sr=22050):
        y, sr = librosa.load(file_path, sr=target_sr)
        return y, sr

    def save_audio(self, audio, output_path, sr=22050):
        librosa.output.write_wav(output_path, audio, sr)

    def preprocess_audio(self, input_dir, output_dir, target_sr=22050):
        os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(input_dir):
            if filename.endswith('.wav'):
                file_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)
                audio, sr = self.load_audio(file_path, target_sr)
                self.save_audio(audio, output_path, sr)
                print(f"Processed {filename}")

# Example usage
if __name__ == "__main__":
    data_loader = DataLoader(data_dir='data/raw/delhi')
    data_loader.preprocess_audio(input_dir='data/raw/delhi', output_dir='data/processed/delhi')
