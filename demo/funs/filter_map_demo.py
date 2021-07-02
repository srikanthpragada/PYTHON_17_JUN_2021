def gettotal(st):
    values = st.split(",")
    marks = filter(str.isdigit, values)
    return sum(map(int, marks))


marks = ["90,87,88", "87,77,,90", "65,55,78,ten"]

for s in map(gettotal, marks):
    print(s)
