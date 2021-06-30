# Keyword arguments
def details(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def printdetails(name, **kwargs):
    print(name)
    for k, v in kwargs.items():
        print(k, v)


def process(*args, **kwargs):
    print(args)
    print(kwargs)


details(a=10, b=20, c=30, d=40)
details(x=10, y=20)
details(name="Python", year=1991)

printdetails('Python', website="python.org", author='Van')

process(10, 20, 30, a=10, b=100)
