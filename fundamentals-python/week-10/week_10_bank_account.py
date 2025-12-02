# Project:
# Simple Bank Account Class. Create a BankAccount class. 
# Each account should have an owner name and a balance.
# The class should have methods to deposit() money, withdraw() money (don't allow withdrawal if funds are insufficient), 
# and display_balance().

class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += float(amount)
        print("You deposited $%.2f." % amount)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= float(amount)
        print("You withdrew $%.2f" % amount)

    def display_balance(self):
        print("Your balance is $%.2f." % self.balance)


my_bank_account = BankAccount("Madina", 100000)
my_bank_account.display_balance()
my_bank_account.deposit(25000)
my_bank_account.display_balance()
my_bank_account.withdraw(130000)
my_bank_account.display_balance()