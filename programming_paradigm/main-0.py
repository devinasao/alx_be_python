import sys
from bank_account import BankAccount

def main():
    # Start with 0 balance (ALX usually expects 0 unless specified)
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()  # make case-insensitive
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        account.display_balance()

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            account.display_balance()
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
