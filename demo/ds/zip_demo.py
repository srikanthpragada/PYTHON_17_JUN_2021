langs = ['Python', "Java", 'C#', "TypeScript"]
years = [1991, 1995, 2000]

for t in zip(langs, years):
    print(t)

for name,year in zip(langs, years):
    print(f"{name:10} {year}")