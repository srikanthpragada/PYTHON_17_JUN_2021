st = input("Enter password :")

upper = digit = False
for c in st:
    if c.isupper():
        upper = True
    elif c.isdigit():
        digit = True

if upper and digit:
    print("Valid password!")
else:
    print("Not a valid password!")
