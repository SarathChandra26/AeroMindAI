import pandas as pd
import random

routes = pd.read_csv(
    "data/routes_clean.csv"
)

routes = routes.copy()

routes["avg_ticket_price"] = [
    random.randint(3000, 25000)
    for _ in range(len(routes))
]

routes["monthly_passengers"] = [
    random.randint(500, 20000)
    for _ in range(len(routes))
]

routes["monthly_revenue"] = (
    routes["avg_ticket_price"]
    *
    routes["monthly_passengers"]
)

routes["operating_cost"] = (
    routes["monthly_revenue"]
    *
    0.65
)

routes["profit"] = (
    routes["monthly_revenue"]
    -
    routes["operating_cost"]
)

routes.to_csv(
    "data/revenue_facts.csv",
    index=False
)

print("Revenue facts created")

print(routes.head())