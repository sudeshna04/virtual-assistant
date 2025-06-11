import pyttsx3
from googletrans import Translator
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
    # eel.DisplayMessage(text1)  
    engine.say(text1)
    # eel.receiverText(text1)
    engine.runAndWait() # Actually speaks it and waits until it's done

def takecommand(prompt=""):
    if prompt:
        speak(prompt)
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        return query.lower()
    except Exception as e:
        speak("I didn't catch that. Please try again.")
        return ""

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text


def translation():
    try:
        text_to_translate = takecommand("What would you like to translate? ").lower()
        target_language = takecommand("To which language? ").lower()
        print("Target language:", target_language)

        translated_text = translate_text(text_to_translate, target_language)
        speak(translated_text)
        print("Translated text:", translated_text)
     

    except Exception as e:
        print("Sorry, something went wrong.")
        speak("Sorry, something went wrong.")
        print("Error:", e)

translation()
