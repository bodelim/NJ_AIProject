from speech_recognition import *
import pyaudio

r = Recognizer()
mic = Microphone()

with mic as source:
    audio = r.listen(source)

voice_data = r.recognize_google(audio, language= 'ko')
print(voice_data)