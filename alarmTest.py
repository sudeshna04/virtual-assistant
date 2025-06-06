import os
import time as time_module
import datetime
from playsound import playsound
import pyttsx3

engine = pyttsx3.init()

def Say(text):
    engine.say(text)
    print("Speaking:", text)
    engine.runAndWait()

def set_alarm():
    Say("Please specify the time for the alarm (e.g., '10:30').")
    alarm_time = input("Enter time (HH:MM): ").strip()

    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        Say("Invalid time format. Please use HH:MM format.")
        return None

    with open("Alarmtext.txt", "w") as alarm_file:
        alarm_file.write(alarm_time)

    Say(f"Alarm set for {alarm_time}.")
    return alarm_time

def ring_alarm(alarm_time):
    Say(f"Waiting for alarm at {alarm_time}...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Current time: {current_time} | Alarm time: {alarm_time.strip()}")  # Debug
        if current_time == alarm_time.strip():
            Say("Alarm ringing.")
            try:
                playsound("www\\assets\\audio\\start_sound.mp3")  # Simplify path or use absolute path
            except Exception as e:
                Say(f"Could not play the alarm sound: {e}")
            break
        time_module.sleep(1)

def handle_alarm():
    alarm_time = set_alarm()
    if alarm_time:
        ring_alarm(alarm_time)

handle_alarm()
