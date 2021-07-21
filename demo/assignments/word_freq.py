# Word Frequency
import re

f = open(r"c:\classroom\old_man.txt", "rt")
content = f.read()
f.close()

words = re.findall(r"\w+", content)

for w in sorted(set(words)):
    print(f"{w:10} - {words.count(w):3}")
