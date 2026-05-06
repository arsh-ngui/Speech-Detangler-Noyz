# import sounddevice as sd
# from scipy.io.wavfile import write
# import whisper

# # Recording settings
# fs = 16000
# duration = 5  # seconds

# print("Recording...")
# audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
# sd.wait()

# # Save temporary file
# write("temp.wav", fs, audio)

# print("Transcribing...")

# # Load model
# model = whisper.load_model("base")

# # Transcribe
# result = model.transcribe("temp.wav", fp16=False)

# print("Transcription:")
# print(result["text"])

import sounddevice as sd
from scipy.io.wavfile import write
import whisper

# Recording settings
fs = 16000
duration = 5  # seconds

print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

# Save audio
write("temp.wav", fs, audio)

print("Transcribing...")

# Load model
model = whisper.load_model("small")  

# Transcribe (ENGLISH)
result = model.transcribe(
    "temp.wav",
    fp16=False,
    language="en",      
    task="transcribe"   
)

print("Transcription:")
print(result["text"])