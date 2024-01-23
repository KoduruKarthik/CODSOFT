tasks = []

def show():
    """Show the to-do list."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add(task):
    """Add a task to the to-do list."""
    tasks.append(task)
    print(f"Added task: {task}")

def remove(task_number):
    """Remove a task from the to-do list."""
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number. Please check your to-do list.")

while True:
    print("\nChoose an option:")
    print("1. Show to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        show()
    elif choice == '2':
        task = input("Enter the task: ")
        add(task)
    elif choice == '3':
        task_number = int(input("Enter the task number to remove: "))
        remove(task_number)
    elif choice == '4':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid number.")
