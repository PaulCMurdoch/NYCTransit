import requests

url = "https://data.ny.gov/resource/28vm-gjqr.json?$limit=5"

response = requests.get(url)

print(f"Status Code: {response.status_code}")

data = response.json()

for i, row in enumerate(data, start=1):
    print(f"\n{'=' * 50}")
    print(f"ROW {i}")
    print(f"{'=' * 50}")

    for key, value in row.items():
        print(f"{key}: {value}")