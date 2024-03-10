import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui

engine = pyttsx3.init('sapi5')                 #SAPI5 MICROSOFT SPEACH API
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!!")
    
    else:
        speak("Good Evening!!")

    speak("I am Pragati , your AI assistant, how may i help you")

def takeCommand():
    #Takes microphonic input from the user and converts it into string format

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic to Execute task based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'search' in query:
            query=query.replace("search","")
            string = query.split()
            result = " "
            for i in string:
                result += i

                result +="+"
            webbrowser.open(f"https://www.google.com/search?q={result}")

        elif 'name' in query or 'about' in query:
            speak("Hii my name is David , i am a AI based Virtual Voice Assistant capable of performing all your daily task !!!!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'time' in query:
            strtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtTime}")
        
        elif 'date' in query:
            strtDate = datetime.datetime.now().strftime("%D:%M:%Y")
            speak(f"The date is {strtDate}")
        
        elif 'up' in query or 'increase' in query:
            pyautogui.press("volumeup")
        
        elif 'down' in query or 'decrease' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'play' in query:
            query=query.replace("play","")
            string = query.split()
            search = " "
            for i in string:
                search += i

                search +="+"
            speak(f"playing...{search}")
            pywhatkit.playonyt(search)
            # webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

        elif 'temperature' in query:
            search = "temperature in chennai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current {search} is {temp}")
        
        elif 'screenshot' in query:
            im = pyautogui.screenshot()
            speak("taking screenshot")
            im.save("ss.jpg")
        
        elif 'picture' in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("smile")
            pyautogui.press("enter")

        
        elif 'quit' in query or 'exit' in query:
            speak("Have a Nice day !!")
            exit()