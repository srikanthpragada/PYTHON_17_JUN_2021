# Extract mobile numbers from mobiles.txt and print them in sorted order
import re

mobiles = []
f = open("mobiles.txt", "rt")
content = f.read()
f.close()

numbers = re.findall(r"\d+", content)
for n in sorted(filter(lambda v: len(v) == 10, numbers)):
    print(n)
