import requests

url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=1"

r = requests.get(url)

print(r.status_code)
print(r.json()[:1])