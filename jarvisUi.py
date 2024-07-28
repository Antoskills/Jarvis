from time import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from playsound import playsound
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
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


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

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

def temp():
    search = "temperature"
    url = f"https://www.google.com/search?q= {search}" 
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature =data.find("div", class_ = "BNeawe").text
    speak(f"the temperature outside Is {temperature}")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def TaskExecution():
    wishMe()
    while True:
        query =takeCommand()

        #LOGIC BUILDING FOR TASK

        if ' open notepad' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe"
            os.startfile(npath)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube....")

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google....")

        elif 'play music' in query:
            music_dir ="F:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\PyScripter\\PyScripter.exe"
            os.startfile(codePath)

        elif 'alarm' in query:
            speak("what time must i set?")
            time =input("...enter the time...")   

            while True:
                time_Ac = datetime.datetime.now()
                now = time_Ac.strftime("%H :%M :%S")

                if now == time:
                    speak("time to wake up sir!")
                    playsound("F:\\music\\iron.mp3")
                    speak("alarm closed!")

                elif now>time:
                        break

        elif 'sleep' in query:
            speak('thank you very much,have a very wonderful day')

            break

        elif 'how to' in query:
            speak("getting data from internet!") 
            op =query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len (how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'temperature' in query:
            temp()    
            
        elif 'email to ANTO' in query:

            try:
                speak("What should I say?")
                content = takeCommand()
                to = "antogeorge00002@gmail.com","anto@2003"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend ANTO bhai. I am not able to send this email")

if __name__ == "__main__":
    while True:
        permission  = takeCommand()
        if "wake up" in permission:
            speak("waking up....")
            TaskExecution()

        elif "goodbye" in permission:
            speak("thanks for using me !")
            sys.exit()

     

