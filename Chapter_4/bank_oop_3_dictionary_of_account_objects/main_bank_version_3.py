# main_bank_version_4.py

# Test program using accounts
# Version 3, using a dictionary of accounts

# Bring in all the code from the Account class file
from account import *


# Start off with an empty dictionary of accounts
accounts_dict: dict = {}
next_account_number: int = 0

# Create two accounts
o_account: Account = Account("Joe", 100, "JoesPassword")
joes_account_number: int = next_account_number
accounts_dict[joes_account_number]: Account = o_account
print(f"Account number for Joe is: {joes_account_number}")

next_account_number += 1

o_account: Account = Account("Mary", 12345, "MarysPassword")
marys_account_number: int = next_account_number
accounts_dict[marys_account_number]: Account = o_account
print(f"Account number for Mary is: {marys_account_number}")

next_account_number += 1

accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts ...")
accounts_dict[joes_account_number].deposit(50, "JoesPassword")
accounts_dict[marys_account_number].withdraw(345, "MarysPassword")
accounts_dict[marys_account_number].deposit(100, "MarysPassword")

# Show the accounts
accounts_dict[joes_account_number].show()
accounts_dict[marys_account_number].show()

# Create another account with information from the user
print()
user_name: str = input("What is the name for the new user account? ")
user_balance: int = int(input("What is the starting balance for this account? $"))
user_password: str = input("What is the password your want to use for this account? ")

o_account: Account = Account(user_name, user_balance, user_password)
new_account_number: int = next_account_number
accounts_dict[new_account_number]: Account = o_account

print(f"Account number for new account is: {new_account_number}")

next_account_number += 1

# Show the newly created user account
accounts_dict[new_account_number].show()

# Let's deposit 100 into the new account
accounts_dict[new_account_number].deposit(100, user_password)
users_balance: int = accounts_dict[new_account_number].get_balance(user_password)

print()
print(f"After depositing $100, the user's balance is: ${users_balance}")

# SHow the new account
accounts_dict[new_account_number].show()
