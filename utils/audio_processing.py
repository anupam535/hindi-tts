import soundfile as sf

def save_audio(waveform, output_path, output_format="mp3"):
    """
    Save waveform as MP3 or WAV.
    :param waveform: Generated waveform
    :param output_path: Output file path
    :param output_format: Output audio format (mp3/wav)
    """
    if output_format == "mp3":
        sf.write(output_path, waveform.numpy(), samplerate=22050, format='mp3')
    elif output_format == "wav":
        sf.write(output_path, waveform.numpy(), samplerate=22050, format='wav')
    else:
        raise ValueError("Unsupported audio format")
