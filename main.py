import sqlite3

from extract import extract
from transform import transform
from load import load_station, load_ridership

conn = sqlite3.connect("data/omny.db")
cursor = conn.cursor()

for row in extract():
    station, ridership = transform(row)
    load_station(cursor, station)
    load_ridership(cursor, ridership)

conn.commit()
conn.close()
print("ETL process completed successfully.")