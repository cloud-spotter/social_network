class Account:
    def __init__(self, id, email, user_name):
        self.id = id
        self.email = email
        self.user_name = user_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Account({self.id}, {self.email}, {self.user_name})"
    