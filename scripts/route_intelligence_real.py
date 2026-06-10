import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/aeromind.db"
)

query = """
SELECT
    source_airport,
    destination_airport,
    COUNT(*) as route_frequency
FROM routes
GROUP BY
    source_airport,
    destination_airport
ORDER BY route_frequency DESC
LIMIT 20
"""

top_routes = pd.read_sql(
    query,
    conn
)

print("\nTOP ROUTES")
print(top_routes)

top_routes.to_csv(
    "data/top_routes.csv",
    index=False
)

conn.close()