import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"🗣️ {text}")
    engine.say(text)
    engine.runAndWait()

def countdown(seconds):
    speak(f"Starting countdown for {seconds} seconds")
    for i in range(seconds, 0, -1):
        speak(str(i))
        time.sleep(1)
    speak("Time's up!")

# Example use:
countdown(15)
