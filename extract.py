import requests

url = "https://data.ny.gov/resource/28vm-gjqr.json?"

def extract(batch_size=50000,limit=0,oldest_timestamp=None):
    params = {
        "$limit": batch_size,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id" }
    
    if oldest_timestamp:
        params["$where"] = f"timestamp >= '{oldest_timestamp}'"

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
        if limit > 0 and params["$offset"] >= limit:
            break

