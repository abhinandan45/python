class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # double underscore = private

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit hua:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Balance kam hai!")
        else:
            self.__balance -= amount
            print("Withdraw hua:", amount)

    def get_balance(self):
        return self.__balance

acc = BankAccount("Abhi", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())