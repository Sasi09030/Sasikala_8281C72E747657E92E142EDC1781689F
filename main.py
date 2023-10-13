class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        # Private attributes with an underscore prefix
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self._account_holder_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Account Balance: ${self._account_balance}")

# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.00)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
