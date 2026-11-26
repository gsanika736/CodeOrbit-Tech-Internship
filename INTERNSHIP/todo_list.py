
# ==========================================
# TO-DO LIST CLI APPLICATION
# ==========================================

# Creating an empty list to store tasks
tasks = []


# Function to add a new task
def add_task():
    task = input("\nEnter your new task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


# Function to display all tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nYour To-Do List is empty!")
    else:
        print("\n========== YOUR TO-DO LIST ==========")

        # Displaying tasks with numbers
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# Function to remove a task
def remove_task():
    view_tasks()

    if len(tasks) > 0:
        try:
            task_number = int(input("\nEnter task number to remove: "))

            # Checking whether the task number is valid
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Task removed successfully:", removed_task)
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")


# Function to save tasks into a text file
def save_tasks():
    try:
        with open("tasks.txt", "w") as file:

            for task in tasks:
                file.write(task + "\n")

        print("Tasks saved successfully in tasks.txt!")

    except OSError:
        print("Error while saving tasks!")


# Main program loop
while True:

    print("\n========== TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        save_tasks()

    elif choice == "5":
        print("\nThank you for using To-Do List App!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")
