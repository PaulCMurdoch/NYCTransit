# MTA Subway Origin-Destination Ridership Estimates Data Pipeline

## Introduction
I chose this dataset because of my interest in public transit. Using MTA origin-destination ridership estimates, this project explores how riders move throughout the New York City subway network through end to end extracting and analyzing.

## Setup
Create database

```python build_db.py```



Run ETL

```python main.py ```

For the analysis run the [Analysis Notebook](analysis.ipynb)

## Data Set Documentation

[MTA Subway Origin-Destination Ridership Estimates Data Pipeline](https://data.ny.gov/Transportation/MTA-Subway-Origin-Destination-Ridership-Estimate-B/28vm-gjqr/about_data)

## ER Diagram
The schema diagram was generated from [schema.dbml](schema.dbml) using [dbdiagram.io](https://dbdiagram.io).

![ER Diagram](img/er_diagram.png)

## Architecture

The project follows a traditional ETL architecture:

1. **Extract** data from the New York State Open Data API.
2. **Transform** records into a normalized table structure.
3. **Load** the transformed data into a SQLite database.

## Limitations
I found that due to the number of Subway Station combinations that my loads were initially not progressing beyond a day even at 1,000,000 rows. This is because the grain of the source data is year * month * days in a week * hours in a day * number of origin/destination pairs. For a simplified representation for each n origin stations there are n-1 destination stations meaning that for a given time frame it is approximately increasing by the square of the number of stations. To have usable results and keep ETL times small I added parameters to decrease the stations, limit the record numbers, and constrain the date range.

## Design Decisions
- A normalized schema was chosen to separate station metadata from ridership measurements.
- The ETL process was split into Extract, Transform, and Load modules for maintainability.
- API pagination and batch processing were used to handle the large volume of source data.