import click
from .db.database import init_db, SessionLocal
from .operations import add_author, add_book, add_customer, purchase_book

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.argument('name')
def add_author_cli(name):
    """Add a new author."""
    session = SessionLocal()
    add_author(session, name)
    click.echo(f"Author {name} added.")

@cli.command()
@click.argument('title')
@click.argument('page_count', type=int)
@click.argument('author_id', type=int)
def add_book_cli(title, page_count, author_id):
    """Add a new book."""
    session = SessionLocal()
    add_book(session, title, page_count, author_id)
    click.echo(f"Book {title} added.")

@cli.command()
@click.argument('name')
def add_customer_cli(name):
    """Add a new customer."""
    session = SessionLocal()
    add_customer(session, name)
    click.echo(f"Customer {name} added.")

@cli.command()
@click.argument('customer_id', type=int)
@click.argument('book_id', type=int)
def purchase_book_cli(customer_id, book_id):
    """Purchase a book."""
    session = SessionLocal()
    purchase_book(session, customer_id, book_id)
    click.echo(f"Customer {customer_id} purchased book {book_id}.")

if __name__ == '__main__':
    cli()

