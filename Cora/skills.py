from assistant import get_transcribe
from assistant import speak
import webbrowser
import os

result = get_transcribe()["text"]
print(result)

if 'открой Википедию' in result or 'открой википедию' in result or 'Открой Википедию' in result or 'Открой википедию' in result:
    webbrowser.open('https://wikipedia.org')
    speak("I'm opening wikipedia")

if 'открой Валик' in result or 'открой валик' in result or 'Открой Валик' in result or 'Открой валик' in result:
   os.startfile("C:\\Riot Games\\Riot Client\\VALORANT.lnk")
   speak("I'm opening valorant")

if 'открой Лол' in result or 'открой лол' in result or 'Открой лол' in result or 'Открой Лол' in result:
   os.startfile("C:\\Riot Games\\Riot Client\\League of Legends.lnk")
   speak("I'm opening LOL")

if 'открой сериал' in result or 'открой Сериал' in result or 'Открой сериал' in result or 'Открой Сериал' in result:
   webbrowser.open('https://ljucifer.lordfilm5.art/')
   speak("I'm opening series")





















