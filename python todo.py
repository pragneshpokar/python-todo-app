# Simple To-Do List App

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete.")
            return

        view_tasks()
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Error occurred.")

# Main Program
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Good bye!")
        break
    else:
        print("Invalid choice, try again.")