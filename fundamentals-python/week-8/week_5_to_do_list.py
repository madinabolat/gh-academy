# Simple To-Do List. Create a program that allows a user to manage a to-do list. The user should be able to:
# Add a new task.
# View all tasks.
# Delete a task by its name or number.
# The program should loop until the user decides to quit.

# Modify your To-Do List program from earlier. 
# When the program starts, it should read any existing tasks from a file named tasks.txt.
# When the user adds or deletes a task, the program should update the file. 
# This way, the tasks are not lost when the program closes.

def add_tasks():
    new_tasks =[]
    while True: 
        user_input = input("Enter your task (type 'stop' if you are done): ")
        if user_input == "stop":
            break
        new_tasks.append(user_input)
        add_line_to_file(user_input, filepath)
    return new_tasks

def delete_task():
    print("Enter the number of a task you want to remove: ")
    n = int(input())
    delete_line_from_file(tasks[n],filepath)
    tasks.pop(n)

def view_tasks(tasks):
    for task in tasks:
        print("%d: %s" %(tasks.index(task), task))

def add_line_to_file(line, filepath):
    with open(filepath, 'a') as f:
        tasks = f.write('\n')
        tasks = f.write(line)

def delete_line_from_file(specific_line, filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    with open(filepath, 'w') as f:
        for line in lines:
            if line.strip('\n') != specific_line:
                f.write(line)

print("Welcome to your task manager!")
filepath = "tasks.txt"
tasks = []
with open('tasks.txt', 'r') as f:
    tasks = f.read().splitlines()
print("Current tasks:")
for task in tasks:
    print(task)

while True:
    print("Next action. Please type 'add' for adding tasks, 'view' for viewing your current asks, 'delete' for deleting a task or 'done' if you want to quit.")
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

