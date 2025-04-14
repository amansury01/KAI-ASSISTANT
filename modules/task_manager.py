import json
import os

TASK_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return f"Task added: {task}"

def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        return f"Task removed: {task}"
    else:
        return f"Couldn't find task: {task}"

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        return "You have no tasks right now."
    return "Here are your tasks:\n" + "\n".join([f"- {t}" for t in tasks])
