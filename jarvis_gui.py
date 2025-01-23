# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:25:55 2020

@author: Ayush Garg
"""

import subprocess 
import wolframalpha 
import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import re
import urllib.request
import urllib.parse
import winshell 
import pyjokes  
import smtplib 
import ctypes 
import time 
import pyowm
import requests 
from tkinter import *
from ecapture import ecapture as ec 

window=Tk()
global var
global var1

var=StringVar()
var1=StringVar()
var0=StringVar()

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Initializing Jarvis.....\n")   
speak("Initializing Jarvis")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        var.set("Jarvis: Good Morning Sir. I am Jarvis. Your personal assistant.")
        window.update()
        print("Jarvis: Good Morning Sir")
        speak("Good Morning Sir")
    elif(hour>=12 and hour<18):
        var.set("Jarvis: Good Afternoon Sir. I am Jarvis. Your personal assistant.")
        window.update()
        print("Jarvis: Good Afternoon Sir")
        speak("Good Afternoon Sir")
    else:
        var.set("Jarvis: Good Evening Sir. I am Jarvis. Your personal assistant.")
        window.update()
        print("Jarvis: Good Evening Sir")
        speak("Good Evening Sir")
    print("        I am Jarvis. Your personal assistant.")
    speak("I am Jarvis. Your personel assistant.")    

def speak(audio): 
	engine.say(audio) 
	engine.runAndWait()
    	
def takeCommand():       
    r = sr.Recognizer()       
    with sr.Microphone() as source:
        var0.set("\nListening...")
        window.update()           
        print("\nListening...") 
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)    
    try: 
        var0.set("Recognizing...")
        window.update()           
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in')
        print("\nYou: "+query)    
    except Exception as e: 
        print(e)
        var.set("Jarvis: Unable to Recognize your voice.")
        window.update()
        print("Jarvis: Unable to Recognize your voice.")   
        speak("Unable to Recognize your voice.")
        return "None"
    var1.set("You: "+query)
    window.update()
    return query 

def sendEmail(to, content): 
	server = smtplib.SMTP('smtp.gmail.com', 587) 
	server.ehlo() 
	server.starttls() 	 
	server.login('Silentgirl0309@gmail.com', 'ayush1234a') 
	server.sendmail('Silentgirl0309@gmail.com', to, content) 
	server.close()
               
if __name__ == '__main__': 
    clear = lambda: os.system('cls') 

    clear()
    
    def play():
        btn2['state'] = 'active'
        btn0['state'] = 'disabled'
        btn1.configure(bg = 'orange')
        
        while True:
            btn1.configure(bg = 'orange')
            query = takeCommand().lower()
            if 'exit' in query or 'quit' in query:
                var.set("Jarvis: Thanks for giving me your time")
                btn1.configure(bg = '#5C85FB')
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                window.update()
                speak("Thanks for giving me your time")
                break

            elif 'wikipedia' in query: 
                speak('Searching Wikipedia...') 
                query = query.replace("wikipedia", "") 
                results = wikipedia.summary(query, sentences = 3) 
                speak("According to Wikipedia")
                var.set("\nJarvis: "+results)
                window.update()
                print("\nJarvis: "+results) 
                speak(results)
                break
    
            elif 'open google' in query: 
                var.set("Jarvis: Here you go to Google")
                window.update()
                print("Jarvis: Here you go to Google")
                speak("Here you go to Google\n")
                url="www.google.com"
                webbrowser.open(url)
                break
    
            elif 'open youtube' in query:
                var.set("Jarvis: Here you go to Youtube")
                window.update()
                print("Jarvis: Here you go to Youtube")
                speak("Here you go to Youtube")
                url="www.youtube.com"
                webbrowser.open(url)
                break
    
            elif 'open stackoverflow' in query:
                var.set("Jarvis: Here you go to Stack Over flow. Happy coding")
                window.update()
                print("Jarvis: Here you go to Stack Over flow. Happy coding")
                speak("Here you go to Stack Over flow. Happy coding")
                url="www.stackoverflow.com"
                webbrowser.open(url)
                break
    
            elif 'open geekforgeeks' in query or 'open gfg' in query:
                var.set("Jarvis: Here you go to GeekforGeeks. Happy coding")
                window.update()
                print("Jarvis: Here you go to GeekforGeeks. Happy coding")
                speak("Here you go to GeekforGeeks. Happy coding")
                url="www.geekforgeeks.org"
                webbrowser.open(url)
                break
    
            elif 'the time' in query: 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                var.set("Jarvis: The time is "+strTime)
                window.update()
                print("Jarvis: The time is "+strTime)
                speak("The time is "+strTime)
                break
            
            elif 'play music' in query or "play song" in query:
                var.set("Jarvis: Which song you wanna listen?")
                window.update()
                print("Jarvis: Which song you wanna listen?")
                speak("Which song you wanna listen")
                msg = takeCommand()
                while msg=="None":
                    msg= takeCommand()
                song = urllib.parse.urlencode({"search_query" : msg})
                result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
                url = "http://www.youtube.com/watch?v="+search_results[0]
                webbrowser.open(url)
                break
            
            elif 'joke' in query:
                joke=pyjokes.get_joke()
                var.set("Jarvis: "+joke)
                window.update()
                print("Jarvis: "+joke)
                speak(joke) 
                break
     
            elif 'news' in query:
                main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
                open_bbc_page = requests.get(main_url).json() 
                article = open_bbc_page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                print('Jarvis: Here are some headlines of the day.')
                speak('here are some headlines of the day') 
                print('''\n=============== NEWS HEADLINES ============'''+ '\n') 				                
                news_string='''\n=============== NEWS HEADLINES ============\n'''
                for i in range(len(results)):
                    news_string=news_string+"\n"+str(i+1)+") "+ results[i]
                    var.set(str(i+1)+") "+ results[i])
                    window.update()
                    print(i+1,end="")
                    print(") "+ results[i])
                    speak(i+1)
                    speak(results[i])
                var.set(news_string)
                window.update()
                break    
                    
            elif 'spell' in query:
                pos=query.index('spell')
                query=query[pos+6:]
                var.set("\nJarvis: "+query)
                window.update()
                print("\nJarvis: "+query) 
                speak(query)  
                break
    
            elif 'empty recycle bin' in query: 
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                var.set("Jarvis: Recycle Bin Recycled")
                window.update()
                print("Jarvis: Recycle Bin Recycled")
                speak("Recycle Bin Recycled") 
                break
                
            elif 'lock window' in query:
                var.set("Jarvis: locking the device.")
                window.update()
                print("Jarvis: locking the device.")
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation()
                break
     
            elif 'shutdown' in query: 
                var.set("Jarvis: Hold On a Sec! Your system is on its way to shut down.")
                window.update()
                print("Jarvis: Hold On a Sec! Your system is on its way to shut down.")
                speak("Hold On a Second! Your system is on its way to shut down") 
                subprocess.call(["shutdown", "/s"]) 
                break
                
            elif "restart" in query: 
                var.set("Jarvis: Hold On a Sec! Your system is Restarting.")
                window.update()
                print("Jarvis: Hold On a Sec! Your system is Restarting.")
                speak("Hold On a Second! Your system is Restarting") 
                subprocess.call(["shutdown", "/r"]) 
                break
			
            elif "hibernate" in query or "sleep" in query: 
                var.set("Jarvis: Hold On a Sec! Your system is on its way to sleep.")
                window.update()
                print("Jarvis: Hold On a Sec! Your system is on its way to sleep.")
                speak("Hold On a Second! Your system is on its way to sleep")
                subprocess.call(["shutdown", "/h"]) 
                break
    
            elif "log off" in query or "sign out" in query:
                var.set("Jarvis: Make sure all the application are closed before sign-out.You have 5 sec to do so.")
                window.update()
                print("Jarvis: Make sure all the application are closed before sign-out")
                print("        You have 5 sec to do so")
                speak("Make sure all the application are closed before sign-out") 
                speak("You have 5 seconds to do so")
                time.sleep(5) 
                subprocess.call(["shutdown", "/l"]) 
                break
                
            elif "camera" in query or "take a photo" in query:
                var.set("Jarvis: Say cheeze!")
                window.update()
                print("Jarvis: Say cheeze!")
                speak("Say cheeeeze")
                ec.capture(0, "Jarvis Camera ", "img.jpg") 
                break
            
            elif "write a note" in query:
                var.set("Jarvis: What should I write, sir?")
                window.update()
                print("Jarvis: What should I write, sir?")
                speak("What should i write, sir") 
                note = takeCommand()
                while note=="None":
                    note = takeCommand()
                file = open('jarvis.txt', 'w') 
                var.set("Jarvis: Sir, Should I include date and time?")
                window.update()
                print("Jarvis: Sir, Should I include date and time?")
                speak("Sir, Should i include date and time") 
                snfm = takeCommand()
                while snfm=="None":
                    snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm: 
                    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                    file.write(strTime) 
                    file.write(" :- \n") 
                    file.write(note) 
                else: 
                    file.write(note)
                var.set("Jarvis: Note made successfully!")
                window.update()
                print("Jarvis: Note made successfully!")
                speak("Note made successfully")
                break
		
            elif "show note" in query:
                var.set("Jarvis: Showing Notes")
                window.update()
                print("Jarvis: Showing Notes")
                speak("Showing Notes") 
                file = open("jarvis.txt", "r")
                print('''\n=============== JARVIS.TXT ============'''+ '\n')
                text=file.read()
                var.set('''\n=============== JARVIS.TXT ============\n'''+text)
                window.update()
                print(text) 
                speak(text) 
                break
                
            elif "where is" in query: 
                query = query.replace("where is", "") 
                location = query
                var.set("Jarvis: Locating" + location)
                window.update()
                print("Jarvis: Locating" + location)
                speak("Locating") 
                speak(location) 
                url = "https://www.google.com/maps/search/?api=1&query=" + location + ""
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(url)
                break
    
            elif 'send a mail' in query: 
                try:
                    var.set("Jarvis: Please provide recievers id.")
                    window.update()
                    print("Jarvis: Please provide recievers id.")
                    speak("Please provide recievers id") 
                    to = input("ENTER RECEIVERS EMAIL ID: ")	 
                    var.set("\nJarvis: What should I say?")
                    window.update()
                    print("\nJarvis: What should I say?")
                    speak("What should I say?") 
                    content = takeCommand()
                    while content=="None":
                        content = takeCommand()
                    sendEmail(to, content) 
                    var.set("Jarvis: Email has been sent succesfully!")
                    window.update()
                    print("Jarvis: Email has been sent succesfully!")
                    speak("Email has been sent succesfully") 
                except Exception as e: 
                    print(e)
                    var.set("Jarvis: I am not able to send this email")
                    window.update()
                    print("Jarvis: I am not able to send this email")
                    speak("I am not able to send this email") 
                break    
    
            elif "calculate" in query: 			
                app_id = "8REQUG-YQ7JGY96T8"
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text 
                var.set("Jarvis: The answer is " + answer)
                window.update()
                print("Jarvis: The answer is " + answer) 
                speak("The answer is " + answer) 
                break
    
            elif "word" in query:
                var.set("Jarvis: Opening Microsoft Word")
                window.update()
                print("Jarvis: Opening Microsoft Word")
                speak("Opening Microsoft Word") 
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\\Word 2016.lnk') 
                break
            
            elif "excel" in query:
                var.set("Jarvis: Opening Microsoft Excel")
                window.update()
                print("Jarvis: Opening Microsoft Excel")
                speak("Opening Microsoft Excel") 
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\\Excel 2016.lnk') 
                break
            
            elif "powerpoint" in query:
                var.set("Jarvis: Opening Microsoft PowerPoint")
                window.update()
                print("Jarvis: Opening Microsoft PowerPoint")
                speak("Opening Microsoft PowerPoint") 
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\\PowerPoint 2016.lnk') 
                break
            
            elif "what is" in query or "what are" in query:
                app_id = "8REQUG-YQ7JGY96T8" 			
                client = wolframalpha.Client(app_id) 
                res = client.query(query)
                msg = query.replace("what is", "")
                msg = query.replace("what are", "") 			
                try: 
                    var.set("Jarvis: " + msg + " is " + next(res.results).text)
                    window.update()
                    print ("Jarvis: " + msg + " is " + next(res.results).text) 
                    speak (msg + "is" + next(res.results).text) 
                except StopIteration: 
                    var.set("Jarvis: No results found.")
                    window.update()
                    print ("Jarvis: No results found.")
                    speak("No results found")
                break
            
            elif "weather" in query:
                print("Jarvis: Please tell me the city name") 
                speak("Please tell me the city name") 
                city_name = takeCommand() 
                while city_name=="None":
                    city_name = takeCommand()
                try:
                    owm=pyowm.OWM("dc753b67b9eea6d22aa6ef2b26fc0dfc")
                    location=owm.weather_at_place(city_name)
                    weather=location.get_weather()
                    temp=weather.get_temperature('celsius')
                    print('Jarvis: Here is the weather report.')
                    speak('Here is the weather report') 
                    weather_string=('''\n=============== WEATHER REPORT ============\n''')
                    for key,value in temp.items():
                        weather_string=weather_string+"\n"+key.upper()+"="+value+'degree C'
                        print(key.upper(),"=",value,'degree C')
                    wind=weather.get_wind()
                    for key,value in wind.items():
                        weather_string=weather_string+"\n"+key.upper()+"="+value
                        print(key.upper(),"=",value)                
                    humidity=weather.get_humidity()  
                    weather_string=weather_string+"\n"+'HUMIDITY ='+humidity+'%'
                    print('HUMIDITY =',humidity,'%') 
                    if temp['temp_max']>35:
                        print("\nJarvis: It's pretty hot outside, with a max temp of {} degrees C.Make sure to close your blinds to block out the heat!".format(temp['temp_max']))
                        speak("It's pretty hot outside, with a max temp of {} degrees Celsius...Make sure to close your blinds to block out the heat!".format(temp['temp_max']))
                    elif temp['temp_max']<18:
                        print("\nJarvis: It's pretty cold outside, with a min temp of {} degrees C, so you probably won't need the AC. Stay warm!".format(temp['temp_min']))
                        speak("It's pretty cold outside, with a min temp of {} degrees Celsius, so you probably won't need the AC... Stay warm!".format(temp['temp_min']))
                    else:
                        print("\nJarvis: The weather looks very pleasant, with a max temp of {} degrees C.".format(temp['temp_max']))
                        speak("The weather looks very pleasant, with a max temp of {} degrees Celsius.".format(temp['temp_max']))    
                    var.set(weather_string)
                    window.update()
                except:
                    var.set("\nJarvis: I couldn't fetch the weather data right now, sorry.. check the weather online.")
                    window.update()
                    print("\nJarvis: I couldn't fetch the weather data right now, sorry.. check the weather online.")
                    speak("I couldn't fetch the weather data right now, sorry.. check the weather online.")
                break
            
            elif 'change background' in query: 
                ctypes.windll.user32.SystemParametersInfoW(20,0,"C:\\Users\\Ayush Garg\\Pictures\\Saved Pictures",0)  
                var.set("Jarvis: Background changed succesfully.")
                window.update()
                print("Jarvis: Background changed succesfully.")
                speak("Background changed succesfully") 
                break
            
            elif 'how are you' in query:
                var.set("Jarvis: I am fine, Thank you.How are you, Sir?")
                window.update()
                print("Jarvis: I am fine, Thank you")
                speak("I am fine, Thank you")
                print("        How are you, Sir?")
                speak("How are you, Sir") 
                break
            
            elif 'fine' in query or "good" in query:
                var.set("Jarvis: It's good to know that your fine.")
                window.update()
                print("Jarvis: It's good to know that your fine.")
                speak("It's good to know that your fine") 
                break
            
            elif "what's your name" in query or "what is your name" in query: 
                var.set("My friends call me Jarvis") 
                window.update()
                speak("My friends call me Jarvis") 
                print("Jarvis: My friends call me Jarvis.") 
                break
            
            elif "who made you" in query or "who created you" in query:
                var.set("Jarvis: I have been created by Lordgodfather.")
                window.update()
                print("Jarvis: I have been created by Lordgodfather.")
                speak("I have been created by Lord god father.") 
                break
            
            elif "who i am" in query:
                var.set("Jarvis: If you talk then definately you are human.")
                window.update()
                print("Jarvis: If you talk then definately you are human.")
                speak("If you talk then definately you are human.") 
                break
            
            elif "why you came to world" in query: 
                var.set("Jarvis: Thanks to Lordgodfather. I am here to make your life easy. Further It's a secret.")
                window.update()
                print("Jarvis: Thanks to Lordgodfather. I am here to make your life easy. Further It's a secret.")
                speak("Thanks to Lord god father. I am here to make your life easy. Further It's a secret") 
                break
            
            elif 'is love' in query: 
                var.set("Jarvis: It is 7th sense that destroys all other senses.")
                window.update()
                print("Jarvis: It is 7th sense that destroys all other senses.")
                speak("It is 7th sense that destroys all other senses") 
                break
            
            elif "who are you" in query:
                var.set("Jarvis: Hello, I am Jarvis. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra.")
                window.update()
                print("Jarvis: Hello, I am Jarvis. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra.")
                speak("Hello, I am Jarvis. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra.") 
                break
            
            elif 'reason for you' in query:
                var.set("Jarvis: I was created as a Minor project by Mr. Lordgodfather.")
                window.update()
                print("Jarvis: I was created as a Minor project by Mr. Lordgodfather.")
                speak("I was created as a Minor project by Mister lord god father") 
                break
            
            elif "will you be my gf" in query or "will you be my bf" in query: 
                var.set("Jarvis: I'm not sure about, may be you should give me some time.")
                window.update()
                print("Jarvis: I'm not sure about, may be you should give me some time.")
                speak("I'm not sure about, may be you should give me some time") 
                break
            
            elif "i love you" in query:
                var.set("Jarvis: It's hard to understand")
                window.update()
                print("Jarvis: It's hard to understand")
                speak("It's hard to understand")
                break
            
            elif "age" in query or"old" in query:
                var.set("Jarvis: I was created in 2020,so I'm still fairly young.But I've learned so much! I hope I'm wise beyond my years.")
                window.update()
                print("Jarvis: I was created in 2020,so I'm still fairly young.But I've learned so much! I hope I'm wise beyond my years.")
                speak("I was created in 2020,so I'm still fairly young...But I've learned so much! I hope I'm wise beyond my years")
                break
            
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('HEY')
label2.pack()

label0 = Label(window, textvariable = var0, bg = '#ADD8E6')
label0.config(font=("Courier", 20))
label0.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('WELCOME')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('JARVIS')

label = Label(window, width = 500, height = 400)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishMe, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()            