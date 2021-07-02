nums = [10, -1, 4, 5, 20, -8, -15]

for n in sorted(nums, key=abs):
    print(n)

names = ["Php", "Java", "c", "Python", "javascript", "C#"]
for n in sorted(names, key=str.upper):
    print(n)
