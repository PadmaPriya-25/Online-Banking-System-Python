# backend.py

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class Customer:
    def __init__(self, username, password, account):
        self.username = username
        self.password = password
        self.account = account
    
    def transfer(self, recipient, amount):
        if self.account.withdraw(amount):
            recipient.account.deposit(amount)
            return True
        else:
            return False

class Transaction:
    @staticmethod
    def create_account(account_number):
        return Account(account_number)
