# main_bank_version_5.py

# Main program for controlling a Bank made up of Accounts

# Bring in all the code of the Bank class
from bank import *


# Create an instance of the Bank
o_bank: Bank = Bank()

# Main code
# Create two test accounts
joes_account_number: int = o_bank.create_account("Joe", 100, "JoesPassword")
print(f"Joe's account number is: {joes_account_number}")

marys_account_number: int = o_bank.create_account("mary", 12345, "MarysPassword")
print(f"Mary's account number is: {marys_account_number}")

while True:
    print()
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w ")
    print()

    action: str = input("What do you want to do? ").lower()[0]
    print()

    if action == "b":
        o_bank.balance()

    elif action == "c":
        o_bank.close_account()

    elif action == "d":
        o_bank.deposit()

    elif action == "o":
        o_bank.open_account()

    elif action == "s":
        o_bank.show()

    elif action == "q":
        break

    elif action == "w":
        o_bank.withdraw()

    else:
        print("Sorry, that was not a valid action. Please try again.")

print("Done")
