import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
response = requests.get(WEBSITE)

bs = BeautifulSoup(response.text, "html.parser")

table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
if table is None:
    print("Sorry! Required table not found!")
    exit(1)

rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all('td')
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    print(f"{title:30} {stdate:10} {timings}")

