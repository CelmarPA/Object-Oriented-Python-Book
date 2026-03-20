# account.py

# Account class
# Errors indicated by "raise" statements

# Define a custom exception
class AbortTransaction(Exception):
    """
    Raise this exception to abort a bank transaction
    """
    pass


class Account:

    def __init__(self, name: str, balance: str, password: str):
        self.name: str = name
        self.balance: int = self.validate_amount(balance)
        self.password: str = password

    def validate_amount(self, amount: str) -> int:
        try:
            amount = int(amount)

        except ValueError:
            raise AbortTransaction("Amount must be an integer")

        if amount <= 0:
            raise  AbortTransaction("Amount must be positive")

        return amount

    def check_password_match(self, password: str) -> None:
        if password != self.password:
            raise AbortTransaction("Incorrect password for this account")

    def deposit(self, amount_to_deposit: str) -> int:
        amount_to_deposit: int = self.validate_amount(amount_to_deposit)

        self.balance += amount_to_deposit

        return self.balance

    def get_balance(self) -> int:
        return self.balance

    def withdraw(self, amount_to_withdraw: str) -> int:
        amount_to_withdraw: int = self.validate_amount(amount_to_withdraw)

        if amount_to_withdraw > self.balance:
            raise AbortTransaction("You cannot withdraw more than you have in your account")

        self.balance -= amount_to_withdraw

        return self.balance

    # Added for debugging
    def show(self):
        print(f"        Name: {self.name}")
        print(f"        Balance: {self.balance}")
        print(f"        Password: {self.password}")
















