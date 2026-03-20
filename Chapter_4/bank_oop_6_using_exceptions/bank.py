# bank.py

# Bank that manages a dictionary of Account objects

from account import *


class Bank:

    def __init__(self, hours: str, address: str, phone: str):
        self.accounts_dict: dict = {}
        self.next_account_number: int = 0
        self.hours: str = hours
        self.address: str = address
        self.phone: str = phone

    def ask_for_valid_account_number(self) -> int:
        account_number: str = input("What is your account number? ")

        try:
            account_number: int = int(account_number)

        except ValueError:
            raise AbortTransaction("The account number must be an integer")

        if account_number not in self.accounts_dict:
            raise AbortTransaction(f"There is no account {account_number}")

        return account_number

    def get_user_account(self) -> Account:
        account_number: int = self.ask_for_valid_account_number()
        o_account: Account = self.accounts_dict[account_number]
        self.ask_for_valid_password(o_account)

        return o_account

    def ask_for_valid_password(self, o_account: Account) -> None:
        password: str = input("Please enter your password: ")
        o_account.check_password_match(password)

    def create_account(self, the_name: str, the_starting_amount: str, the_password: str) -> int:
        o_account: Account = Account(the_name, the_starting_amount, the_password)
        new_account_number: int = self.next_account_number
        self.accounts_dict[new_account_number] = o_account

        # Increment to prepare for the next account to be created
        self.next_account_number += 1

        return new_account_number

    def open_account(self) -> None:
        print(f"*** Open Account ***")

        user_name: str = input("What is your name? ")
        user_starting_amount: str = input("How much money to start your account? $")
        user_password: str = input("What password would you like to use for this account? ")
        user_account_number: int = self.create_account(user_name, user_starting_amount, user_password)

        print(f"Your new account number is: {user_account_number}")

    def close_account(self) -> None:
        print(f"*** Close Account ***")

        user_account_number: int = self.ask_for_valid_account_number()
        o_account: Account = self.accounts_dict[user_account_number]
        self.ask_for_valid_password(o_account)
        the_balance: int = o_account.get_balance()

        print(f"You had, ${the_balance} in your account, which is being returned to you.")

        del self.accounts_dict[user_account_number]

        print("Your account is now closed.")

    def balance(self) -> None:
        print("*** Get Balance ***")

        o_account = self.get_user_account()
        the_balance: int = o_account.get_balance()

        print(f"Your balace is: ${the_balance}")

    def deposit(self) -> None:
        print("*** Deposit ***")

        o_account: Account = self.get_user_account()
        deposit_amount: str = input("Please enter the amount to deposit: $")
        the_balance: int = o_account.deposit(deposit_amount)

        print(f"Deposited: ${deposit_amount}")
        print(f"Your new balance is: ${the_balance}")

    def withdraw(self) -> None:
        print("*** Withdraw ***")

        o_account: Account = self.get_user_account()
        user_amount: str = input("Please enter the amount to withdraw: $")
        the_balance: int = o_account.withdraw(user_amount)

        print(f"Withdrew: ${user_amount}")
        print(f"Your new balance is: ${the_balance}")

    def get_info(self) -> None:
        print(f"Hours: {self.hours}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")

        print(f"We currently have {len(self.accounts_dict)}, account(s) open.")

    # Special method for Bank administrator only
    def show(self) -> None:
        print("*** Show ***")
        print("(This would typically require an admin password)")

        for user_account_number in self.accounts_dict:
            o_account: Account = self.accounts_dict[user_account_number]
            print(f"Account: {user_account_number}")
            o_account.show()
            print()
