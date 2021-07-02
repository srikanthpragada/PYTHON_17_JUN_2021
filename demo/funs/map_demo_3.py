marks = ["90,87,88", "87,77,90", "65,55,78"]

for m in marks:
    values = m.split(",")
    print(values)
    print(sum(map(int, values)))
