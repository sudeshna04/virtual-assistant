from jarvis_db import Task, session

def delete_task():
    try:
        print("Jarvis: Please enter the Task ID you want to delete:")
        task_id = int(input("You: "))

        task = session.query(Task).filter_by(tid=task_id).first()

        if not task:
            print("Jarvis: ❌ No task found with ID", task_id)
            return

        session.delete(task)
        session.commit()

        print(f"Jarvis: ✅ Task ID {task_id} has been deleted.")
    except Exception as e:
        print(f"Jarvis: ⚠️ Error occurred - {e}")

if __name__ == "__main__":
    delete_task()
