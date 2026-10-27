import sqlite3

from extract import extract
from transform import transform
from load import load_station, load_ridership

def main():
    """ Main function to orchestrate the ETL process. """
    conn = sqlite3.connect("data/omny.db")
    cursor = conn.cursor()

    for batch in extract(
        batch_size=50_000,
        limit=500_000,
        oldest_timestamp=None,
        station_count=30,
        timeout=30
    ):
        print(f"Processing batch of {len(batch)} rows")

        station, ridership = transform(batch)

        load_station(cursor, station)
        load_ridership(cursor, ridership)

        try:
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Error committing transaction: {e}")

    conn.close()

    print("ETL process completed successfully.")
if __name__ == "__main__":
    main()