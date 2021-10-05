#working on pocketsphinx


# from pocketsphinx import LiveSpeech
# for phrase in LiveSpeech(): print(phrase)

import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
#creating recognizer

engine.say('How are you')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command1 = listener.recognize_sphinx(voice)
        print("sphinx:", command1)
        # if 'jarvis' in command:
        #     #engine.say(command)
        #     #engine
        #     print(command)
except:
    pass

