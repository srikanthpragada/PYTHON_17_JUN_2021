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
print(a1.getbalance())

a2 = Account(2, "Mark")
a2.show()
