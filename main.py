from vosk import Model, KaldiRecognizer
import os
import pyaudio
import datetime
from datetime import date
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

def initial():
    print('listening...')
    speak('hi are you doing fine')
    while True:
        data = stream.read(8000)
        if len(data) == 0:
            print('returned')
            break
        if rec.AcceptWaveform(data):
            text = rec.Result()
            text = json.loads(text)

            print(text['text'])
            if text['text'] == 'yes' or text['text'] == 'yeah':
                #print('yes')
                speak('i hoped so this made my day')
                return
            elif text['text'] == 'no' or text['text'] == 'nah':
                speak('what i can do to lighten your mood')
                return
            else:
                speak('sorry i could not understand')

while True:
    #print('listening...')
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):

        text = rec.Result()
        text = json.loads(text)
        print(text['text'])
        if text['text'] == 'jarvis' or text['text']=='hi jarvis' or text['text']=='hello jarvis' :
            print(text['text'])
            break

initial()
while True:

    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):

        text = rec.Result()
        text = json.loads(text)
        print(text['text'])
        speak(text['text'])
        command = text['text']
        if 'time' in text['text']:
            cur_time = datetime.datetime.now().strftime('%I:%M %p')
            print(cur_time)
            speak('time now is' + cur_time)
            continue
        if 'date' in text['text']:
            cur_date = date.today()
            print(cur_date)
            speak(cur_date)
            continue
        if 'thank you' in command:
            speak('you are welcome')
            continue
        if 'switch off' or 'stop' or 'exit' in command:
            break

