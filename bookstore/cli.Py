@cli.command()
def list_books_cli():
    
    """List all books."""
    session = SessionLocal()
    books = list_books(session)
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Pages: {book.page_count}")

@cli.command()
@click.argument('author_name')
def find_books_by_author_cli(author_name):
    """Find books by author."""
    session = SessionLocal()
    books = find_books_by_author(session, author_name)
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Pages: {book.page_count}")
