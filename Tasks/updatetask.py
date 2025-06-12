from jarvis_db import Task, session
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def change_specific_task():
    try:
        speak("Jarvis: Which task do you want to change? Please tell me the Task ID.")
        task_id = int(input("You: "))
        task = session.query(Task).filter_by(tid=task_id).first()

        if not task:
            speak("Task not found.")
            return

        speak("Jarvis: Tell me the new status (Pending/Completed):")
        new_status = input("You: ").capitalize()
        if new_status not in ["Pending", "Completed"]:
            speak("Jarvis: ❌ Invalid status.")
            return

        speak("Jarvis: Tell me the new priority (High/Medium/Low):")
        new_priority = input("You: ").capitalize()
        if new_priority not in ["High", "Medium", "Low"]:
            speak("Jarvis: ❌ Invalid priority.")
            return

        task.status = new_status
        task.priority = new_priority
        session.commit()

        speak(f"Jarvis: ✅ Task ID {task_id} updated to {new_status} status and {new_priority} priority.")
    except Exception as e:
        speak(f"Jarvis: ⚠️ Error occurred - {e}")

def change_by_status_only():
    try:
        speak("Jarvis: Tell me the status to filter by (Pending/Completed):")
        status = input("You: ").capitalize()
        if status not in ["Pending", "Completed"]:
            speak("Jarvis: ❌ Invalid status.")
            return

        speak("Jarvis: Tell me the priority (High/Medium/Low):")
        priority = input("You: ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            speak("Jarvis: ❌ Invalid priority.")
            return

        # You can modify this logic to select by user choice later
        task = session.query(Task).filter_by(status=status, priority=priority).first()

        if not task:
            speak("Jarvis: ❌ No task found with given status and priority.")
            return

        speak(f"Jarvis: Found Task ID {task.tid}. Now updating it...")
        speak("Jarvis: What is the new status? (Pending/Completed):")
        new_status = input("You: ").capitalize()
        speak("Jarvis: What is the new priority? (High/Medium/Low):")
        new_priority = input("You: ").capitalize()

        task.status = new_status
        task.priority = new_priority
        session.commit()

        speak(f"Jarvis: ✅ Task ID {task.tid} successfully updated to {new_status} status and {new_priority} priority.")

    except Exception as e:
        speak(f"Jarvis: ⚠️ Error occurred - {e}")

# Example menu to test both
if __name__ == "__main__":
    print("Type 1 to change by Task ID or 2 to change by status/priority:")
    speak("Type 1 to change by Task ID or 2 to change by status/priority:")
    choice = input("You: ").strip()
    if choice == "1":
        change_specific_task()
    elif choice == "2":
        change_by_status_only()
    else:
        speak("Jarvis: ❌ Invalid choice.")
