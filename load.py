def load_station(cursor, stations):
    for station in stations:
        cursor.execute(
            """
            INSERT OR IGNORE INTO STATION
            (
                station_id,
                station_name,
                latitude,
                longitude
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                station["station_id"],
                station["station_name"],
                station["latitude"],
                station["longitude"]
            )
        )

def load_ridership(cursor, riderships):
    for ridership in riderships:
        cursor.execute(
        """
        INSERT OR REPLACE INTO RIDERSHIP
        (
            year,
            month,
            day_of_week,
            hour_of_day,
            origin_station_id,
            destination_station_id,
            est_avg_ridership
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ridership["year"],
            ridership["month"],
            ridership["day_of_week"],
            ridership["hour_of_day"],
            ridership["origin_station_id"],
            ridership["destination_station_id"],
            ridership["est_avg_ridership"]
        )
    )