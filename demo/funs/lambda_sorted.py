codes = ["SE123", "DE345", "AE987", "AA383", "EF833"]

for n in sorted(codes, key=lambda v: v[2:]):
    print(n)

