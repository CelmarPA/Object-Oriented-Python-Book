# main_bank_version_6.py

# Main program for controlling a Bank made up of Accounts

from bank import *


#Create an instance of the Bank
o_bank: Bank = Bank("9 to 17", "123 Main Street, Anytown, USA", "(650) 555-1212")

# Main code
while True:
    print()
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To get bank information, press i")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w")
    print()

    action = input("What do you want to do? ").lower()[0]   # grab the first letter
    print()

    try:
        if action == "b":
            o_bank.balance()

        elif action == "c":
            o_bank.close_account()

        elif action == "d":
            o_bank.deposit()

        elif action == "i":
            o_bank.get_info()

        elif action == "o":
            o_bank.open_account()

        elif action == "q":
            break

        elif action == "s":
            o_bank.show()

        elif action == "w":
            o_bank.withdraw()

    except AbortTransaction as error:
        # Print out the text of the error message
        print(error)

print("Done")
