import pyttsx3
import datetime
# import time
import speech_recognition as sr

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate=170
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("current time is")
    speak(Time)

def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)

def greet():
    speak("Welcome back Akanksha")
    # date()
    # time()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak('Good morning')
    elif hour>=12 and hour<18:
        speak('Good afternoon')
    elif hour>=18 and hour<=24:
        speak('Good evening')
    else:
        speak('Good night')
    speak("How can i help you?")

def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...",end=" ",flush=True)
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("\nRecognizing...")
        query=r.recognize_google(audio)
        # query=r.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return(query)


if __name__=="__main__":
    greet()
    while(True):
        query=take().lower()
        # print(query)
        

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
# take()
# greet()
# date()
# speak("Good evening akanksha")
# time()