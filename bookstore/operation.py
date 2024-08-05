def list_books(session):
    return session.query(Book).all()

def find_books_by_author(session, author_name):
    return session.query(Book).join(Author).filter(Author.name == author_name).all()
