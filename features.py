import pywhatkit
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web  
import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)




def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    speak("sir this is what i found for your youtube search .")

    pywhatkit.playonyt(term)

    speak("this may also help you sir .")

def Alarm(query):

    TimeHere =open('C:\\Users\\asus\\Desktop\\HOW TO MAKE JARVIS\\Data.txt')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("")

Alarm("set alarm for 16:38")






