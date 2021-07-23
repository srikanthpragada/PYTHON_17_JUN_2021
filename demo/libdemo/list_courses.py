from bs4 import BeautifulSoup

f = open("courses.html", "rt")
bs = BeautifulSoup(f.read(), "html.parser")
f.close()
print(bs.h1.text)
print(bs.h1.attrs)

for li_tag in bs.find_all("li"):
    print(li_tag.text)
