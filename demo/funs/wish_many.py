def wish(*names, message="Hello"):
    # print(type(names))
    for n in names:
        print(message, n)


wish('Scott', 'Andy')
wish("Joe", "Bob", "Bill", message="Hi")
