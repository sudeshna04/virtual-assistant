import pyttsx3
import speech_recognition as sr
import random

# Initialize TTS engine
engine = pyttsx3.init()

# List of motivational quotes
motivational_quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "Your limitation—it's only your imagination. – Unknown"
]

# Speak function
def speak(text):
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

# Function to give motivational quotes
def give_motivational_quote():
    quote = random.choice(motivational_quotes)
    print(quote)
    speak(quote)

# Main control loop for Jarvis
def jarvis_quotes():
    speak("Jarvis is now active and listening.")
    while True:
        command = take_command()

        if "motivational quote" in command or "tell me a motivational quote" in command or "say me a motivational quote" in command:
            give_motivational_quote()
        
        elif "thank you" in command:
            speak("you're Welcome")
        
        elif "bye" in command:
            speak("Okay bye, have a nice day")
            break

        elif "exit" in command or "quit" in command :
            speak("Okay")
            break
        
        else:
            speak("Command not recognized. Try again.")

# Run the controller
jarvis_quotes()
