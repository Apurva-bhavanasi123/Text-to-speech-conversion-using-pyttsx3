# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:12:54 2019

@author: Apoorva
"""

import os
import pyttsx3
import datetime
import random
import smtplib
import sys
import speech_recognition as sr
import wolframalpha
import webbrowser 
import wikipedia

engine=pyttsx3.init()
engine.say("Hello I am your personal assistant scooobi, at your service")
engine.runAndWait()
voices=engine.getProperty('voices')
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9) 
client=wolframalpha.Client('app id')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

def speak(audio):
    print("scoobi:" +audio)
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    current=int(datetime.datetime.now().hour)
    if(current>=0 and current<12):
        speak("Good Morning")
    elif(current>=12 and current<18):
        speak("good afternoon")
    elif(current>=18 and current<20):
        speak("Good evening")
    else:
        speak("Ohh It's already night")

greetMe()
speak("helloo Welcome what is your command")
def mycommand():
    r=sr.Recognizer()
    try:
        
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1
            audio=r.listen(source)
        query=r.recognize_google(audio,language='en-in')
        print('User :'+query)
    except Exception:
        speak('Sorry I am not able to recognize your voice')
        query=input('command:')
    return query
if __name__ == '__main__':
    while(True):
        query=mycommand()
        query=query.lower()
        if ('open youtube ' in query):
            webbrowser.open('www.youtube.com')
        elif('open google' in query):
            webbrowser.open('www.google.com')
        elif('open gmail' in query):
            webbrowser.open('www.gmail.com')
        elif(" what's up" in query or 'how are you' in query):
            msgs=['GOOD','Just doing my thing','I am fine','I am full of energy']
            speak(random.choice(msgs))
        elif 'email' in query:
            speak('who is recipient')
            recipient=mycommand()
            if ('me' in recipient):
                try:
                    #inorder to do this you need to change settings in mail ,allow to signin using low security apps
                    speak("what should it say")
                    content=mycommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("mail", 'password')
                    server.sendmail('sender', "receiver", content)
                    server.close()
                    speak('Email sent!')
                except Exception:
                    speak("Some error occured")
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except Exception:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
                    
        
            except Exception:
               # webbrowser.open('www.google.com')
                webbrowser.open(query)
               # speak(wikipedia.summary(query,sentences=2))
        
        speak('Next Command! Sir!')
            
            
                
        
    
