import sqlite3
import pandas as pd
import json
import os

os.makedirs("frontend/assets", exist_ok=True)

conn = sqlite3.connect("database/aeromind.db")

df = pd.read_sql(
    "SELECT * FROM flights",
    conn
)

kpis = {
    "total_revenue": float(df["revenue"].sum()),
    "total_passengers": int(df["passengers"].sum()),
    "avg_ticket_price": float(df["ticket_price"].mean()),
    "total_flights": int(len(df))
}

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.strftime("%b")

monthly = (
    df.groupby("month")["revenue"]
    .sum()
    .reset_index()
)

output = {
    "kpis": kpis,
    "monthly_revenue": monthly.to_dict(orient="records")
}

with open(
    "frontend/assets/dashboard_data.json",
    "w"
) as f:
    json.dump(output, f)

print("Dashboard data created successfully!")

conn.close()