from dataclasses import replace
from datetime import datetime
from email.mime import audio
from logging import exception
from unittest import result
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your robot sir. Please tell me how can i help you")
def takecommand():
    '''
    
    '''
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language="eng-in")
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)

        print("say that again please....")
        return "None"
        return query
if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()

         #logic for exculting tasks basesd on query
        if 'wikipedia' in query:
           speak('Searching wikipedia..')
           query = query.replace('wikipedia','')
           results = wikipedia.summary(query, sentence=2)
           speak('According to wikipedia')
           print(results)
           speak(results)