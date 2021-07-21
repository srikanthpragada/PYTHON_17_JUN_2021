import re

codes = ["AB123", "DEF39333", "X393X"]

pattern = re.compile(r"([A-Z]+)(\d+)")

for code in codes:
    match = pattern.match(code)
    if match is not None:
        print(f"{match.group(1):5} {match.group(2):8}")