import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bookstore.models import Base, Author, Book, Customer, Purchase
from bookstore.operations import add_author, add_book, add_customer, purchase_book

DATABASE_URL = "sqlite:///test_bookstore.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='module')
def session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_add_author(session):
    add_author(session, "Author A")
    author = session.query(Author).filter_by(name="Author A").first()
    assert author is not None

def test_add_book(session):
    add_author(session, "Author B")
    author = session.query(Author).filter_by(name="Author B").first()
    add_book(session, "Book B", 123, author.id)
    book = session.query(Book).filter_by(title="Book B").first()
    assert book is not None

def test_add_customer(session):
    add_customer(session, "Customer A")
    customer = session.query(Customer).filter_by(name="Customer A").first()
    assert customer is not None

def test_purchase_book(session):
    add_author(session, "Author C")
    author = session.query(Author).filter_by(name="Author C").first()
    add_book(session, "Book C", 123, author.id)
    add_customer(session, "Customer B")
    customer = session.query(Customer).filter_by(name="Customer B").first()
    book = session.query(Book).filter_by(title="Book C").first()
    purchase_book(session, customer.id, book.id)
    purchase = session.query(Purchase).filter_by(customer_id=customer.id, book_id=book.id).first()
    assert purchase is not None
