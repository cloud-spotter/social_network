from lib.database_connection import DatabaseConnection
# from lib.artist_repository import ArtistRepository # Update for book_store
from lib.book_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all books
book_repository = BookRepository(connection)
books = book_repository.all()

for book in books:
    print(book)         

# Retrieve all artists
# artist_repository = ArtistRepository(connection)  # Update for book_store
# artists = artist_repository.all()

# # List them out
# for artist in artists:                            # Update for book_store
#     print(artist)


# Examples from music_library seed (music_library project)
# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)