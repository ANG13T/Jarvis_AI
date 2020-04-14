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
engine.setProperty('volume',0.5)    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sayFullDate():
    today = date.today()
    now = today.strftime("%B %d, %Y")
    now = now.split()
    print(now)
    print(now[2][:2])
    engine.say("Today is " + str(now[0]) + str(now[1]) + str(now[2][:2]) + " " + str(now[2][2:]))
    engine.runAndWait()

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
        
    if int(min) < 10:
        print("here")
        engine.say("It is " + str(hour) + " o " + str(min))
    else:
        print("ceer")
        engine.say("It is " + str(hour) + " " + str(min))
    engine.runAndWait()

def getTimeIn(city):
    pass

sayTime()