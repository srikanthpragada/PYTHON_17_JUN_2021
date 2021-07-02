def getcode(s):
    return s[2:]


codes = ["SE123", "DE345", "AE987", "AA383", "EF833"]

for n in sorted(codes, key=getcode):
    print(n)
