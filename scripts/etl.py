import pandas as pd
import sqlite3

conn = sqlite3.connect("database/aeromind.db")

airports = pd.read_csv("data/airports.csv")
routes = pd.read_csv("data/routes.csv")
flights = pd.read_csv("data/flights.csv")
bookings = pd.read_csv("data/bookings.csv")

# Basic cleaning
flights.drop_duplicates(inplace=True)
flights.fillna(0, inplace=True)

# Load into database
airports.to_sql(
    "airports",
    conn,
    if_exists="replace",
    index=False
)

routes.to_sql(
    "routes",
    conn,
    if_exists="replace",
    index=False
)

flights.to_sql(
    "flights",
    conn,
    if_exists="replace",
    index=False
)

bookings.to_sql(
    "bookings",
    conn,
    if_exists="replace",
    index=False
)

print("ETL completed successfully")

conn.close()