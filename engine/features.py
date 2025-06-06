import datetime
import os
import struct
import subprocess
import time
import eel
import re
import webbrowser
import sqlite3
from hugchat import hugchat
from playsound import playsound
import pvporcupine
import pyaudio
import pyautogui
import pyttsx3
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit
from engine.helper import extract_yt_term, format_response, remove_words, split_text_by_sentences, stTerm
from engine.command import allCommands
from urllib.parse import quote

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()


@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    mappings = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "notepad": "notepad",
        "calculator": "calc",
        "word": "winword",
        "msword":"winword",
        "excel": "excel",
        "clock": "ms-clock:",
        "calendar": "outlookcal:",
        "settings": "ms-settings:",
    }

    app_name = query

    if app_name != "":
        try:
            # Check in database first
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + app_name)
                os.startfile(results[0][0])
                return

            # Check in web_command
            cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + app_name)
                webbrowser.open(results[0][0])
                return

            # Check in mappings
            if app_name in mappings:
                speak("Opening " + app_name)
                if mappings[app_name].startswith("ms-") or ":" in mappings[app_name]:
                    subprocess.run(f"start {mappings[app_name]}", shell=True)
                else:
                    os.startfile(mappings[app_name])
                return

            # As a last fallback
            speak("Opening " + app_name)
            os.system("start " + app_name)

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong")

# greet
@eel.expose
def greetInitialSound():
    hr=int(datetime.datetime.now().hour)
    if 0 <= hr < 12:
        speak("Good Morning!")
    elif 12 <= hr < 17:
        speak("Good Afternoon!")
    elif 17 <= hr < 21:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am JARVIS. How can I help you?")


# play particular on youTube
def playYoutube(query):
    search_term = extract_yt_term(query)

    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    
    elif "on youtube" in query:
        stream=stTerm(query)
        if stream:
            speak("Playing " + stream + " on YouTube")
            kit.playonyt(stream)

    else:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")


import random
def speak_thankyou_response():
    responses = [
        "You're welcome!",
        "Anytime!",
        "Welcome dear!",
        "Glad to help!",
        "No problem at all!",
        "Always here for you!"
    ]
    response = random.choice(responses)
    speak(response)

 
#  hotword or wakeWord
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")
                
                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

                allCommands()
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    

# Whatsapp
voice_call_coords = (1291, 65)    #x, y = pyautogui.position()
video_call_coords = (1240, 67)    

def whatsApp(mobile_no, message, flag, name):
    flag = flag.lower()

    if flag == 'message':
        encoded_message = quote(message)
    else:
        encoded_message = quote("")

    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(6)

    if flag == 'message':
        pyautogui.press('enter')
        speak(f"Message sent successfully to {name}")

    elif flag == 'call':
        pyautogui.moveTo(voice_call_coords[0], voice_call_coords[1], duration=0.5)
        pyautogui.click()
        speak(f"Calling to {name}")

    elif flag == 'video call':
        pyautogui.moveTo(video_call_coords[0], video_call_coords[1], duration=0.5)
        pyautogui.click()
        speak(f"Starting video call with {name}")


# search google
def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Opening Google search results for: {query}")
