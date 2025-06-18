# import pyttsx3
# from googletrans import Translator
# import datetime
# import sys
# import pyautogui
# import pyttsx3
# import requests
# import speech_recognition as sr
# import eel
# import time

# def speak(text1):
#     text1=str(text1)
#     engine=pyttsx3.init()
#     rate = engine.getProperty('rate')   # getting details of current speaking rate
#     engine.setProperty('rate', 150)  
#     eel.DisplayMessage(text1)  
#     engine.say(text1)
#     eel.receiverText(text1)
#     engine.runAndWait() # Actually speaks it and waits until it's done

# def takecommand(prompt=""):
#     if prompt:
#         speak(prompt)
    
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         audio = r.listen(source, 10, 6)

#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}")
#         return query.lower()
#     except Exception as e:
#         speak("I didn't catch that. Please try again.")
#         return ""

# def translate_text(text, target_language):
#     translator = Translator()
#     translated = translator.translate(text, dest=target_language)
#     return translated.text

# @eel.expose
# def translation():
#     try:
#         text_to_translate = takecommand("What would you like to translate? ").lower()
#         target_language = takecommand("To which language? ").lower()
#         print("Target language:", target_language)
#         eel.DisplayMessage(f"Translating to {target_language}...")
#         speak(f"Translating to {target_language}...")


#         translated_text = translate_text(text_to_translate, target_language)
#         speak(translated_text)
#         eel.DisplayMessage(translated_text)
#         print("Translated text:", translated_text)
        
     

#     except Exception as e:
#         print("Sorry, something went wrong.")
#         eel.DisplayMessage("Sorry, something went wrong.")
#         speak("Sorry, something went wrong.")
#         print("Error:", e)

# translation()
import eel
from gtts import gTTS
from playsound import playsound
import os
from googletrans import Translator
import speech_recognition as sr
import time

# Initialize eel
# eel.init("web")

# Language mapping (spoken → code)
language_map = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "tamil": "ta"
}

def speak(text, lang="en"):
    try:
        eel.DisplayMessage(text)
        eel.receiverText(text)
        tts = gTTS(text=text, lang=lang)
        filename = "temp.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"❌ Speech Error: {e}")

def takecommand(prompt=""):
    if prompt:
        speak(prompt)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("🎧 Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"✅ You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""
        except Exception as e:
            print(f"⚠️ Error: {e}")
            return ""

def translate_text(text, target_lang_code):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang_code)
    return translated.text

@eel.expose
def translation():
    try:
        text_to_translate = takecommand("What would you like to translate?")
        if not text_to_translate:
            return

        target_lang_spoken = takecommand("Which language do you want to translate to?")
        target_lang_code = language_map.get(target_lang_spoken.lower(), "en")

        eel.DisplayMessage(f"Translating to {target_lang_spoken.capitalize()}...")
        translated_text = translate_text(text_to_translate, target_lang_code)
        speak(translated_text, lang=target_lang_code)

    except Exception as e:
        print("❌ Something went wrong:", e)
        speak("Sorry, something went wrong.")

translation()
# Start app
# eel.start("index.html", size=(500, 400))
