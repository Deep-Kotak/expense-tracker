from database import connect_db


def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(amount, category, expense_date) VALUES (?, ?, ?)",
        (amount, category, date)
    )

    conn.commit()

    print("Expense Added Successfully!")

    conn.close()


def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    print("\n===== EXPENSE LIST =====\n")

    for expense in expenses:
        print(
            f"ID: {expense[0]} | Amount: ₹{expense[1]} | Category: {expense[2]} | Date: {expense[3]}"
        )

    conn.close()


def update_expense():
    expense_id = int(input("Enter Expense ID to Update: "))

    amount = float(input("Enter New Amount: "))
    category = input("Enter New Category: ")
    date = input("Enter New Date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, expense_date = ?
        WHERE id = ?
    """, (amount, category, date, expense_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Expense Updated Successfully!")
    else:
        print("Expense ID Not Found!")

    conn.close()


def delete_expense():
    expense_id = int(input("Enter Expense ID to Delete: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Expense Deleted Successfully!")
    else:
        print("Expense Not Found!")

    conn.close()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")