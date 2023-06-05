tasks = []

def add_task():
    task = input("Enter a task : ")
    tasks.append(task)
    print("Task added successfully!!!")

def view_task():
    if tasks:
        print("Tasks: ")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
    else:
        print("No Tasks:")

def remove_task():
    view_task()
    index = int(input("Enter the task number to remove: "))
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task {removed_task} removed successfully!")
    else:
        print("Invalid task number")

while True:
    print("Welocme to To-Do List")
    print("\t1. Add Task")
    print("\t2. view Task")
    print("\t3. Remove Task")
    print("\t4. Quit")

    choice = input("Enter your choice (1-4)")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("GoodBye!")
        break
    else:
        print("Invalid choice! please try again.")
        


