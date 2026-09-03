tasks = []
def add_task():
    task= input("Enter a task: ")
    tasks.append(task)
    print("task added!")
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return 
    print("\nYour Tasks:")
    for i,task in enumerate(tasks,start = 1):
        print(f"{i}. {task}")
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
while True:
    print("\n==== TO-DO LIST ====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("invalid choice.")