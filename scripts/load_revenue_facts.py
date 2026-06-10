import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/aeromind.db"
)

revenue = pd.read_csv(
    "data/revenue_facts.csv"
)

revenue.to_sql(
    "revenue_facts",
    conn,
    if_exists="replace",
    index=False
)

print(
    "Revenue fact table loaded"
)

conn.close()