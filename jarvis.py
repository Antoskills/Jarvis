# speak functions 
# :- how to use voices

from time import time
import pyttsx3
 #pip install pyttsx3
import speech_recognition as sr 
#pip install speechRecognition
from playsound import playsound
from pywikihow import search_wikihow





engine = pyttsx3.init('sapi5')
voices =engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
engine.setProperty('rate',180)


def speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
        query = query.lower()
    return query

def TaskExe():

    while True:

        query = takeCommand()

        if 'youtube search'in query:
            Query = query.replace("jarvis",'')
            query = Query.replace("Youtube search","")
            from features import YouTubeSearch
            YouTubeSearch(query)

        elif '' in query:
                


