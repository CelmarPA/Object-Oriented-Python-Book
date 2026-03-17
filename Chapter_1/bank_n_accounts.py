# bank_one_account_3.py
# Non-OOP
# Bank Version 4
# Any number of accounts - with lists
from pygments.plugin import iter_entry_points

account_names_list: list = []
account_balances_list: list = []
account_passwords_list: list = []


def new_account(name: str, balance: int, password: str) -> None:
    global account_names_list, account_balances_list, account_passwords_list

    account_names_list.append(name)
    account_balances_list.append(balance)
    account_passwords_list.append(password)


def show(account_number: int) -> None:
    global account_names_list, account_balances_list, account_passwords_list

    print(f"Account {account_number}")
    print(f"    Name {account_names_list[account_number]}")
    print(f"    Balance: ${account_balances_list[account_number]}")
    print(f"    Password: {account_passwords_list[account_number]}")
    print()


def get_balance(account_number: int, password: str) -> int | None:
    global account_names_list, account_balances_list, account_passwords_list

    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None

    return account_balances_list[account_number]


def deposit(account_number: int, amount_to_deposit: int, password: str) -> int | None:
    global account_names_list, account_balances_list, account_passwords_list

    if amount_to_deposit < 0:
        print("You cannot deposit a negative amount!")
        return None

    if password != account_passwords_list[account_number]:
        print("Incorrect password")
        return None

    account_balances_list[account_number] += amount_to_deposit

    return account_balances_list[account_number]


def withdraw(account_number: int, amount_to_withdraw: int, password: str) -> int | None:
    global account_names_list, account_balances_list, account_passwords_list

    if amount_to_withdraw < 0:
        print("You cannot withdraw a negative amount")
        return None

    if password != account_passwords_list[account_number]:
        print("Incorrect password for this account")
        return None

    if amount_to_withdraw > account_balances_list[account_number]:
        print("You cannot withdraw more than you have in your account")
        return None

    account_balances_list[account_number] -= amount_to_withdraw

    return account_balances_list[account_number]


# Create two sample accounts
print("Joe's account is account number:", len(account_names_list))
new_account("Joe", 100, 'soup')

print("Mary's account is account number:", len(account_names_list))
new_account("Mary", 12345, 'nuts')

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press n to create a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
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
        print("Deposit:")
        user_account_number: int = int(input("Please enter your account number: "))
        user_deposit_amount: int = int(input("Please enter amount to deposit: "))
        user_password: str = input("Please enter the password: ")

        new_balance: int = deposit(user_account_number, user_deposit_amount, user_password)

        if new_balance is not None:
            print(f"Your new balance is: ${new_balance}")


    elif action == "n":
        print('New Account:')
        user_name: str = input("What is your name? ")
        user_starting_amount: int = int( input("What is the amount of your initial deposit? "))
        user_password: str = input("What password would you like to use for this account? ")

        user_account_number: int = len(account_names_list)

        new_account(user_name, user_starting_amount, user_password)
        print(f"Your new account number is: {user_account_number}")

    elif action == "s":
        print("Show")
        n_accounts: int = len(account_names_list)

        for account_number in range(n_accounts):
            show(account_number)

    elif action == "q":
        break

    elif action == "w":
        print('Withdraw:')
        user_account_number: int = int(input('Please enter your account number: '))
        user_withdraw_amount: int = int(input('Please enter the amount to withdraw: '))
        user_password: str = input('Please enter the password: ')

        new_balance = withdraw(user_account_number, user_withdraw_amount, user_password)

        if new_balance is not None:
            print('Your new balance is:', new_balance)

print("Done")