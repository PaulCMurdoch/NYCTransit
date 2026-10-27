import requests

url = "https://data.ny.gov/resource/28vm-gjqr.json?"

def extract(batch_size=5):
    params = {
        "$limit": batch_size,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id" }

    response = requests.get(url, params=params)
    data = response.json()
    response.raise_for_status()

    while data:
        print(f"Extracting {len(data)} rows from offset {params['$offset']}")
        yield data
        params["$offset"] += params["$limit"]
        response = requests.get(url, params=params)
        data = response.json()
        response.raise_for_status()
        if params["$offset"] >= 10:
            break
