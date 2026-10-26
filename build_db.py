import sqlite3
from pathlib import Path

# Create data folder if needed
Path("data").mkdir(exist_ok=True)

# Create database
conn = sqlite3.connect("data/omny.db")

# Run schema
with open("schema.sql", "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully.")