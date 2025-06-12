import random
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def game_play():
    print("LET'S PLAY ROCK PAPER SCISSORS!")
    speak("LET'S PLAY ROCK PAPER SCISSORS!")
    ME = input("Please tell me your name: ").strip()
    Me_score = 0
    Com_score = 0
    choices = ("rock", "paper", "scissors")

    for i in range(5):
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        
        # Handle common typos or funny alternatives
        if user_choice == "seizures" or user_choice == "caesar":
            user_choice = "scissors"

        if user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        com_choice = random.choice(choices)
        print(f"Computer chose: {com_choice}")
        speak(f"Computer chose: {com_choice}")

        if user_choice == com_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and com_choice == "scissors") or
            (user_choice == "paper" and com_choice == "rock") or
            (user_choice == "scissors" and com_choice == "paper")
        ):
            print(f"{ME} wins this round!")
            speak(f"{ME} wins this round!")
            Me_score += 1
        else:
            print("Computer wins this round!")
            speak("Computer wins this round!")
            Com_score += 1

        print(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
        speak(f"Score: {ME} - {Me_score} | Computer - {Com_score}")
        print("-----")

    print(f"FINAL SCORE: {ME} - {Me_score} | Computer - {Com_score}")
    speak(f"FINAL SCORE: {ME} - {Me_score} | Computer - {Com_score}")
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
