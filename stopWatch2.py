import os
import time
import pyautogui
import speech_recognition as sr
import pyttsx3
import re

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for user voice commands
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except:
        speak("Sorry, I did not understand.")
        return ""

# Extract duration in seconds from command
def extract_duration(command):
    match = re.search(r'(\d+)\s*(second|seconds|minute|minutes|min)', command)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        if "second" in unit:
            return value
        elif "minute" in unit or "min" in unit:
            return value * 60
    return None

# Simulate stopwatch start with click and wait
def start_stopwatch(seconds):
    speak(f"Starting stopwatch for {seconds} seconds")
    pyautogui.click(x=1220, y=620)  # <-- Adjust these coordinates for your screen!
    time.sleep(seconds)
    speak("Time's up!")

# Main function to control the stopwatch
def stopWatch_controller():
    os.system("start ms-clock:")  # Open the Windows Clock app
    time.sleep(3)  # Wait for app to load (adjust if needed)
    speak("Stopwatch is ready. Please tell me the duration.")

    while True:
        command = take_command()
        if "ok bye" in command:
            speak("Goodbye!")
            break

        duration = extract_duration(command)
        if duration:
            start_stopwatch(duration)
        else:
            speak("I didn't understand. Say something like '2 minutes' or '30 seconds'.")

# Run the program
stopWatch_controller()
