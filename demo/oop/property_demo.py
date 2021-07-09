class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def category(self):
        if self.age < 20:
            return "Child"
        elif self.age < 50:
            return "Young"
        else:
            return "Old"


p = Person("James", 67)
print(p.name)
print(p.category)    # p.category()
