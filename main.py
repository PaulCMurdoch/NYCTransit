import sqlite3

from extract import extract
from transform import transform
from load import load_station, load_ridership

conn = sqlite3.connect("data/omny.db")
cursor = conn.cursor()

BATCH_SIZE = 50000

for batch in extract(
    batch_size=BATCH_SIZE,
    limit=1000000,
    oldest_timestamp="2026-08-01T00:00:00.000"
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