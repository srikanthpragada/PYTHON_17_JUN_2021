def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


nums = [4, 5, 2, 8, 7]
for n in nums:
    print(f"{n:2}  {factorial(n):5}")
