from operator import imod
from time import time
from time import sleep
from winreg import QueryInfoKey
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from playsound import playsound
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from keyboard import write
from keyboard import press
from keyboard import press_and_release
from pyautogui import click
import webbrowser as web
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


def YoutubeAuto(command):

    query =str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')   

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press("t")

    elif "skip" in query:

        press('I')

    elif 'back' in query:

        press('j')    

    elif 'mute' in query:

        press("m")

    elif 'unmute' in query:

        press("m")

    elif 'my channel' in query:

        web.open("https://www.youtube.com/channel/UCBZhS1KlDYq0iG_yYRvqdrg")

    



