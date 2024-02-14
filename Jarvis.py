from __future__ import with_statement 
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk 
import os
import pyautogui
import time
import requests
import sys
import operator
from googletrans import Translator
from gtts import gTTS



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
 
    speak("Ready To Comply. What can I do for you ?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
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
        print("Say that again please...") 
        return "None"
    return query

if __name__ == "__main__":
    query = takeCommand().lower()
    wishMe()
    if 'jarvis' in query:
        print("Yes Ma'am")
        speak("Yes Ma'am")
    
    

    elif "who are you" in query:
        print('My Name Is JARVIS')
        speak('My Name Is JARVIS')
        print('I can Do Everything that my creator programmed me to do')
        speak('I can Do Everything that my creator programmed me to do')
    elif "who created you" in query:
        print('Sonali Verma is the developer, I am created with Python Language, in Visual Studio Code.')
        speak('Sonali Verma is the developer, I am created with Python Language, in Visual Studio Code.')
    elif "what is" in query:
        speak('searching wikipedia....')
        query=query.replace("what is","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif "channel analytics" in query:
 
        webbrowser.open("https://studio.youtube.com/channel/UCxeYbp9rU_HuIwVcuHvK0pw/analytics/tab-overview/period-default")
    elif "who is" in query:
        speak('searching wikipedia....')
        query=query.replace("who is","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'search on youtube' in query:
        query = query.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?search_query={query}")
    


    elif 'just open google' in query:
        webbrowser.open('google.com')
        
    elif 'open google' in query:
        speak("what should I search ?")
        qry = takeCommand().lower()
        webbrowser.open(f"{qry}")
        results = wikipedia.summary(qry, sentences=2)
        speak(results)
    elif 'search on youtube' in query:
        query = query.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?search_query={query}")
    elif 'open youtube' in query:
       
        speak("what you will like to watch ?")
        qrry = takeCommand().lower()
        wk.playonyt(f"{qrry}")
    elif 'close youtube' in query:
        os.system("taskkill /f /im msedge.exe")
    elif 'close browser' in query:
        os.system("taskkill /f /im msedge.exe")
    elif 'placement kab lagegi' in query:
        print(" Iska to bhagwan hi malik hai")
        speak(" Iska to bhawan hi malik hai")
    elif 'kya mam hamen project ke pure number denge' in query:
        print('bilkul maam bhot pyari hai project ke pure number dengi')
        speak('bilkul maam bhot pyari hai project ke pure number dengi')
    elif 'kya mam hamen project ke pure number dengi' in query:
        print('bilkul maam bhot pyari hai project ke pure number dengi')
        speak('bilkul maam bhot pyari hai project ke pure number dengi')
    elif 'kya sir hamen project ke pure number denge' in query:
        print('bilkul sir bhot ache hai project ke pure number denge')
        speak('bilkul sir bhot ache hai project ke pure number denge')

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"Ma'am, the time is {strTime}")
    
    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")
    elif "Lock the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    elif "open notepad" in query:
        npath = "C:\WINDOWS\system32\\notepad.exe" 
        os.startfile(npath)
    elif "close notepad" in query:
        os.system("taskkill /f /im notepad.exe")
    
    elif "open notepad and write my  name" in query:
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.write('notepad')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("Sonali Verma", interval = 0.1)
    elif "subscribe" in query: 
        print("Please Give us full amrks in mini project")
 
    elif 'type' in query: #10
        query = query.replace("type", "")
        pyautogui.write(f"{query}")  
    
    
 
    elif 'open browser' in query:
        os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    
    elif 'maximize this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
   
    elif 'google search' in query:
        query = query.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
   
    elif 'youtube search' in query:
        query = query.replace("youtube search", "")
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    
    elif 'open new window' in query:
        pyautogui.hotkey('ctrl', 'n')                           


    
    elif 'open incognito window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')
    
    elif 'minimise this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
    
    elif 'open history' in query:
        pyautogui.hotkey('ctrl', 'h')
    
    elif 'open downloads' in query:
        pyautogui.hotkey('ctrl', 'j')
    
    elif 'previous tab' in query:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    
    elif 'next tab' in query:
        pyautogui.hotkey('ctrl', 'tab')
   
    elif 'close tab' in query:
        pyautogui.hotkey('ctrl', 'w')
    elif 'close window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'w')
    elif 'clear browsing history' in query:
        pyautogui.hotkey('ctrl', 'shift', 'delete')
    elif 'close chrome' in query:
        os.system("taskkill /f /im msedge.exe")
    elif "tell me my ip address" in query:
     speak("Checking")
     try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        speak("your ip adress is")
        speak(ipAdd)
     except Exception as e:
        speak("network is weak, please try again some time later")

    elif "take screenshot" in query:
        speak('tell me a name for the file')
        name = takeCommand().lower()
        time.sleep(3)
        img = pyautogui.screenshot() 
        img.save(f"{name}.png") 
        speak("screenshot saved")
   


    
