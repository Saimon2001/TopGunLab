#ex1 
#Write a Python class called BankAccount with methods for depositing, withdrawing, and checking the account balance.

class BankAccount:
    def __init__(self, name:str):
        self.name = name
        self.balance = 0

    def depositing(self, balance:float):
        self.balance = self.balance + balance
        print(f"The account of {self.name}, Current balance is ${self.balance}")

    def withdraw(self, sacada:float):
        if sacada > self.balance:
            print("not enough funds")
        else:
            self.balance = self.balance - sacada
            print(f"The account of {self.name}, Current balance is ${self.balance}")

    def check(self):
        print(f"The account of {self.name}, Current account balance is ${self.balance}, you can do deposites or withdraw")
        

bank = BankAccount('Simon')
bank.depositing(5)
bank.depositing(10)
bank.withdraw(6)
bank.check()