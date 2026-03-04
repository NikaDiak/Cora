import pyaudio
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os


# import numpy

engine = pyttsx3.init()
engine.setProperty("rate", 180)
def speak(text):
    print(f"assistant: {text}")
    engine.say(text)
    engine.runAndWait()

speak("I'm cora and ready to help you")

voice_recognize= sr.Recognizer()
with sr.Microphone() as source:
    print("Speak")
    audio=voice_recognize.listen(source, timeout=5, phrase_time_limit=10)
txt = voice_recognize.recognize_google(audio, language="ru")
print(txt)

if "Википедия" in txt:
    webbrowser.open('https://wikipedia.org')
    speak("I'm opening wikipedia")
if 'Валик' in txt:
    os.startfile("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
    speak("I'm opening valorant")