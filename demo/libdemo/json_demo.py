import json


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)


# Object to JSON
e = Employee("Abc", 100000)
json_st = json.dumps(e.__dict__)
print(json_st)

# JSON to Object
e_dict = json.loads(json_st)
ne = Employee(e_dict['name'], e_dict['salary'])
ne.show()
