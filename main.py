from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyttsx3

model = Model("model")
rec = KaldiRecognizer(model, 16000)
# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak('on')
print('listening...')
while True:

    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):

        text = rec.Result()
        text = json.loads(text)
        print(text['text'])
        speak(text['text'])

