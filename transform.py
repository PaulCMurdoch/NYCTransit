def transform(rows):
    stations = {}
    ridership = []

    for row in rows:
        # Station Table
        origin_id = int(row["origin_station_complex_id"])
        destination_id = int(row["destination_station_complex_id"])

        stations[origin_id] = {
            "station_id": origin_id,
            "station_name": row["origin_station_complex_name"],
            "latitude": float(row["origin_latitude"]),
            "longitude": float(row["origin_longitude"])
        }

        stations[destination_id] = {
            "station_id": destination_id,
            "station_name": row["destination_station_complex_name"],
            "latitude": float(row["destination_latitude"]),
            "longitude": float(row["destination_longitude"])
        }

        # Ridership Table
        ridership.append({
            "year": int(row["year"]),
            "month": int(row["month"]),
            "day_of_week": row["day_of_week"],
            "hour_of_day": int(row["hour_of_day"]),
            "origin_station_id": origin_id,
            "destination_station_id": destination_id,
            "est_avg_ridership": float(row["estimated_average_ridership"])
        })
    return list(stations.values()), ridership