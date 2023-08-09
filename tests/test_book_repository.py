from lib.book_repository import *
from lib.book import *

"""
When we call BookRepostiory#all
We get a list of all book objects reflecting the seed data
"""
def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql") #Seed the database with some test data
    print(BookRepository)
    repository = BookRepository(db_connection) # Create a new BookRepository()
    books = repository.all() # Get all the books!

    # Assert results we should see
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]
    assert len(books) == 5

