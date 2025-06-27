# Simple To-Do List App

#Import necessary libraries
import argparse
import json
import os

# In data.json , we will store our tasks
TASK = "data.json"

# functions to load the task which is stored in data.json
def load_tasks():
    if os.path.exists(TASK):
        with open(TASK, 'r') as f: 
            try:
              return json.load(f)
            except json.JSONDecodeError:
                print("Error: The task file is corrupted or empty.")
                return []
    return []

# save tasks to data.json
def save_tasks(tasks):
    with open(TASK, 'w') as f:
        json.dump(tasks, f, indent=4)

# Adding a new task to the list 
def add_task(task,category):
    tasks = load_tasks()
    tasks.append({"task":task,
                  "category": category if category else "General"})
    save_tasks(tasks)
    print(f"Task added: {task} [{category}]")

# checking if the task is present in the list and removing it
def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed}")
    else:
        print(" Not in the list. Please check the index.")

# to view all tasks in the list
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
    for i, task in enumerate(tasks):
        print(f"{i}. {task['task']}[{task['category']}]")

# Making a Command Line Interface (CLI) for the To-Do List App
parser = argparse.ArgumentParser(description=" A To-Do list App") #Define what Command line arguments my script can accept , Description is not necessary

parser.add_argument('--add', help="Add a new task")               # whatever we pass after --add , our program will treat it as a task to be added
parser.add_argument('--category', help="Add a category with the task") # add a category to the task
parser.add_argument('--remove', type=int, help="Remove a task by index")       # remove a task by its index in the list
parser.add_argument('--view', action='store_true', help="View all tasks")      # view all tasks in the list

args = parser.parse_args()    # now we can access the arguments using "args.add", "args.remove", and "args.view"
 
if args.add:
    add_task(args.add, args.category)
elif args.remove is not None:
    remove_task(args.remove)
elif args.view:
    view_tasks()
else:
    print("Error : No valid command . Use --add, --remove, or --view.")
