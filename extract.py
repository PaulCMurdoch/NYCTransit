import requests

URL = "https://data.ny.gov/resource/28vm-gjqr.json"

def extract(batch_size=50000, limit=0, oldest_timestamp=None,station_count=10,timeout=30):
    """
    Extracts data from the NYC Open Data API in batches.
    """
    params = {
        "$limit": batch_size,
        "$offset": 0,
        "$order": "timestamp DESC, origin_station_complex_id, destination_station_complex_id",
        f"$where": f"origin_station_complex_id < {station_count} and destination_station_complex_id < {station_count}"
    }
    
    if oldest_timestamp:
        params["$where"] += f" and timestamp >= '{oldest_timestamp}'"

    while True:
        try:
            response = requests.get(URL, params=params, timeout=timeout)
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return

        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return

        if not data:
            break

        print(
            f"Extracting {len(data)} rows from offset {params['$offset']}"
        )

        yield data

        params["$offset"] += batch_size

        if limit > 0 and params["$offset"] >= limit:
            break