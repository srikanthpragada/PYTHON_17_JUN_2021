import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
if response.status_code != 200:
    print("Sorry! Could not get details about countries!")
    exit(1)

countries = response.json()  # List of dict

for country in sorted(countries, key=lambda c: c['region']):
    print(f"{country['region']:20}  {country['name']}")
