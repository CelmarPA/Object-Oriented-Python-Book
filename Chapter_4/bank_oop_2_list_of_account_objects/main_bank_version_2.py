# main_bank_version_4.py

# Test program using accounts
# Version 2, using a list of accounts

# Bring in all the code from the Account class file
from account import *


# Start off with an empty list of accounts
accounts_list: list = []

# Create two accounts
o_account: Account = Account("Joe", 100, "JoesPassword")
accounts_list.append(o_account)
print("Joe's account number is 0")

o_account: Account = Account("Mary", 12345, "MarysPassword")
accounts_list.append(o_account)
print("Mary's account number is 1")

accounts_list[0].show()
accounts_list[1].show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts ...")
accounts_list[0].deposit(50, "JoesPassword")
accounts_list[1].withdraw(345, "MarysPassword")
accounts_list[1].deposit(100, "MarysPassword")

# Show the accounts
accounts_list[0].show()
accounts_list[1].show()

# Create another account with information from the user
print()
user_name: str = input("What is the name for the new user account? ")
user_balance: int = int(input("What is the starting balance for this account? $"))
user_password: str = input("What is the password your want to use for this account? ")

o_account: Account = Account(user_name, user_balance, user_password)
accounts_list.append(o_account)   # append to list of accounts

# Show the newly created user account
print("Created new account, account number is 2")
accounts_list[2].show()

# Let's deposit 100 into the new account
accounts_list[2].deposit(100, user_password)
users_balance: int = accounts_list[2].get_balance(user_password)

print()
print(f"After depositing $100, the user's balance is: ${users_balance}")

# SHow the new account
accounts_list[2].show()

