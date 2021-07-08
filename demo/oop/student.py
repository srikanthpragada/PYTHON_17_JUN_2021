import math


class Student:
    # Class attribute or Static attribute
    taxrate = 12
    fees = {'python': 5000, 'c': 4000, 'java': 6000}

    @staticmethod
    def get_course_fee(course):
        total = Student.fees[course.lower()]
        return math.trunc(total + total * Student.taxrate / 100)

    def __init__(self, admno, name, course='Python'):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return  Student.get_course_fee(self.course)

    def getdue(self):
        return self.totalfee() - self.feepaid

    def show(self):
        print("Admno      :", self.admno)
        print("Name       :", self.name)
        print("Course     :", self.course)
        print("Feepaid    :", self.feepaid)


s = Student(1, "James", "Java")
s.payment(3000)
s.show()
print(s.getdue())
