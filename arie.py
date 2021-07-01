import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import pyjokes
import datetime
import webbrowser
import subprocess
import os
import wx


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('rate',175)
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command.lower()
            if 'alexa' in command:

                command=command.replace('alexa','')
                print(command)
        except:
            pass
        return command
def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
         time=datetime.datetime.now().strftime('%H:%M %P')
         
         talk("It's is"+time) 
    elif 'how are you' in command:
        talk("I am doing fine,how about you?")
    elif command=='thank you':
        talk('you\'re welcome')
    elif 'who is' or 'what is' in command:
        person=command.replace('who is'or'what is','')
        answer=wikipedia.summary(person,2)
        talk(answer)
        print(answer)
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open notepad' or 'Open Notepad'in command:
        talk('opening notepad')
        os.system('Notepad')
    else:
        talk('Sorry can you please say it again')
    
    
while True:
    run_alexa()