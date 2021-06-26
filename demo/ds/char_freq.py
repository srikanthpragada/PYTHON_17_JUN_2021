
st = "Java and Java EE"

for c in sorted(set(st)):
    print(f"{c} - {st.count(c)}")
