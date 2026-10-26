import requests

url = "https://data.ny.gov/resource/28vm-gjqr.json?"

def full_load():
    params = {
        "$limit": 5,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id" }

    response = requests.get(url, params=params)
    data = response.json()

    while data:
        params["$offset"] += params["$limit"]
        response = requests.get(url, params=params)
        data = response.json()
