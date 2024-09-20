import speech_recognition as sr
import pyttsx3


def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate',120)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
    
if __name__ == "__main__":
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        voice = listener.listen(source)
    command = listener.recognize_google(voice)
    print(speak(command))
