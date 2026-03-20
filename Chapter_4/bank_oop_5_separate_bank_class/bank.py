# bank.py

# Bank that manages a dictionary of Account objects

from account import *


class Bank:

    def __init__(self):
        self.accounts_dict: dict = {}
        self.next_account_number: int = 0


    def create_account(self, the_name: str, the_starting_amount: int, the_password: str) -> int:
        o_account: Account = Account(the_name, the_starting_amount, the_password)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = o_account

        # Increment to prepare for next account to be created
        self.next_account_number += 1

        return new_account_number

    def open_account(self) -> None:
        print(f"*** Open Account ***")

        user_name: str = input("What is the name for the new user account? ")
        user_starting_amount: int = int(input("What is the starting balance for this account? $"))
        user_password: str = input("What is the password you want to use for this account? ")

        user_account_number: int = self.create_account(user_name, user_starting_amount, user_password)

        print(f"Your new account number is: {user_account_number}")
        print()

    def close_account(self) -> None:
        print(f"*** Close Account ***")
        user_account_number: int = int(input("What is you account number? "))
        user_password: str = input("What is your password? ")

        o_account: Account = self.accounts_dict[user_account_number]
        the_balance: int = o_account.get_balance(user_password)

        if the_balance is not None:
            print(f"You had {the_balance} in your account, which is being returned to you.")

            # Remove user's account from the dictionary of accounts
            del self.accounts_dict[user_account_number]
            print("Your account is now closed.")

    def balance(self):
        print("*** Get Balance ***")

        user_account_number: int = int(input("Please enter your account number: "))
        user_account_password: str = input("Please enter the password: ")

        o_account: Account = self.accounts_dict[user_account_number]
        the_balance: int = o_account.get_balance(user_account_password)

        if the_balance is not None:
            print(f"Your balance is: ${the_balance}")

    def deposit(self):
        print(f"*** Get Balance ***")

        account_number: int = int(input("Please enter your account number: "))
        deposit_amount: int = int(input("Please enter amount to deposit: $"))
        user_account_password: str = input("Please enter the password: ")

        o_account: Account = self.accounts_dict[account_number]
        the_balance: int = o_account.deposit(deposit_amount, user_account_password)

        if the_balance is not None:
            print(f"Your new balance is: ${the_balance}")

    def show(self):
        print(f"*** Show ***")

        for user_account_number in self.accounts_dict:
            o_account:  Account = self.accounts_dict[user_account_number]
            print(f"        Account: {user_account_number}")
            o_account.show()

    def withdraw(self):
        print(f"*** Withdraw ***")

        user_account_number: int = int(input("Please enter your account number: "))
        user_amount: int = int(input("Please enter the amount to withdraw: $"))
        user_account_password: str = input("Please enter the password: ")

        o_account: Account = self.accounts_dict[user_account_number]
        the_balance: int = o_account.withdraw(user_amount, user_account_password)

        if the_balance is not None:
            print(f"Withdrew: ${user_amount}")
            print(f"Your new balance is: ${the_balance}")
