g = 1000  # Global variable


def f1():
    global g
    e = 100  # Enclosing variable
    print("In f1()")
    g = 2000

    # Local function
    def f2():
        nonlocal e
        l = 200
        e = 10
        print("In f2()")
        print(g, e, l)

    f2()
    print(e)


f1()
