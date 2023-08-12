from lib.post_repository import *
from lib.posts import *

'''
#all returns a list of all records from the seed data
'''
def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 1),
        Post(2, 'Post 2', 'Post 2 content', 24, 2),  
    ]

# '''
# #find returns a single post
# where the post matches the query condition
# '''

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.find(1)
    result = Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 2)

# '''
# #create makes a new post record entry in the posts table
# and the new post appears in the table when #all is called
# '''

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(3, 'Pumpkins', 'Growing Pumkins in Alaska', 7, 1)
    repository.create(post)
    
    assert repository.all() == [
        Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 1),
        Post(2, 'Post 2', 'Post 2 content', 24, 2),
        Post(3, 'Pumpkins', 'Growing Pumkins in Alaska', 7, 1)       
    ]

# '''
# #delete removes an post entry from the posts table
# and the post does not feature in the list when #all is called
# '''
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    assert repository.delete(3) is None
    assert repository.all() == [
        Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 1),
        Post(2, 'Post 2', 'Post 2 content', 24, 2)
    ]

# '''
# #update replaces existing post field data in table
# with new data passed to it
# '''
# def test_update(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = PostRepository(db_connection)
#     post = repository.find(1)
#     post.title = "Growing Tomatoes in Iceland"
#     repository.update(post) is None
#     assert repository.all() == [
#         Post(1, 'Tomatoes', "Growing Tomatoes in Iceland", 3, 2),
#         Post(2, 'Post 2', 'Post 2 content', 24, 2)        
#     ]