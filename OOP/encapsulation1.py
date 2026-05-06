"""Pratical Use cases for encapsulation in Python

Knowing when and why to use python encapsulation will help you wirte
more modular code.

Financial Calculations and transactions"""

class BankAccount:
    def __init__(self, account_number, initial_balance):
        
        self.account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: ${amount}")
    
    def __record_transaction(self, transaction_type, amount):
        
        self.__transaction_history.append({
            "type": transaction_type,
            "amount": amount,
        })
    
    @property
    def balance(self):
        
        return self.__balance
    
account = BankAccount("123456789", 1000)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(200)
print(account.balance)