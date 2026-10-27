import sqlite3

from extract import extract
from transform import transform
from load import load_station, load_ridership

conn = sqlite3.connect("data/omny.db")
cursor = conn.cursor()

batch = []
BATCH_SIZE = 50000

for row in extract(
    batch_size=BATCH_SIZE,
    limit=200000,
    oldest_timestamp="2026-08-01T00:00:00.000"
):
    batch.append(row)

    if len(batch) >= BATCH_SIZE:
        print(f"Processing batch of {len(batch)} rows")

        for batch_row in batch:
            station, ridership = transform(batch_row)
            load_station(cursor, station)
            load_ridership(cursor, ridership)

        conn.commit()
        batch = []

# Process remaining rows
if batch:
    print(f"Processing final batch of {len(batch)} rows")

    for batch_row in batch:
        station, ridership = transform(batch_row)
        load_station(cursor, station)
        load_ridership(cursor, ridership)

    conn.commit()

conn.close()

print("ETL process completed successfully.")