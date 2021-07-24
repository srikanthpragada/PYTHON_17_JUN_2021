import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.w3schools.com"
response = requests.get(WEBSITE)

bs = BeautifulSoup(response.text, "html.parser")

for link in bs.find_all("a"):
    if 'href' not in link.attrs:
        continue

    href = link['href']
    if href == '#':
        continue

    if 'javascript:' in href:
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = "/" + href
        href = WEBSITE + href

    print(href)
