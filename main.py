import requests

url = "https://data.ny.gov/resource/28vm-gjqr.json?"

def extract(batch_size=5):
    params = {
        "$limit": batch_size,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id" }

    response = requests.get(url, params=params)
    data = response.json()

    while data:
        params["$offset"] += params["$limit"]
        response = requests.get(url, params=params)
        data = response.json()
        
def incremental_load(last_timestamp, batch_size=5):
    params = {
        "$limit": batch_size,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id",
        "$where": f"timestamp > '{last_timestamp}'" }

    response = requests.get(url, params=params)
    data = response.json()

    while data:
        params["$offset"] += params["$limit"]
        response = requests.get(url, params=params)
        data = response.json()
