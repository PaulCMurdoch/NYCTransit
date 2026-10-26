from extract import extract
from transform import transform
from load import load_station, load_ridership

for row in extract():
    station, ridership = transform(row)

    load_station(cursor, station)
    load_ridership(cursor, ridership)

conn.commit()