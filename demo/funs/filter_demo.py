def iseven(n):
    # print(f"Value of n = {n}")
    return n % 2 == 0


nums = [10, 22, 11, 35, 60]
for n in filter(iseven, nums):
    print(n)
