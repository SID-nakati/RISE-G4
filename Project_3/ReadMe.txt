This Library Book Management System is a simple command-line based application built using Python. It helps manage a small library by allowing users to add, remove, list, issue, and return books. The application uses JSON files to store book and issue data persistently across sessions, making it suitable for basic use cases such as school or personal libraries.

The system allows users to add books with a unique Book ID, title, and author. Each book entry is stored with an availability status. The removal feature lets users delete books from the system using the Book ID. A listing feature displays all the books along with their current status (Available or Issued), making it easy to browse the collection.

For lending operations, the user can issue a book to a student by entering their name. The book is marked as unavailable, and the issue details—including issue date and a due date 14 days later—are saved. The return feature checks if the book was returned late, calculates the delay, and applies a fine of ₹5 per day if applicable. All data related to issued books is maintained in a separate JSON file to track loan records.

To run this application, users need to have Python installed. The program operates entirely through text input in the terminal and requires no additional libraries or frameworks. The system provides an efficient way to manage book circulation and return tracking for small-scale libraries or personal collections, and can be further expanded to include user authentication, search functionality, or a graphical interface for ease of use.

