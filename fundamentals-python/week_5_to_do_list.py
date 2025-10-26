# Simple To-Do List. Create a program that allows a user to manage a to-do list. The user should be able to:
# Add a new task.
# View all tasks.
# Delete a task by its name or number.
# The program should loop until the user decides to quit.

def add_tasks():
    tasks =[]
    while True: 
        user_input = input("Enter your task (type 'stop' if you are done): ")
        if user_input == "stop":
            break
        tasks.append(user_input)
    return tasks

def delete_task():
    print("Enter the number of a task you want to remove: ")
    n = int(input())
    tasks.pop(n)

def view_tasks(tasks):
    for task in tasks:
        print("%d: %s" %(tasks.index(task), task))

print("Welcome to your task manager!")
tasks=[]
while True:
    print("Next action. Please type 'add' for adding tasks, 'view' for vieweing your current asks, 'delete' for deleting a task or 'done' if you want to quit.")
    action = input()
    if action == "done":
        break
    elif action == "add":
        new_tasks = add_tasks()
        tasks.extend(new_tasks)
    elif action == "view":
        view_tasks(tasks)
    elif action == "delete":
        delete_task()
    else: 
        print("Enter valid command.")
