with open("emails.txt", "rt") as f:
    emails = set()
    for line in f:
        parts = line.split(",")
        validparts = filter(lambda p: len(p.strip()) > 0, parts)
        emails = emails.union(map(str.strip, validparts))

# print in sorted order
for email in sorted(emails):
    print(email)
