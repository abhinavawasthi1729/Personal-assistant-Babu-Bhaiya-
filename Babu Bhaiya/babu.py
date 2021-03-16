import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Abhinav ")
    elif hour>=12 and hour<18:
        speak("Good afternoon Abhinav ")
    else:
        speak("Good evening Abhinav")

    speak ("What should I do now")



def takeCommand():
    #take input from microphone and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
     
    try:
         print("Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(f"User said : {query}\n") 
        
    except Exception as e:
        #print(e)
        print("Say that again plz...")
        return "None"

    return query 


if __name__=="__main__":
    wishMe()
    

    

    while True:
            query=takeCommand().lower()

            #executing task based on query
        
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query=query.replace('wikipedia','')
                results=wikipedia.summary(query,sentences=1)
                speak('According to Wikipedia')
                print(results)
                speak(results)
            

            elif 'open youtube' in query:
                #webbrowser.open('youtube.com')
                webbrowser.get('chrome').open('youtube.com')

            
            elif 'open google' in query:
                #webbrowser.open('google.com')
                webbrowser.get('chrome').open('google.com')
            
            elif 'open gaana.com' in query:
                webbrowser.get('chrome').open('gaana.com')


            elif 'play music' in query:
                 music_dir='F:\\music\\mp3'
                 songs=os.listdir(music_dir)
                 #print(songs)
                 #os.startfile(os.path.join(music_dir,songs[0]))
                 os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

            
            elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Abhinav, the time is {strTime}")

            
            elif 'open code' in query:
                codePath="C:\\Users\\ABHINAV AWASTHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open zoom' in query:
                zoomPath="C:\\Users\\ABHINAV AWASTHI\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                os.startfile(zoomPath)