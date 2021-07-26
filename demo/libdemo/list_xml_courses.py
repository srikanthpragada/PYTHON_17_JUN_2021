from bs4 import BeautifulSoup

f = open("courses.xml", "rt")
bs = BeautifulSoup(f.read(), "xml")
f.close()

for course in bs.find_all("course"):
    print(course.find("title").text)
    print(course.find("duration").text)
