from lib.account import *

'''
Account constructs with id & user_name
'''
def test_account_constructs():
    account = Account(1, 'hello@hello.com', 'George Orwell')
    assert account.id == 1
    assert account.email == 'hello@hello.com'
    assert account.user_name == 'George Orwell'

'''
Check two identical account records register as equal
'''
def test_two_accounts_are_equal():
    account1 = Account(1, 'hello@hello.com', 'George Orwell')
    account2 = Account(1, 'hello@hello.com', 'George Orwell')
    assert account1 == account2

'''
Format accounts nicely
'''
def test_format_accounts_nicely():
    account =  Account(1, 'hello@hello.com', 'George Orwell')   
    assert str(account) == 'Account(1, hello@hello.com, George Orwell)'
