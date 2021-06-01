import pyttsx3 
import datetime
# import time
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # to search on wikipedia
import smtplib,ssl #to send email
import webbrowser as wb #used for chrome search- or an browser search
import os
import pyautogui #to take screenshot
import psutil # used to get cpu and battery usage
import pyjokes #to tell jokes

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

def sendmail(to,content):
    # context=ssl.create_default_context()
    server=smtplib.SMTP("smtp.gmail.com",587)#port no os 587
    # server.connect("smtp.gmail.com",465)
    server.ehlo # these 2 lines are used to check the 
    server.starttls() # connection with the SMTP server
    server.login("<sender's email>","<sender's password>")
    server.sendmail("sender's email",to,content)
    server.close()

def screenshot(x):
    img=pyautogui.screenshot()
    img.save("D:\python\AI assistant\screenshots\\"+x+".png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)

    battery=psutil.sensors_battery()
    speak("battery is at "+str(battery.percent)+"%")
    # speak(battery.percent)
    # print(battery)

def jokes():
    speak(pyjokes.get_joke())


if __name__=="__main__":
    os.system('cls')
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
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say?")
                content=take()
                to="reciever's email"
                sendmail(to,content)
                speak("mail sent successfully")
            except Exception as e:
                print(e)
                speak("some error occured , unable to send email")
        elif "chrome" in query :
            speak("What do you want me to search?")
            # wb.register('chrome', None)
            # wb.open(take().lower())
            #*************************
            search=take().lower() 
            chromepath= ' "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s'  
            print(search)
            wb.get(chromepath).open(search+".com")     
            # wb.get("google-chrome").open_new_tab(search+".com")     
            # wb.open("www.google.com")
            #*************************
            # chromepath="‪C://Program Files (x86)//Google//Chrome//Application//chrome.exe"  
            # urL='https://www.google.com'
            # wb.register('chrome',None,wb.BackgroundBrowser(chromepath))
            # wb.get('chrome').open(urL)
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "song" in query:
            # song_dir:"D:\python\AI assistant\music"
            songs=os.listdir("D:\python\AI assistant\music")
            print(songs)
            os.startfile(os.path.join("D:\python\AI assistant\music",songs[0]))
            break

        elif "remember something" in query:
            speak("what should i remember?")
            data=take()
            speak("you said me to remember "+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "remember anything" in query:
            remember=open("data.txt","r")
            speak("you asked me to remember that"+remember.read())
            remember.close()

        elif "screenshot" in query:
            speak("what is the named you want the screenshot to be saved with?")
            x=take()
            screenshot(x)
            speak("screenshot taken.")

        elif "battery" in query:
            cpu()

        elif "joke" in query:
            jokes()

# take()
# greet()
# date()
# speak("Good evening akanksha")
# time()