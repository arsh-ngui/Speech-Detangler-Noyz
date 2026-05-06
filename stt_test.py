import whisper

# load model
model = whisper.load_model("small")

# transcribe audio
result = model.transcribe("test.wav")

print(result["text"])