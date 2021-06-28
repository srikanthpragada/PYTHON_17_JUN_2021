langs = {'java': (1995, 'James'),
         'python': (1995, 'Van'),
         'c#': (2000, 'Anders')}

for k in langs.keys():
    print(k, langs[k])

for k, v in sorted(langs.items()):
    print(k, v[1])
