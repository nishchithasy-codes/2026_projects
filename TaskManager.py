import sqlite3

# Connect to database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()


while True:

    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # 1. Add Task
    if choice == "1":

        task = input("Enter task: ").strip()

        if task == "":
            print("Task cannot be empty.")
            continue

        priority = input("Enter priority (High/Medium/Low): ").capitalize()

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority.")
            continue

        cursor.execute("""
        INSERT INTO tasks (task, priority, status)
        VALUES (?, ?, ?)
        """, (task, priority, "Pending"))

        conn.commit()

        print("Task added successfully!")


    # 2. View Tasks
    elif choice == "2":

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        if not tasks:
            print("No tasks found.")

        else:
            print("\n===== YOUR TASKS =====")

            for task in tasks:
                print(
                    "ID:", task[0],
                    "| Task:", task[1],
                    "| Priority:", task[2],
                    "| Status:", task[3]
                )


    # 3. Mark Task as Completed
    elif choice == "3":

        task_id = int(input("Enter task ID: "))

        cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """, ("Completed", task_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Task marked as completed!")
        else:
            print("Task not found.")


    # 4. Delete Task
    elif choice == "4":

        task_id = int(input("Enter task ID to delete: "))

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Task deleted successfully!")
        else:
            print("Task not found.")


    # 5. Search Task
    elif choice == "5":

        keyword = input("Enter keyword to search: ")

        cursor.execute("""
        SELECT * FROM tasks
        WHERE task LIKE ?
        """, ("%" + keyword + "%",))

        results = cursor.fetchall()

        if not results:
            print("No matching tasks found.")

        else:
            print("\n===== SEARCH RESULTS =====")

            for task in results:
                print(
                    "ID:", task[0],
                    "| Task:", task[1],
                    "| Priority:", task[2],
                    "| Status:", task[3]
                )


    # 6. Exit
    elif choice == "6":

        print("Thank you for using Task Manager!")
        break


    else:
        print("Invalid choice. Please try again.")


# Close database
conn.close()