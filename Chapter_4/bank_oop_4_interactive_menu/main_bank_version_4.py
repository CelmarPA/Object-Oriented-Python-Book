# main_bank_version_4.py

# Interactive test program creating a dictionary of accounts
# Versions 4, with an interactive menu

# Bring in all the code from the Account class file
from account import *


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

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()

    action: str = input("What do you want to do? ").lower()[0]
    print()

    if action == "b":
        print("*** Get Balance ***")

        user_account_number: int = int(input("Please enter your account number: "))
        user_account_password: str = input("Please enter your password: ")

        o_account: Account = accounts_dict[user_account_number]

        the_balance: int = o_account.get_balance(user_account_password)

        if the_balance is not None:
            print(f"Your balance is: ${the_balance}")

    elif action == "d":
        print("*** Deposit ***")

        user_account_number: int = int(input("Please enter your account number: "))
        user_deposit_amount: int = int(input("Please enter the amount to deposit: $"))
        user_account_password: str = input("Please enter your password: ")

        o_account: Account = accounts_dict[user_account_number]

        the_balance: int = o_account.deposit(user_deposit_amount, user_account_password)

        if the_balance is not None:
            print(f"Your new balance is: ${the_balance}")

    elif action == "o":
        print("*** Open Account ***")

        user_name: str = input("What is the name for the new user account? ")
        user_starting_amount: int = int(input("What is the starting balance for this account? $"))
        user_password: str = input("What is the password your want to use for this account? ")

        o_account: Account = Account(user_name, user_starting_amount, user_password)

        accounts_dict[next_account_number]: Account = o_account

        print(f"Your new account number is: {next_account_number}")

        next_account_number += 1
        print()

    elif action == "s":
        print("Show:")
        for user_account_number in accounts_dict:
            o_account: Account = accounts_dict[user_account_number]
            print(f"        Account Number: {user_account_number}")
            o_account.show()

    elif action == "q":
        break

    elif action == "w":
        print("*** Withdraw ***")

        user_account_number: int = int(input("Please enter your account number: "))
        user_withdraw_amount: int = int(input("Please enter the amount to withdraw: $"))
        user_account_password: str = input("Please enter your password: ")

        o_account: Account = accounts_dict[user_account_number]

        the_balance: int = o_account.withdraw(user_withdraw_amount, user_account_password)

        if the_balance is not None:
            print(f"Withdrew: ${user_withdraw_amount}")
            print(f"Your new balance is: ${the_balance}")

    else:
        print("Sorry, that was not a valid action. Please try again.")

    print('Done')
