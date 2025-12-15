from faster_whisper import WhisperModel

model = WhisperModel("tiny.en", device="cpu", compute_type="int8")

segments, info = model.transcribe("test.m4a")
def answer():
    for segment in segments:
        print(segment.text)

answer()
