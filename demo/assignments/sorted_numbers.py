lst = []
while True:
    a = int(input("Enter number [0 to stop] :"))
    if a == 0:
        break

    lst.append(a)

print(sorted(lst))
