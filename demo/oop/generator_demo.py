def numbers():
    for n in range(1, 5):
        print(f'Resuming at {n}')
        yield n


g = numbers()
print(type(g))
print(next(g))
print(next(g))
g2 = numbers()
for v in g2:
    print(v)
