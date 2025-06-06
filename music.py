import eel
import pygame
import pyttsx3
import speech_recognition as sr
import os
import random
import time

# Config
MUSIC_FOLDER = "./www/assets/music" 

# Initialize modules
pygame.mixer.init()
engine = pyttsx3.init()

# Speak function
def speak(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    eel.DisplayMessage(text)
    eel.receiverText(text)

    engine.say(text)
    engine.runAndWait()


# Listen to user
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
        speak("Sorry, I didn't catch that.")
        return ""

# Music control
def get_random_song():
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
    if not files:
        speak("No music files found.")
        return None
    return os.path.join(MUSIC_FOLDER, random.choice(files))

def play_random_music():
    song_path = get_random_song()
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        speak(f"Now playing: {os.path.basename(song_path)}")

def pause_music():
    pygame.mixer.music.pause()
    speak("Music paused.")

def unpause_music():
    pygame.mixer.music.unpause()
    speak("Resuming music.")

def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")

def rewind_music():
    pygame.mixer.music.rewind()
    speak("Rewinding music.")

def forward_music(seconds=10):
    current_pos = pygame.mixer.music.get_pos() / 1000.0
    new_pos = current_pos + seconds
    pygame.mixer.music.play(start=new_pos)
    speak(f"Forwarded to {int(new_pos)} seconds.")

# Main control loop
def jarvis_music_controller():
    speak("Jarvis music controller is now active.")
    speak("Say 'start music' to start playing ")
    while True:
        command = take_command()
        if "play music" in command or "start music" in command:
            play_random_music()
        elif "pause" in command:
            pause_music()
        elif "resume" in command or "continue" in command:
            unpause_music()
        elif "stop" in command:
            stop_music()
        elif "rewind" in command:
            rewind_music()
        elif "forward" in command:
            forward_music(10)
        elif "exit" in command or "quit" in command:
            stop_music()
            speak("Exiting music control.")
            break
        else:
            speak("Command not recognized. Try again.")

# Run the controller
jarvis_music_controller()
