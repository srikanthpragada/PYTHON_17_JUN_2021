from bs4 import BeautifulSoup

f = open("mycourses.xml", "rt")
bs = BeautifulSoup(f.read(), "xml")
f.close()

for course in bs.find_all("course"):
    print(f"{course['title']:20} {course['duration']:3}")
