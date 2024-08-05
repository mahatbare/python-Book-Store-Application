from .models import Author, Book, Customer, Purchase

def add_author(session, name):
    author = Author(name=name)
    session.add(author)
    session.commit()

def add_book(session, title, page_count, author_id):
    book = Book(title=title, page_count=page_count, author_id=author_id)
    session.add(book)
    session.commit()

def add_customer(session, name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()

def purchase_book(session, customer_id, book_id):
    purchase = Purchase(customer_id=customer_id, book_id=book_id)
    session.add(purchase)
    session.commit()
