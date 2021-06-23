pos_total = neg_total = 0
for i in range(10):
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    if n > 0:
        pos_total += n
    else:
        neg_total += n

print(f"Positive Total = {pos_total}, Negative Total = {neg_total}")
