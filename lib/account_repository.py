from lib.account import *

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM accounts ORDER BY id ASC")
        return [
            Account(row["id"], row["email"], row["user_name"])
            for row in rows
        ]
    
    def find(self, account_id):
        rows = self._connection.execute(
            "SELECT * FROM accounts WHERE id = %s", [account_id])
        row = rows[0]
        return Account(row["id"], row["email"], row["user_name"])
    
    def create(self, account) -> None:
        self._connection.execute(
            "INSERT INTO accounts (email, user_name) VALUES (%s, %s)", 
            [account.email, account.user_name]
        )
        return None
    
    def delete(self, account_id) -> None:
        self._connection.execute(
            "DELETE FROM accounts WHERE id = %s",
            [account_id]
        )
        return None
    
    def update(self, account) -> None:
        self._connection.execute(
            "UPDATE accounts SET email = %s, user_name = %s WHERE id = %s",
            [account.email, account.user_name, account.id]
        )
