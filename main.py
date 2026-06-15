from database import connect_db

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

from database import connect_db

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

view_expenses()