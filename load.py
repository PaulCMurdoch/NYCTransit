import sqlite3

def load_station(cursor, stations):
    """ Loads station data into the STATION table in the SQLite database.
    Args:
        cursor (sqlite3.Cursor): The SQLite cursor object.
        stations (list): A list of dictionaries containing station data."""
    for station in stations:
        try:
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
        except sqlite3.Error as e:
            print(f"Error loading station data: {e}")

def load_ridership(cursor, riderships):
    """ Loads ridership data into the RIDERSHIP table in the SQLite database.
    Args:
        cursor (sqlite3.Cursor): The SQLite cursor object.
        riderships (list): A list of dictionaries containing ridership data."""
    for ridership in riderships:
        try:
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
        except sqlite3.Error as e:
            print(f"Error loading ridership data: {e}")
              