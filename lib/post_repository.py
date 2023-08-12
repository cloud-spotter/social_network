from lib.posts import *

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM posts ORDER BY id ASC")
        return [
            Post(row["id"], row['title'], row['content'], row['views'], row['account_id'])
            for row in rows
        ]
    
    def find(self, post_id):
        rows = self._connection.execute(
            "SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row['title'], row['content'], row['views'], row['account_id'])
    
    def create(self, post) -> None:
        self._connection.execute(
            "INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s)", 
            [post.title, post.content, post.views, post.account_id]
        )
        return None
    
    def delete(self, post_id) -> None:
        self._connection.execute(
            "DELETE FROM posts WHERE id = %s",
            [post_id]
        )
        return None