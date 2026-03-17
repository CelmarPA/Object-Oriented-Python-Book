# bank_one_account_3.py

# Non-OOP
# Bank Version 3
# Two account

account_name_0: str = ""
account_balance_0: int = 0
account_password_0: str = ""
account_name_1: str = ""
account_balance_1: int = 0
account_password_1: str = ""
n_accounts: int = 0


def new_account(account_number: int, name: str, balance: int, password: str) -> None:
    global account_name_0, account_balance_0, account_password_0
    global account_name_1, account_balance_1, account_password_1

    if account_number == 0:
        account_name_0 =  name
        account_balance_0 = balance
        account_password_0 = password

    if account_number == 1:
        account_name_1 =  name
        account_balance_1 = balance
        account_password_1 = password


def show() -> None:
    global account_name_0, account_balance_0, account_password_0
    global account_name_1, account_balance_1, account_password_1

    if account_name_0 != "":
        print(f"    Name {account_name_0}")
        print(f"    Balance: ${account_balance_0}")
        print(f"    Password: {account_password_0}")
        print()

    if account_name_1 != "":
        print(f"    Name {account_name_1}")
        print(f"    Balance: ${account_balance_1}")
        print(f"    Password: {account_password_1}")
        print()


def get_balance(account_number: int, password: str) -> int | None:
    global account_name_0, account_balance_0, account_password_0
    global account_name_1, account_balance_1, account_password_1

    if account_number == 0:
        if password != account_password_0:
            print("Incorrect password")
            return None

        return account_balance_0

    if account_number == 1:
        if password != account_password_1:
            print("Incorrect password")
            return None

        return account_balance_1

    return None


def deposit(account_number: int, amount_to_deposit: int, password: str) -> int | None:
    global account_name_0, account_balance_0, account_password_0
    global account_name_1, account_balance_1, account_password_1

    if account_number == 0:
        if amount_to_deposit < 0:
            print("You cannot deposit a negative amount!")
            return None

        if password != account_password_0:
            print("Incorrect password")
            return None

        account_balance_0 += amount_to_deposit

        return account_balance_0

    if account_number == 1:
        if amount_to_deposit < 0:
            print("You cannot deposit a negative amount!")
            return None

        if password != account_password_1:
            print("Incorrect password")
            return None

        account_balance_1 += amount_to_deposit

        return account_balance_1

    return None


def withdraw(account_number: int, amount_to_withdraw: int, password: str) -> int | None:
    global account_name_0, account_balance_0, account_password_0
    global account_name_1, account_balance_1, account_password_1

    if account_number == 0:
        if amount_to_withdraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        if password != account_password_0:
            print("Incorrect password")
            return None

        if amount_to_withdraw > account_balance_0:
            print("You cannot withdraw more than you have in your account")
            return None

        account_balance_0 -= amount_to_withdraw

        return account_balance_0

    if account_number == 1:
        if amount_to_withdraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        if password != account_password_1:
            print("Incorrect password")
            return None

        if amount_to_withdraw > account_balance_1:
            print("You cannot withdraw more than you have in your account")
            return None

        account_balance_1 -= amount_to_withdraw

        return account_balance_1

    return None


# Create one test account
new_account(n_accounts,"Joe", 100, "soup")
n_accounts = 1

while True:
    print()
    print("Type b to get the balance")
    print("Type d to make a deposit")
    print("Type n to create a new account")
    print("Type w to make a withdrawal")
    print("Type s to show all accounts")
    print("Type q to quit")
    print()

    action: str = input("What do you want to do? ").lower()[0]
    print()

    if action == "b":
        print("Get Balance:")
        user_account_number: int = int(input("Please enter your account number: "))
        user_password: str = input("Please enter the password: ")

        the_balance: int = get_balance(user_account_number, user_password)

        if the_balance is not None:
            print(f"Your balance is: ${the_balance}")

    elif action == "d":
        print("Deposit")
        user_account_number: int = int(input("Please enter your account number: "))
        user_deposit_amount: int = int(input("Please enter amount to deposit: $"))
        user_password: str = input("Please enter the password: ")

        new_balance: int = deposit(user_account_number, user_deposit_amount, user_password)

        if new_balance is not None:
            print(f"Your new balance is: ${new_balance}")

    elif action == "n":
        print("New Account:")
        new_user_name: str = input("What is your name? ")
        new_user_starting_amount: int = int(input("How much money to have to start you account with? "))
        new_user_password: str = input("What password would you like to use for this account? ")

        new_account(n_accounts, new_user_name, new_user_starting_amount, new_user_password)
        print(f"Your new account number is: {n_accounts}")

        n_accounts += 1


    elif action == "s":  # show all
        print("Show:")
        show()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")
        user_account_number: int = int(input("Please enter your account number: "))
        user_withdraw_amount: int = int(input("Please enter the amount to withdraw: $"))
        user_password: str = input("Please enter the password: ")

        new_balance: int = withdraw(user_account_number, user_withdraw_amount, user_password)

        if new_balance is not None:
            print(f"Your new balance is : ${new_balance}")


print('Done')