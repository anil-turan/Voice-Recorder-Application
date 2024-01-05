import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration, file_name):
    print("Recording started...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()
    write(file_name, 44100, audio)
    print(f"Recording complete! File name: {file_name}")

if __name__ == "__main__":
    recording_duration = float(input("Enter the recording duration in seconds: "))
    file_name = input("Enter the file name to save (e.g., recording.wav): ")
    record_audio(recording_duration, file_name)