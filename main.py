python
from models import Book, User, init_db

def main_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Add User")
    print("6. Exit")

def handle_choice(choice):
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        Book.add_book(title, author, isbn)
        print("Book added successfully.")
    elif choice == 2:
        book_id = int(input("Enter book ID to remove: "))
        Book.remove_book(book_id)
        print("Book removed successfully.")
    elif choice == 3:
        keyword = input("Enter search keyword: ")
        books = Book.search_books(keyword)
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Available: {book[4]}")
    elif choice == 4:
        book_id = int(input("Enter book ID to borrow: "))
        user_id = int(input("Enter user ID: "))
        Book.borrow_book(book_id, user_id)
        print("Book borrowed successfully.")
    elif choice == 5:
        name = input("Enter user name: ")
        User.add_user(name)
        print("User added successfully.")
    elif choice == 6:
        print("Exiting...")
        exit()

if __name__ == "__main__":
    init_db()
    while True:
        main_menu()
        choice = int(input("Enter your choice: "))
        handle_choice(choice)
