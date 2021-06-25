st = "Hello"

codes = []
for c in st:
    codes.append(ord(c))

print(codes)

# List Comprehension
codes = [ord(c) for c in st]
print(codes)

# List Comprehension with condition
codes = [ord(c) for c in st if c.islower()]
print(codes)