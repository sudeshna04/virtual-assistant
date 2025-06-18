from jarvis_db import Note, Task, session
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def add_note():
    print("Please enter the Task ID to which you want to add a note:")
    speak("Please enter the Task ID to which you want to add a note:")
    tid = int(input("You: "))
    task = session.query(Task).filter_by(tid=tid).first()
    
    if not task:
        print("o task found with ID", tid)
        return
    
    print("Please enter your note content:")
    speak("Please enter your note content:")
    data = input("You: ")

    print("Please enter priority (High/Medium/Low):")
    speak("Please enter priority (High/Medium/Low):")
    priority = input("You: ")

    note = Note(data=data, priority=priority, tid=tid)
    session.add(note)
    session.commit()
    print("Note added successfully.")
    speak("Note added successfully.")

def show_notes():
    notes = session.query(Note).all()
    if not notes:
        print(" No notes found.")
        speak(" No notes found.")
        return
    
    print("Here are all your notes:")
    speak("Here are all your notes:")
    for note in notes:
        print(f"  ID: {note.nid}, Task ID: {note.tid}, Priority: {note.priority}")
        print(f"  Content: {note.data}")
        speak(f"  ID: {note.nid}, Task ID: {note.tid}, Priority: {note.priority}")
        speak(f"  Content: {note.data}")
        print("-" * 40)

def update_note():
    print("Please enter the Note ID to update:")
    nid = int(input("You: "))
    note = session.query(Note).filter_by(nid=nid).first()

    if not note:
        print(" No note found with ID", nid)
        return

    print("Enter new note content:")
    data = input("You: ")

    print("Enter new priority (High/Medium/Low):")
    priority = input("You: ")

    note.data = data
    note.priority = priority
    session.commit()
    print("Note updated successfully.")

def delete_note():
    print("Enter the Note ID to delete:")
    nid = int(input("You: "))
    note = session.query(Note).filter_by(nid=nid).first()

    if not note:
        print("No note found with ID", nid)
        return

    session.delete(note)
    session.commit()
    print(f"Note ID {nid} deleted.")

if __name__ == "__main__":
    print("What do you want to do with notes? (add/show/update/delete)")
    speak("What do you want to do with notes? You can add, show, update, or delete notes.")
    action = input("You: ").strip().lower()

    if action == "add":
        add_note()
    elif action == "show":
        show_notes()
    elif action == "update":
        update_note()
    elif action == "delete":
        delete_note()
    else:
        print("I didn't understand. Please choose from add, show, update, or delete.")
