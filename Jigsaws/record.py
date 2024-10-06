import pyaudio
import wave
from pydub import AudioSegment
from pathlib import Path
from typing import Optional

def record_audio(output_path: Path, duration: int = 5, sample_rate: int = 44100, channels: int = 1, chunk: int = 1024) -> None:
    """
    Record audio using PyAudio and save it as an MP3 file.

    Args:
        output_path (Path): The path where the MP3 file will be saved.
        duration (int): The duration of the recording in seconds. Defaults to 5.
        sample_rate (int): The sample rate of the audio. Defaults to 44100.
        channels (int): The number of audio channels. Defaults to 2 (stereo).
        chunk (int): The number of frames per buffer. Defaults to 1024.
    """
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save as WAV first
    temp_wav = output_path.with_suffix('.wav')
    wf = wave.open(str(temp_wav), 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert WAV to MP3
    audio = AudioSegment.from_wav(str(temp_wav))
    audio.export(str(output_path), format="mp3")

    # Remove temporary WAV file
    temp_wav.unlink()

    print(f"Audio saved as {output_path}")

def main() -> None:
    output_path = Path("recorded_audio.mp3")
    record_audio(output_path)

if __name__ == "__main__":
    main()
