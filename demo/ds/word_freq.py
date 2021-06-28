s = "This is Python. Python has wonderful data structures. Python is simple"

words = s.split()
word_freq = {}

for w in set(words):
    word_freq[w] = words.count(w)

for w, c in sorted(word_freq.items()):
    print(f"{w:10} {c:2}")

