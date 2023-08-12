from lib.account_repository import *
from lib.account import *

'''
#all returns a list of all records from the seed data
'''
def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    accounts = repository.all()

    assert accounts == [
        Account(1, 'George@hello.com', 'George Orwell'),
        Account(2, 'Ben@hiya.com', 'Ben Almond')
    ]

'''
#find returns a single account
where the account matches the query condition
'''

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    result = repository.find(1)
    result == Account(1, 'George@hello.com', 'George Orwell')

'''
#create makes a new account record entry in the accounts table
and the new account appears in the table when #all is called
'''

def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    account = Account(None, 'jason@hello.com', 'Jason J Jasonson')
    repository.create(account)
    
    assert repository.all() == [
        Account(1, 'George@hello.com', 'George Orwell'),
        Account(2, 'Ben@hiya.com', 'Ben Almond'),       
        Account(3, 'jason@hello.com', 'Jason J Jasonson')
    ]

'''
#delete removes an account entry from the accounts table
and the account does not feature in the list when #all is called
'''
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    assert repository.delete(3) is None
    assert repository.all() == [
        Account(1, 'George@hello.com', 'George Orwell'),
        Account(2, 'Ben@hiya.com', 'Ben Almond')
    ]

'''
#update replaces existing account field data in table
with new data passed to it
'''
def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    account = repository.find(1)
    account.email = "new@email.com"
    repository.update(account) is None
    assert repository.all() == [
        Account(1, 'new@email.com', 'George Orwell'),
        Account(2, 'Ben@hiya.com', 'Ben Almond')        
    ]