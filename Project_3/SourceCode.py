import json
import os
from datetime import datetime, timedelta

BOOK_FILE = "books.json"
ISSUE_FILE = "issued.json"
FINE_PER_DAY = 5  # ₹5 per day fine

# Utility functions
def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Book Functions
def add_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book already exists.")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    books[book_id] = {"title": title, "author": author, "available": True}
    save_data(BOOK_FILE, books)
    print("Book added successfully.")

def remove_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        save_data(BOOK_FILE, books)
        print("Book removed.")
    else:
        print("Book ID not found.")

def list_books():
    books = load_data(BOOK_FILE)
    print("\nAvailable Books:")
    for book_id, info in books.items():
        status = "Available" if info["available"] else "Issued"
        print(f"{book_id}: {info['title']} by {info['author']} [{status}]")

# Issue/Return Functions
def issue_book():
    books = load_data(BOOK_FILE)
    issued = load_data(ISSUE_FILE)

    book_id = input("Enter Book ID to issue: ")
    if book_id not in books or not books[book_id]["available"]:
        print("Book not available.")
        return

    student = input("Enter student name: ")
    issue_date = datetime.now().strftime("%Y-%m-%d")
    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")  # 14 day loan

    issued[book_id] = {
        "student": student,
        "issue_date": issue_date,
        "due_date": due_date
    }

    books[book_id]["available"] = False
    save_data(BOOK_FILE, books)
    save_data(ISSUE_FILE, issued)

    print(f"Book issued to {student}. Due date: {due_date}")

def return_book():
    books = load_data(BOOK_FILE)
    issued = load_data(ISSUE_FILE)

    book_id = input("Enter Book ID to return: ")
    if book_id not in issued:
        print("Book was not issued.")
        return

    return_date = datetime.now()
    due_date = datetime.strptime(issued[book_id]["due_date"], "%Y-%m-%d")
    days_late = (return_date - due_date).days

    fine = FINE_PER_DAY * days_late if days_late > 0 else 0
    if fine > 0:
        print(f"Book is {days_late} days late. Fine: ₹{fine}")
    else:
        print("Book returned on time. No fine.")

    books[book_id]["available"] = True
    del issued[book_id]

    save_data(BOOK_FILE, books)
    save_data(ISSUE_FILE, issued)

# Main Menu
def main():
    while True:
        print("\n=== Library Book Management ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Goodbye \nSee you Soon")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
1