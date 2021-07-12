class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)

    def getsalary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, hraper):
        super().__init__(name, salary)
        self.hraper = hraper

    # Overriding
    def show(self):
        super().show()
        print(self.hraper)

    def getsalary(self):
        salary = super().getsalary()
        return salary + self.salary * self.hraper / 100


e = Employee("Joe", 45000)
e.show()
m = Manager("Shaw", 70000, 20)
m.show()
