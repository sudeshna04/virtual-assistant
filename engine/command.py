import datetime
import sys
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import eel
import time

def speak(text1):
    text1=str(text1)
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)  
    eel.DisplayMessage(text1)  
    engine.say(text1)
    eel.receiverText(text1)
    engine.runAndWait() # Actually speaks it and waits until it's done

def takecommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")        
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=0.5)  # shorter noise adjust
        audio=r.listen(source,10,6)

    try:
        print("Recognizing..")
        eel.DisplayMessage("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
        
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommands(message=1):
    try:
        if message == 1:
            query = takecommand()
            eel.senderText(query)

        else:
            query = message.lower()
            eel.senderText(query)

        print("Query received:", query)

        if "bye" in query:
            speak("Okay bye, see you soon!")
            eel.quit()            

        elif "play" in query and "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        elif "play music" in query:
            from music import jarvis_music_controller
            jarvis_music_controller(query)

        elif "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "how are you" in query:
            speak("I am fine, how about you?")

        elif "how are you doing today" in query:
            speak("I am doing great, how about you?")

        elif "jarvis" == query:
            speak("Ya, I am listening")

        elif "thank you" in query or "thanks" in query:
            from engine.features import speak_thankyou_response
            speak_thankyou_response()

        elif "search" in query:
            from engine.features import search_google
            search_google(query)
        
        elif "lord" in query:
            speak("Hare krishna")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)


        elif "date" in query:
            date = datetime.date.today()
            speak(date)


        elif "day" in query:            
            day = datetime.datetime.now().strftime("%A")
            speak(day)

        elif "my ip address" in query or "my ip" in query:
            speak("Finding IP Address")
            ip_address = requests.get('https://api.ipify.org?format=json').json()
            result = ip_address["ip"]

            speak("Your IP Address is: " + result)

        elif "hello" in query:
            speak("Hii")

        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("screenshot_sample.jpg")
            speak("Screenshot captured and saved.")
           
        # whatsApp
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if contact_no != 0:
                if "send message" in query:
                    flag = 'message'
                    speak("What message to send?")
                    query = takecommand()
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'

                whatsApp(contact_no, query, flag, name)
        # else:
        #     speak("Sorry, I cannot understand")

        else:
        #    from engine.features import chatBot
        #    speak("Please wait while am fetching...")
        #    chatBot(query)
             from gpt import chatBot
             speak("Please wait while am fetching...")
             chatBot(query)
        
           
    except Exception as e:
        print("Error:", str(e))

    eel.ShowHood()
