# Print each word on a separate line
st = "How are you?"

for c in st:
    if c == ' ':
        print()    # Go to next line
    else:
        print(c, end ='')
