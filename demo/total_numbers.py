
total = 0
for i in range(5):
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    total += n


print(f"Total = {total}")