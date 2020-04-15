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
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Setting Voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = engine.setProperty('voice', voices[3])
# Setting Volume 
volume = engine.getProperty('volume')  
engine.setProperty('volume',1) 
#Setting rate
engine.setProperty('rate',180)   

master = "Angelina"
quit = False
exit_commands = ["quit", "stop", "I want to leave", "bye", "exit", "leave"]

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

def checkWikipedia(topic):
    results = wikipedia.summary(topic, sentences=2)
    speak(results)


greeting()
while(quit != True):
    query = takeCommand()
    print(query)
    for command in exit_commands:
        if command in query.lower():
            print("Goodbye " + master)
            speak("Goodbye " + master)
            quit = True
    if quit != True:
        if 'wikipedia' in query.lower():
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            checkWikipedia(query)
        elif 'time' in query.lower():
            sayTime()
        elif 'date' in query.lower():
            sayFullDate()
        elif 'what is' in query.lower():
            speak("Searching Wikipedia")
            query = query.replace('what is', '')
            checkWikipedia(query)
        elif 'what are' in query.lower():
            speak("Searching Wikipedia")
            query = query.replace('what are', '')
            checkWikipedia(query)
        elif 'open youtube' in query.lower() or 'open up youtube' in  query.lower():
            print("Opening Youtube...")
            webbrowser.get(chrome_path).open("http://youtube.com")
        elif 'open school tabs' in query.lower() or 'open up school tabs' in query.lower():
            webbrowser.get(chrome_path).open("https://docs.google.com/spreadsheets/d/1DOGhlYhpY8onx8mgolAUQGntmOXbwJNbwdaYZXq0txs/edit#gid=1691470956")
            webbrowser.get(chrome_path).open("https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/5eb55a21-9496-46ce-8161-f092fc9def23/chadwick/Middle%20School%20Distance%20Learning%20Schedule.pdf")
            webbrowser.get(chrome_path).open("https://classroom.google.com/u/0/h")
        else:
            speak("Sorry, I didn't understand that")

    
