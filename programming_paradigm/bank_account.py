class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            withdraw_result = True
        else:
            withdraw_result = False
        return withdraw_result

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")