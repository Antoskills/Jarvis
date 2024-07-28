from operator import imod
import queue
from time import time
from winreg import QueryInfoKey
from click import command
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from playsound import playsound
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from keyboard import write
from keyboard import press
from keyboard import press_and_release
import requests
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

def Pass(pass_inp):

    password = "python"

    passss =str(password)

    if passss==str(pass_inp):

            speak("Access Granted.") 


    else:
        speak("Access Not Granted")

if __name__ == "__main__":


    speak("this file is password protected.")

    speak ('kindly provide password')

    passsssss = takeCommand()

    Pass(passsssss)









