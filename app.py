from lib.database_connection import DatabaseConnection
from lib.post_repository import *
from lib.posts import *
from lib.account_repository import *
from lib.account import *

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all posts
posts_repository = PostRepository(connection)
posts = posts_repository.all()

for post in posts:
    print(post)         

# Retrieve all accounts
account_repository = AccountRepository(connection)  
accounts = account_repository.all()

# # List them out
for account in accounts:                            
    print(account)