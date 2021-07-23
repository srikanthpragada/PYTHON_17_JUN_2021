import requests

response = requests.get("https://api.github.com/users/srikanthpragada/repos")
if response.status_code != 200:
    print("Sorry! Could not get details about repos!")
    exit(1)


repos = response.json()  # List of dict

for repo in repos:
    print(repo['name'])
