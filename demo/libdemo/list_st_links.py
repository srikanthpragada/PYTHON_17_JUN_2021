import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
response = requests.get(WEBSITE)

bs = BeautifulSoup(response.text, "html.parser")

for link in bs.find_all("a"):
    if 'href' not in link.attrs:
        continue

    href = link['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        href = WEBSITE + "/" + href

    print(href)
