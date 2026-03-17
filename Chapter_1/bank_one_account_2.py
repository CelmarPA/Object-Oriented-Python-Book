# bank_one_account_2.py

# Non-OOP
# Bank Version 2
# Single account

account_name: str = ""
account_balance: int = 0
account_password: str = ""


def new_account(name: str, balance: int, password: str) -> None:
    global account_name, account_balance, account_password

    account_name =  name
    account_balance = balance
    account_password = password


def show() -> None:
    global account_name, account_balance, account_password

    print(f"    Name {account_name}")
    print(f"    Balance: ${account_balance}")
    print(f"    Password: {account_password}")
    print()


def get_balance(password: str) -> int | None:
    global account_name, account_balance, account_password

    if password != account_password:
        print("Incorrect password")
        return None

    return account_balance

def deposit(amount_to_deposit: int, password: str) -> int | None:
    global account_name, account_balance, account_password

    if amount_to_deposit < 0:
        print("You cannot deposit a negative amount!")
        return None

    if password != account_password:
        print("Incorrect password")
        return None

    account_balance += amount_to_deposit

    return account_balance

def  withdraw(amount_to_withdraw: int, password: str) -> int | None:
    global account_name, account_balance, account_password

    if amount_to_withdraw < 0:
        print("You cannot withdraw a negative amount")
        return None

    if password != account_password:
        print("Incorrect password")
        return None

    if amount_to_withdraw > account_balance:
        print("You cannot withdraw more than you have in your account")
        return None

    account_balance -= amount_to_withdraw

    return account_balance


new_account("Joe", 100, "soup") # create an account

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action: str = input("What do you want to do? ").lower()[0]
    print()

    if action == "b":
        print("Get Balance:")
        user_password: str = input("Please enter the password: ")

        the_balance: int = get_balance(user_password)

        if the_balance is not None:
            print(f"Your balance is: ${the_balance}")

    elif action == "d":
        print("Deposit")
        user_deposit_amount: int = input("Please enter amount to deposit: $")
        user_password: str = input("Please enter the password: ")

        new_balance: int = deposit(user_deposit_amount, user_password)

        if new_balance is not None:
            print(f"Your new balance is: ${new_balance}")

    elif action == "s":  # show
        print("Show:")
        show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")

        user_withdraw_amount: int = int(input("Please enter the amount to withdraw: $"))
        user_password: str = input("Please enter the password: ")

        new_balance: int = withdraw(user_withdraw_amount, user_password)

        if new_balance is not None:
            print(f"Your new balance is : ${new_balance}")


print('Done')