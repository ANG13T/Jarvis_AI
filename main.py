import pyttsx3
import speech_recognition as sr
import datetime
from datetime import datetime
from datetime import date
import wikipedia
import os
import webbrowser
import smtplib

print("This is wokring")
# Setting Voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = engine.setProperty('voice', voices[0])
# Setting Volume 
volume = engine.getProperty('volume')  
engine.setProperty('volume',1)   

master = "Angelina"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greeting():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning " + master + " what can I do for you?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + master + " what can I do for you?")
    else:
        speak("Good Evening " + master + " what can I do for you?")

    

def sayFullDate():
    today = date.today()
    now = today.strftime("%B %d, %Y")
    now = now.split()
    print(now)
    print(now[2][:2])
    speak("Today is " + str(now[0]) + str(now[1]) + str(now[2][:2]) + " " + str(now[2][2:]))
    

def sayTime():
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    dt = dt_string.split(':')
    print(dt)
    hour = dt[0]
    min  = dt[1]
    sec = dt[2]
    if int(hour) < 10:
        hour = hour[1]
    if int(hour) > 12:
        hour = int(hour) % 12

    if int(min) < 10:
        print("here")
        speak("It is " + str(hour) + " o " + str(min))
    else:
        print("ceer")
        speak("It is " + str(hour) + " " + str(min))

def getTimeIn(city):
    pass

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        return r.recognize_google(audio, language='en-in')
        print("You said : {}".format(query))
    except Exception as e:
        print("Say that again?")

greeting()
query = takeCommand()
print(query)

if 'wikipedia' in query or 'Wikipedia' in query:
    print("Ummmm")

if 'time' in query or 'Time' in query:
    sayTime()

if 'date' in query or 'Date' in query:
    sayFullDate()