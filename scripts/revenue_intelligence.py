import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/aeromind.db"
)

query = """
SELECT
source_airport,
destination_airport,
SUM(monthly_revenue) as revenue,
SUM(profit) as profit,
SUM(monthly_passengers) as passengers
FROM revenue_facts
GROUP BY
source_airport,
destination_airport
ORDER BY revenue DESC
LIMIT 20
"""

df = pd.read_sql(
    query,
    conn
)

print("\nTOP REVENUE ROUTES\n")

print(df)

df.to_csv(
    "data/top_revenue_routes.csv",
    index=False
)

conn.close()