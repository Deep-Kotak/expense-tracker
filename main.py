from database import connect_db
import csv


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

    if len(expenses) == 0:
        print("No Expenses Found!")

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


def expense_summary():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\n===== EXPENSE SUMMARY =====")
    print(f"Total Expense: ₹{total}")

    print("\nCategory Wise Summary")

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()

    for row in data:
        print(f"{row[0]} : ₹{row[1]}")

    conn.close()


def export_to_csv():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Amount",
            "Category",
            "Date"
        ])

        writer.writerows(expenses)

    print("Expenses Exported Successfully!")

    conn.close()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Expense Summary")
    print("6. Export to CSV")
    print("7. Exit")

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
        expense_summary()

    elif choice == "6":
        export_to_csv()

    elif choice == "7":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")