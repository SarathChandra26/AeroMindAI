import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/aeromind.db"
)

airports = pd.read_csv(
    "data/airports_clean.csv"
)

routes = pd.read_csv(
    "data/routes_clean.csv"
)

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

print("Warehouse loaded successfully")

conn.close()