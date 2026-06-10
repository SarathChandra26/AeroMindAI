import pandas as pd
import random
from datetime import datetime, timedelta

# Airports
airports = pd.DataFrame({
    "airport_code": ["BLR", "DEL", "BOM", "HYD", "MAA"],
    "city": ["Bangalore", "Delhi", "Mumbai", "Hyderabad", "Chennai"]
})

airports.to_csv("data/airports.csv", index=False)

# Routes
routes = pd.DataFrame({
    "route_id": [1,2,3,4,5],
    "origin": ["BLR","BLR","DEL","BOM","HYD"],
    "destination": ["DEL","BOM","MAA","HYD","BLR"]
})

routes.to_csv("data/routes.csv", index=False)

# Flights
records = []

start_date = datetime(2025,1,1)

for i in range(1,501):
    date = start_date + timedelta(days=random.randint(0,365))

    passengers = random.randint(80,220)

    ticket_price = random.randint(3000,12000)

    revenue = passengers * ticket_price

    route_id = random.randint(1,5)

    records.append([
        i,
        route_id,
        date.strftime("%Y-%m-%d"),
        passengers,
        ticket_price,
        revenue
    ])

flights = pd.DataFrame(records,
    columns=[
        "flight_id",
        "route_id",
        "date",
        "passengers",
        "ticket_price",
        "revenue"
    ])

flights.to_csv("data/flights.csv", index=False)

# Bookings
bookings = flights[[
    "flight_id",
    "route_id",
    "date",
    "ticket_price"
]]

bookings.to_csv("data/bookings.csv", index=False)

print("Data generated successfully")