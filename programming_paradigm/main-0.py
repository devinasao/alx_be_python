from bank_account import BankAccount

def main():
    account = BankAccount()  # start with 0 balance

    while True:
        user_input = input("Enter command (deposit, withdraw, display, exit): ").strip().lower()

        if user_input == "exit":
            print("Exiting...")
            break

        if user_input.startswith("deposit"):
            try:
                amount = float(user_input.split()[1])
                account.deposit(amount)
                account.display_balance()
            except (IndexError, ValueError):
                print("Invalid deposit amount. Usage: deposit <amount>")

        elif user_input.startswith("withdraw"):
            try:
                amount = float(user_input.split()[1])
                if account.withdraw(amount):
                    account.display_balance()
                else:
                    print("Insufficient funds.")
            except (IndexError, ValueError):
                print("Invalid withdraw amount. Usage: withdraw <amount>")

        elif user_input == "display":
            account.display_balance()

        else:
            print("Invalid command. Commands: deposit <amount>, withdraw <amount>, display, exit")

if __name__ == "__main__":
    main()
