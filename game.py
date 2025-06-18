import random
import pyttsx3
import eel
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
        # eel.DisplayMessage(query)
        time.sleep(2)
        
        
    except Exception as e:
        return ""
    return query.lower()
@eel.expose
def game_play():
    print("LET'S PLAY ROCK PAPER SCISSORS!")
    speak("LET'S PLAY ROCK PAPER SCISSORS!")
    eel.DisplayMessage("LET'S PLAY ROCK PAPER SCISSORS!")
    speak("Please tell me your name: ")
    ME = takecommand().strip().capitalize()
    Me_score = 0
    Com_score = 0
    choices = ("rock", "paper", "scissors")
    eel.DisplayMessage(choices)
    for i in range(3):
        speak("Choose Rock, Paper, or Scissors: ")
        eel.DisplayMessage("Choose Rock, Paper, or Scissors: ")
        user_choice = takecommand().strip().lower()

        # Correct common misinterpretations
        if user_choice in ["seizures", "caesar","scissors"]:
            user_choice = "scissors"

        if user_choice not in choices:
            print("Invalid choice. Please say Rock, Paper, or Scissors.")
            speak("Invalid choice. Please say Rock, Paper, or Scissors.")
            eel.DisplayMessage("Invalid choice. Please say Rock, Paper, or Scissors. ")
            continue

        com_choice = random.choice(choices)
        print(f"Computer chose: {com_choice}")
        speak(f"Computer chose: {com_choice}")

        if user_choice == com_choice:
            print("🤝 It's a tie!")
            speak("It's a tie!")
        elif (
            (user_choice == "rock" and com_choice == "scissors") or
            (user_choice == "paper" and com_choice == "rock") or
            (user_choice == "scissors" and com_choice == "paper")
        ):
            print(f"✅ {ME} wins this round!")
            speak(f"{ME} wins this round!")
            eel.DisplayMessage(f"{ME} wins this round!")
            Me_score += 1
        else:
            print("Computer wins this round!")
            speak("Computer wins this round!")
            eel.DisplayMessage(f"{ME} wins this round!")
            Com_score += 1

        print(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
        speak(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
        eel.DisplayMessage(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
        print("-----")

    # Final result
    print(f"FINAL SCORE: {ME} - {Me_score} | Computer - {Com_score}")
    speak(f"FINAL SCORE: {ME} - {Me_score} | Computer - {Com_score}")
    eel.DisplayMessage(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
    
    if Me_score > Com_score:
        print(f"🏆 Winner: {ME}!")
        speak(f"Winner: {ME}!")
    elif Me_score < Com_score:
        print("🏆 Winner: Computer!")
        speak("Winner: Computer!")
    else:
        print("🤝 It's a tie!")
        speak("It's a tie!")
        

game_play()
