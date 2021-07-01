def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def operation(x, y, task):
    print(task(x, y))


operation(10, 20, add)
operation(10, 20, multiply)
