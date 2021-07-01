def hasupper(s):
    for c in s:
        if c.isupper():
            return True

    return False


names = ["python", "Java", "C", "typescript"]
for n in filter(hasupper, names):
    print(n)
