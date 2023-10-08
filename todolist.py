import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Initialize the tasks list or load existing tasks
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['description']} - Due: {task['due_date'] if 'due_date' in task else 'Not specified'}")

# Function to add a task
def add_task(description, due_date=None):
    task = {"description": description}
    if due_date:
        task["due_date"] = due_date
    tasks.append(task)
    save_tasks()
    print("Task added successfully.")

# Function to mark a task as completed
def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks()
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Function to save tasks to the file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        description = input("Enter task description: ")
        due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
        add_task(description, due_date)
    elif choice == "3":
        display_tasks()
        index = int(input("Enter the index of the task to mark as completed: "))
        complete_task(index)
    elif choice == "4":
        display_tasks()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")

