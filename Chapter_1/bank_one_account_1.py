# bank_one_account_1.py

# Non-OOP
# Bank Version 1
# Single account

account_name: str = "Joe"
account_balance: int = 100
account_password: str = "soup"

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

        if user_password != account_password:
            print("Incorrect password")

        else:
            print(f"Your balance is: ${account_balance}")

    elif action == "d":
        print("Deposit:")

        user_deposit_amount: int = int(input("Please enter amount to deposit: $"))
        user_password: str = input("Please enter the password: ")

        if user_deposit_amount < 0:
            print("You cannot deposit a negative amount!")

        elif user_password != account_password:
            print('Incorrect password')

        else: # OK
            account_balance += user_deposit_amount
            print(f"Your new balance is: ${account_balance}")

    elif action == "s":  # show
        print("Show:")
        print(f"    Name {account_name}")
        print(f"    Balance: ${account_balance}")
        print(f"    Password: {account_password}")
        print()

    elif action == "q":
        break

    elif action == "w":
        print("Withdraw:")

        user_withdraw_amount: int = int(input("Please enter the amount to withdraw: $"))
        user_password: str = input("Please enter the password: ")

        if user_withdraw_amount < 0:
            print("You cannot withdraw a negative amount")

        elif user_password != account_password:
            print("Incorrect password for this account")

        elif user_withdraw_amount > account_balance:
            print("You cannot withdraw more than you have in your account")

        else:  # OK
            account_balance -= user_withdraw_amount
            print(f"Your new balance is : ${account_balance}")

print('Done')
