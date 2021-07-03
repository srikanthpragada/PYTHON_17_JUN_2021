def zero(n):
    print("Before ", id(n))
    n = 0
    print("After  ", id(n))


def prepend(lst, value):
    lst.insert(0, value)


a = 100
print(id(a))
zero(a)
print(id(a))
print(a)

nums = [1, 2, 3]
prepend(nums, 10)
print(nums)
