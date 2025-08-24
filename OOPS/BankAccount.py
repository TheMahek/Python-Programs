class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited:{amount}")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
    
# Create an Object 
account= BankAccount()
account.deposit(100)
account.withdraw(30)
print("Balance:",account.get_balance())
