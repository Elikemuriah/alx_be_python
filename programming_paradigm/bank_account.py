
class BankAccount:
    def __init__(self, initial_Balance=0):
    #Initialize the account with an optional starting balance (default is 0).

        self._Current_Balance = initial_Balance  # Private attribute for encapsulation

    def deposit(self, amount):
        #Add the specified amount to the account balance.

        if amount > 0:
            self._account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        #Deduct the specified amount from the account balance if funds are sufficient.
        
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        #Print the current account balance in a user-friendly format.

        print(f"Current balance: ${self._account_balance:.2f}")
