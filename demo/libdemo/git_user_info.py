import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code == 200:
    details = response.json()
    for k, v in details.items():
        print(f"{k:20} {v}")
else:
    print("Sorry! Could not get details!")
