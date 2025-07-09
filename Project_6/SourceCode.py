import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['completed'] else "✘"
        print(f"{i}. [{status}] {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")

# Add task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    })
    print("Task added!")

# Edit task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        i = int(input("Enter task number to edit: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["title"] = input("New title: ") or tasks[i]["title"]
            tasks[i]["priority"] = input("New priority: ") or tasks[i]["priority"]
            tasks[i]["due_date"] = input("New due date: ") or tasks[i]["due_date"]
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Mark as done
def toggle_task_completion(tasks):
    display_tasks(tasks)
    try:
        i = int(input("Enter task number to toggle completion: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["completed"] = not tasks[i]["completed"]
            print("Task status updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Delete task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        i = int(input("Enter task number to delete: ")) - 1
        if 0 <= i < len(tasks):
            del tasks[i]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n==== TASK MANAGER ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Mark as Done/Undone")
        print("5. Delete Task")
        print("6. Save & Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            toggle_task_completion(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Mhuwaa!! See Yaa")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
