def upper(s):
    return s.strip().upper()

names = ["  python ", "Java   ", "   C", "typescript"]

for v in map(len, names):
    print(v)


for v in map(upper, names):
    print(v)