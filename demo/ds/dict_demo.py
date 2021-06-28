langs = {'java': 1995, 'python': 1995, 'c#': 2000}

for k in langs.keys():
    print(k)

for k in langs.keys():
    print(k, langs[k])

for k, v in sorted(langs.items()):
    print(k, v)
