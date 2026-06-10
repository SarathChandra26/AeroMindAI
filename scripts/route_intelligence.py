import sqlite3
import pandas as pd
import json

conn = sqlite3.connect("database/aeromind.db")

flights = pd.read_sql("""
SELECT
    r.origin,
    r.destination,
    SUM(f.revenue) as revenue,
    SUM(f.passengers) as passengers,
    COUNT(*) as flights
FROM flights f
JOIN routes r
ON f.route_id = r.route_id
GROUP BY r.origin, r.destination
""", conn)

flights["route"] = (
    flights["origin"] +
    " → " +
    flights["destination"]
)

top_routes = (
    flights
    .sort_values(
        by="revenue",
        ascending=False
    )
)

output = {
    "top_routes":
    top_routes.to_dict(
        orient="records"
    )
}

with open(
    "frontend/assets/route_data.json",
    "w"
) as f:
    json.dump(output, f)

print("Route intelligence created")