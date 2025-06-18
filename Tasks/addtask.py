from jarvis_db import Task, session
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

# def takecommand():
#     r=sr.Recognizer()
    
#     with sr.Microphone() as source:
#         print("Listening....")
#         # eel.DisplayMessage("Listening....")        
#         r.pause_threshold=1
#         r.adjust_for_ambient_noise(source, duration=0.5)  # shorter noise adjust
#         audio=r.listen(source,10,6)

#     try:
#         print("Recognizing..")
#         # eel.DisplayMessage("Recognizing...")
#         query=r.recognize_google(audio,language='en-in')
#         print(f"user said: {query}")
#         # eel.DisplayMessage(query)
#         time.sleep(2)
        
        
#     except Exception as e:
#         return ""
#     return query.lower()


# def add_task_from_input():
#     # Get task name
#     speak("What is the name of your task?")
#     while True:
#         name = takecommand().strip().capitalize()
#         if name:
#             break
#         speak("I didn't catch that. Please say the task name again.")

#     print(f"Task name received: {name}")

#     # Get status
#     valid_statuses = ["Pending", "Completed"]
#     speak("What is the status of your task? Pending or Completed?")
#     while True:
#         status = takecommand().strip().capitalize()
#         if status in valid_statuses:
#             break
#         speak("Invalid status. Please say either Pending or Completed.")

#     # Get priority
#     valid_priorities = ["High", "Medium", "Low"]
#     speak("What is the priority of your task? High, Medium, or Low?")
#     while True:
#         priority = takecommand().strip().capitalize()
#         if priority in valid_priorities:
#             break
#         speak("Invalid priority. Please say High, Medium, or Low.")

#     # Save the task
#     task = Task(name=name, status=status, priority=priority)
#     session.add(task)
#     session.commit()

#     speak(f"Task '{task.name}' added successfully with status {task.status} and priority {task.priority}")

# add_task_from_input()
# --- Run it ---
# if __name__ == "__main__":
#     add_task_from_input()

# from jarvis_db import Task, session


def add_task_from_input():
    speak(" Add New Task")
    print("Add New Task")
    speak(f"enter name of your task:")
    name=input("Enter name of your task:").capitalize().strip()

    speak(f"Enter task status (Pending/Completed):")
    status = input("Enter task status (Pending/Completed): ").capitalize().strip()
    
    speak(f"Enter task priority (High/Medium/Low):")
    priority = input("Enter task priority (High/Medium/Low): ").capitalize().strip()
    # Optional: validate inputs
    if status not in ["Pending", "Completed"]:
        print("Invalid status. Must be 'Pending' or 'Completed'.")
        speak("Invalid status. Must be 'Pending' or 'Completed'.")
        return
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Must be 'High', 'Medium', or 'Low'.")
        speak("Invalid priority. Must be 'High', 'Medium', or 'Low'.")
        return

    # Create and save the task
    task = Task(name=name, status=status, priority=priority)
    session.add(task)
    session.commit()

    print(f"Task added with ID {task.tid},Name:{task.name}, Status: {task.status}, Priority: {task.priority}")
    speak(f"Task added with ID {task.tid}, Name: {task.name}, Status: {task.status}, Priority: {task.priority}")
# --- Run it ---
if __name__ == "__main__":
    add_task_from_input()
import sys
import os
import pyttsx3
import speech_recognition as sr
import time

# ✅ Ensure Python can find jarvis_db.py in parent directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from jarvis_db import Task, session  # Now this should work!

# def speak(text1):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.say(str(text1))
#     engine.runAndWait()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Listening...")
#         speak("I'm listening.")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=1)
#         try:
#             audio = r.listen(source, timeout=5, phrase_time_limit=10)
#             print("🎧 Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print(f"✅ You said: {query}")
#             return query.lower()
#         except sr.UnknownValueError:
#             speak("Sorry, I couldn't understand.")
#             return ""
#         except sr.RequestError as e:
#             speak("Network error.")
#             print(f"API error: {e}")
#             return ""
#         except Exception as e:
#             print(f"General error in takecommand(): {e}")
#             return ""

# def add_task_from_input():
#     speak("What is the name of your task?")
#     name = takecommand().capitalize().strip()
#     print(f"Task name received: {name}")
#     if not name:
#         speak("Task name not understood.")
#         return

#     speak("What is the status of your task? Pending or Completed?")
#     status = takecommand().capitalize().strip()
#     if status not in ["Pending", "Completed"]:
#         speak("Invalid status. Please say either Pending or Completed.")
#         return

#     speak("What is the priority of your task? High, Medium, or Low?")
#     priority = takecommand().capitalize().strip()
#     print(f"Priority received: {priority}")
#     if priority not in ["High", "Medium", "Low"]:
#         speak("Invalid priority. Please say High, Medium, or Low.")
#         return

#     # ✅ Save the task
#     task = Task(name=name, status=status, priority=priority)
#     session.add(task)
#     session.commit()

#     speak(f"Task '{task.name}' added successfully with status {task.status} and priority {task.priority}")

# # --- Run it ---
# if __name__ == "__main__":
#     add_task_from_input()
