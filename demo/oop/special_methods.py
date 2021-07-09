class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        # print('__gt__')
        return self.age > other.age

    def __add__(self, other):
        if isinstance(other, int):
            return Person(self.name, self.age + other)
        else:
            raise ValueError("Invalid operation")


p1 = Person("James", 67)  # p1.__init__("James",67)
p2 = Person("Anders", 58)
p3 = Person("James", 67)

print(p1 == p3)  # p1.__eq__(p3)
print(p1 != p3)

print(p1)  # p1.__str__()  or str(p1)
print(p1.__str__())

# print(p1 > p2)  # p1.__gt__(p2)

persons = [Person("Abc", 20), Person("Xyz", 45), Person("Pqr", 34), Person("Def", 19)]

for p in sorted(persons):
    print(p)

print(p1 + 10)  # p1.__add__(10)

for p in sorted(persons, key=lambda p: p.name):
    print(p)
