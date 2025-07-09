import json
import os
from datetime import datetime
import math as plt
import matplotlib.pyplot as plt


DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g. food, travel, bills): ").capitalize()
        date_str = input("Enter date (YYYY-MM-DD): ")
        datetime.strptime(date_str, "%Y-%m-%d")  # Validate date
        expenses = load_expenses()
        expenses.append({
            "amount": amount,
            "category": category,
            "date": date_str
        })
        save_expenses(expenses)
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input. Try again.\n")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        if exp["date"].startswith(month):
            category = exp["category"]
            summary[category] = summary.get(category, 0) + exp["amount"]
    if summary:
        print(f"\nExpense Summary for {month}:")
        for cat, total in summary.items():
            print(f"{cat}: ₹{total:.2f}")
    else:
        print("No expenses found for that month.")
    return summary

def plot_summary(summary, chart_type="pie"):
    if not summary:
        print("Nothing to plot.")
        return

    categories = list(summary.keys())
    totals = list(summary.values())

    if chart_type == "pie":
        plt.pie(totals, labels=categories, autopct="%1.1f%%")
        plt.title("Expense Distribution")
    elif chart_type == "bar":
        plt.bar(categories, totals, color='skyblue')
        plt.ylabel("Amount (₹)")
        plt.title("Expense by Category")

    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Monthly Summary")
        print("3. Plot Pie Chart")
        print("4. Plot Bar Chart")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            summary = monthly_summary()
            plot_summary(summary, "pie")
        elif choice == "4":
            summary = monthly_summary()
            plot_summary(summary, "bar")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
