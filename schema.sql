CREATE TABLE STATION (
    station_id INTEGER PRIMARY KEY,
    station_name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

CREATE TABLE RIDERSHIP (
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day_of_week TEXT NOT NULL,
    hour_of_day INTEGER NOT NULL,

    origin_station_id INTEGER NOT NULL,
    destination_station_id INTEGER NOT NULL,

    est_avg_ridership REAL,

    PRIMARY KEY (
        year,
        month,
        day_of_week,
        hour_of_day,
        origin_station_id,
        destination_station_id
    ),

    FOREIGN KEY (origin_station_id)
        REFERENCES STATION(station_id),

    FOREIGN KEY (destination_station_id)
        REFERENCES STATION(station_id)
);