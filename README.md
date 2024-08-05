# Phase 3 CLI Project 
Bookstore CLI Application
This is a command-line interface (CLI) application for managing a bookstore. It allows you to manage authors, books, and customers, and track book purchases using a SQLite database with SQLAlchemy ORM.

Features
Add, list, and manage authors
Add, list, and manage books
Add, list, and manage customers
Track book purchases
Simple CLI commands for interaction

Project Structure

bookstore/
│
├── bookstore/
│   ├── __init__.py
│   ├── cli.py
│   ├── database.py
│   ├── models.py
│   └── operations.py
│
├── tests/
│   ├── __init__.py
│   └── test_bookstore.py
│
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/bookstore-cli.git
cd bookstore-cli
Install dependencies using Pipenv:

sh
Copy code
pipenv install
pipenv shell
Initialize the database:

sh
Copy code
python -m bookstore.cli init
Usage
Adding an Author
To add a new author to the database, use the add-author-cli command followed by the author's name.

sh
Copy code
python -m bookstore.cli add-author-cli "Author Name"
Adding a Book
To add a new book to the database, use the add-book-cli command followed by the book title, page count, and author ID.

sh
Copy code
python -m bookstore.cli add-book-cli "Book Title" 123 1
Adding a Customer
To add a new customer to the database, use the add-customer-cli command followed by the customer's name.

sh
Copy code
python -m bookstore.cli add-customer-cli "Customer Name"
Purchasing a Book
To record a book purchase, use the purchase-book-cli command followed by the customer ID and book ID.

sh
Copy code
python -m bookstore.cli purchase-book-cli 1 1
Listing All Books
To list all books in the database, use the list-books-cli command.

sh
Copy code
python -m bookstore.cli list-books-cli
Finding Books by Author
To find books by a specific author, use the find-books-by-author-cli command followed by the author's name.

sh
Copy code
python -m bookstore.cli find-books-by-author-cli "Author Name"
Running Tests
To run the tests, use pytest:

sh
Copy code
pytest
Contributing
Contributions are welcome! Please create an issue or pull request with your suggestions or improvements.