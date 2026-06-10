import sqlite3
import pandas as pd

conn = sqlite3.connect("database/aeromind.db")

df = pd.read_sql(
    "SELECT * FROM flights",
    conn
)

total_revenue = df["revenue"].sum()

total_passengers = df["passengers"].sum()

avg_ticket_price = df["ticket_price"].mean()

print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Passengers: {total_passengers:,}")
print(f"Average Ticket Price: ₹{avg_ticket_price:,.0f}")

conn.close()