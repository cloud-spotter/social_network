from lib.book import *

"""
Book constructs with an id, title and author_name
"""

def test_book_constructs():
    book = Book(1, "Test Title", "Test Author Name")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author Name"

"""
Format books to strings nicely
"""
def test_format_books_nicely():
    book = Book(1, "Test Title", "Test Author Name")
    assert str(book) == "Book(1, Test Title, Test Author Name)"

"""
Compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author Name")
    book2 = Book(1, "Test Title", "Test Author Name")
    assert book1 == book2

