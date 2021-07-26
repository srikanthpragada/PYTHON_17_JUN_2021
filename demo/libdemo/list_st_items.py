import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com/rss.xml"
response = requests.get(URL)

bs = BeautifulSoup(response.text, "xml")

for item in bs.find_all("item"):
    pubdate = item.find("pubDate").text
    if '2021' not in pubdate:
        break

    print(item.find('title').text.strip())
    print(item.find("link").text.strip())
    print(pubdate)
    print("-" * 50)