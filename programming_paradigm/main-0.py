import sys
from bank_account import BankAccount

def main():
    # Initialize the bank account
    account = BankAccount()

    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> <amount>")
        print("Operations: deposit, withdraw, display")
        return

    # Retrieve operation and optional amount
    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else None

    # Perform the requested operation
    if operation == "deposit":
        if amount is None:
            print("Please specify an amount to deposit.")
        elif account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit failed. Amount should be positive.")

    elif operation == "withdraw":
        if amount is None:
            print("Please specify an amount to withdraw.")
        elif account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Withdrawal failed. Insufficient funds or invalid amount.")

    elif operation == "display":
        account.display_balance()

    else:
        print("Invalid operation. Available operations: deposit, withdraw, display")

if __name__ == "__main__":
    main()