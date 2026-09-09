import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    amount REAL,
    category TEXT,
    description TEXT
)
""")

conn.commit()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Delete Transaction")
    print("5. Exit")

    choice = input("Enter your choice: ")


    # 1. Add Transaction
    if choice == "1":

        transaction_type = input("Enter type (income/expense): ").lower()
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        cursor.execute("""
        INSERT INTO transactions
        (type, amount, category, description)
        VALUES (?, ?, ?, ?)
        """, (transaction_type, amount, category, description))

        conn.commit()

        print("Transaction added successfully!")


    # 2. View Transactions
    elif choice == "2":

        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()

        if not transactions:
            print("No transactions found.")

        else:
            print("\n===== ALL TRANSACTIONS =====")

            for transaction in transactions:
                print(
                    "ID:", transaction[0],
                    "|", transaction[1],
                    "| ₹", transaction[2],
                    "|", transaction[3],
                    "|", transaction[4]
                )


    # 3. View Summary
    elif choice == "3":

        cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = 'income'
        """)

        income = cursor.fetchone()[0] or 0

        cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = 'expense'
        """)

        expense = cursor.fetchone()[0] or 0

        balance = income - expense

        print("\n===== SUMMARY =====")
        print("Total Income  :", income)
        print("Total Expense :", expense)
        print("Balance       :", balance)


    # 4. Delete Transaction
    elif choice == "4":

        transaction_id = int(input("Enter transaction ID: "))

        cursor.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,)
        )

        conn.commit()

        print("Transaction deleted successfully!")


    # 5. Exit
    elif choice == "5":

        print("Thank you for using Expense Tracker!")
        break


    else:
        print("Invalid choice!")


conn.close()