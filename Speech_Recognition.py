import speech_recognition as sr
import pyaudio

listener = sr.Recognizer()

with sr.Microphone() as source:
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    print(command)