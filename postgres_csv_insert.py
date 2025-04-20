import csv
import pandas as pd
import psycopg2
from psycopg2 import sql

# Drop Null Values
df = pd.read_csv("Meteorite_Landings.csv")
df.dropna(inplace=True)
df["year"] = df["year"].astype(int)
df.to_csv("modified_data.csv", index=False)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="postgres", host="localhost", port=5432
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Drop the table if it exists
drop_table_query = """
    DROP TABLE IF EXISTS meteorites
"""
cur.execute(drop_table_query)
conn.commit()

# Create the table to store the data
create_table_query = """
    CREATE TABLE meteorites (
        name TEXT,
        id INTEGER PRIMARY KEY,
        nametype TEXT,
        recclass TEXT,
        mass NUMERIC,
        fall TEXT,
        year INTEGER,
        reclat NUMERIC,
        reclong NUMERIC,
        geolocation VARCHAR
    )
"""
cur.execute(create_table_query)
conn.commit()

# Read the CSV file and insert data into the table
with open("modified_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        # Prepare the SQL INSERT statement
        insert_query = sql.SQL(
            """
            INSERT INTO meteorites (name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        )
        # Execute the INSERT statement
        cur.execute(
            insert_query,
            (
                row[0],
                int(row[1]),
                row[2],
                row[3],
                float(row[4]),
                row[5],
                int(row[6]),
                float(row[7]),
                float(row[8]),
                row[9],
            ),
        )
    # Commit the transaction
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
