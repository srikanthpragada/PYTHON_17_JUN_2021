# Word Frequency using dict
import re

f = open(r"c:\classroom\old_man.txt", "rt")
content = f.read()
f.close()

words = re.findall(r"\w+", content)
word_freq = {}

for w in words:
    if w in word_freq:
        word_freq[w] += 1  # Increment count
    else:
        word_freq[w] = 1  # New word add with count 1

for w, c in sorted(word_freq.items()):
    print(f"{w:10} - {c:3}")
