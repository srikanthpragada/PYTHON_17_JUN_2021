st = "Java and Java EE"

chars = []
for c in st:
    if c not in chars:
        print(c)
        chars.append(c)
