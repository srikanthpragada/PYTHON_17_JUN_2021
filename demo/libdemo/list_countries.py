import requests

response = requests.get("https://restcountries.eu/rest/v2/all")
if response.status_code != 200:
    print("Sorry! Could not get details about countries!")
    exit(1)


countries = response.json()  # List of dict

for country in countries:
    print(f"{country['name']:50}  {country['capital']}")
