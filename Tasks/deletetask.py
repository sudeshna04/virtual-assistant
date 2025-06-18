from jarvis_db import Task, session
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
    engine.runAndWait()
def delete_task():
    try:
        print("Jarvis: Please enter the Task ID you want to delete:")
        speak("Please enter the Task ID you want to delete:")
        task_id = int(input("You: "))

        task = session.query(Task).filter_by(tid=task_id).first()

        if not task:
            print("Jarvis: ❌ No task found with ID", task_id)
            speak(f"No task found with ID {task_id}.")
            return

        session.delete(task)
        session.commit()

        print(f"Jarvis: ✅ Task ID {task_id} has been deleted.")
        speak(f"Task ID {task_id} has been deleted.")
    except Exception as e:
        print(f"Jarvis: ⚠️ Error occurred - {e}")

if __name__ == "__main__":
    delete_task()
