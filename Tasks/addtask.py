from jarvis_db import Task, session


def add_task_from_input():
    print("📝 Add New Task")
    name=input("Enter name of your task:").capitalize().strip()
    status = input("Enter task status (Pending/Completed): ").capitalize().strip()
    priority = input("Enter task priority (High/Medium/Low): ").capitalize().strip()

    # Optional: validate inputs
    if status not in ["Pending", "Completed"]:
        print("❌ Invalid status. Must be 'Pending' or 'Completed'.")
        return
    if priority not in ["High", "Medium", "Low"]:
        print("❌ Invalid priority. Must be 'High', 'Medium', or 'Low'.")
        return

    # Create and save the task
    task = Task(name=name, status=status, priority=priority)
    session.add(task)
    session.commit()

    print(f"✅ Task added with ID {task.tid},Name:{task.name}, Status: {task.status}, Priority: {task.priority}")

# --- Run it ---
# if __name__ == "__main__":
#     add_task_from_input()
