def get_email(email):
    e = email.strip()
    if len(e) == 0:
        return None

    pos = email.find("@")
    if pos == -1:
        return None

    if pos > 0 and pos < len(email) - 1:
        return e
    else:
        return None


with open("emails.txt", "rt") as f:
    emails = set()
    for line in f:
        parts = line.split(",")
        for p in parts:
            email = get_email(p)
            if email is not None:
                emails.add(email)

# print in sorted order
for email in sorted(emails):
    print(email)
