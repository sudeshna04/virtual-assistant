import openai
import eel

import pyttsx3
import speech_recognition as sr

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

API_Key = os.getenv("API_Key")

print("API Key loaded:", bool(API_Key))  # Should print True if loaded


openai.api_key = API_Key
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


def chatBot(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": query}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        answer = response.choices[0].message['content']
        print("Bot:", answer)

        # ✅ Save to .txt
        file_path = "chat_response.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"User: {query}\n")
            file.write(f"Bot: {answer}\n")

        # ✅ Open the file in text editor
        import os, platform
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":
            os.system(f"open {file_path}")
        else:
            os.system(f"xdg-open {file_path}")

        # ✅ Read and speak/display from file
        with open(file_path, "r", encoding="utf-8") as file:
            saved_response = file.read()
            print("\n📝 Saved Response from File:\n", saved_response)

            speak(saved_response)
            eel.receiverText(saved_response)

        return answer

    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't process your request."
chatBot("lord krishna")