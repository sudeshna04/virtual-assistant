from jarvis_db import Task, session
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_pending_tasks():
    pending_tasks = session.query(Task).filter_by(status="Pending").all()

    if not pending_tasks:
        message = "You have no pending tasks."
        print( message)
        speak(message)
    else:
        message = "Your pending tasks are: "
        print( message)
        for task in pending_tasks:
            task_info = f"Task ID {task.tid}, Name: {task.name} with {task.priority} priority"
            print(f"- {task_info}")
            message += task_info + ", "
        speak(message)

# --- Run it ---
if __name__ == "__main__":
    tell_pending_tasks()
