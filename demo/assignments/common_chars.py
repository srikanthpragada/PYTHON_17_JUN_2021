def common_char(st1, st2):
    common = set(st1) & set(st2)
    print(sorted(common))


st1 = "Python"
st2 = "tooth"
common_char(st1, st2)
