class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def difference(self):
        return self.amount - self.balance

    def __str__(self):
        return f"Insufficient balance [{self.balance}] for a withdraw of [{self.amount}]"


class Account:
    # Constructor
    def __init__(self, acno, customer, balance=0):
        # Object Attributes
        self.acno = acno
        self.customer = customer
        self.__balance = balance  # Private attribute

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            raise InsufficientBalanceError(self.__balance, amount)

        self.__balance -= amount

    def getbalance(self):
        return self.__balance

    def show(self):
        print('Acno      :', self.acno)
        print('Customer  :', self.customer)
        print('Balance   :', self.__balance)


a1 = Account(1, "Scott", 20000)  # Create an object/instance
print(a1.__dict__)
print(a1._Account__balance)
a1.deposit(10000)
a1.deposit(20000)
try:
    a1.withdraw(60000)
except InsufficientBalanceError as ex:
    print("Error : ", ex)
    print("Shortage is : ", ex.difference())

print(a1.getbalance())

a2 = Account(2, "Mark")
a2.show()
