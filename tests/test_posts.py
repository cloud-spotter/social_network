from lib.posts import *

'''
Constructs with an id, title, content, views and Post_id
'''
def test_constructs():
    post = Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 2)
    assert post.id == 1
    assert post.title == 'Tomatoes'
    assert post.content == 'Growing tomatoes test'
    assert post.views == 3
    assert post.account_id == 2

'''
Check two identical post records register as equal
'''
def test_two_posts_are_equal():
    post1 = Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 2)
    post2 = Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 2)
    assert post1 == post2

'''
Format posts nicely
'''
def test_format_posts_nicely():
    post = Post(1, 'Tomatoes', 'Growing tomatoes test', 3, 2) 
    assert str(post) == 'Post(1, Tomatoes, Growing tomatoes test, 3, 2)'