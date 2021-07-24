import requests
from bs4 import BeautifulSoup

WEBSITE = "https://tiobe.com/tiobe-index/"
response = requests.get(WEBSITE)

bs = BeautifulSoup(response.text, "html.parser")

table = bs.find(id='top20')
if table is None:
    print("Sorry! Required table not found!")
    exit(1)

rows = table.tbody.find_all("tr")
for row in rows[:10]:
    cols = row.find_all('td')
    lang = cols[4].text
    print(f"{lang}")

