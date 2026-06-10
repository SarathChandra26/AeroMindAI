import pandas as pd
import json

routes = pd.read_csv(
    "data/top_revenue_routes.csv"
)

revenue_forecast = pd.read_csv(
    "data/revenue_forecast.csv"
)

passenger_forecast = pd.read_csv(
    "data/passenger_forecast.csv"
)

dashboard = {

    "kpis": {

        "total_revenue":
        float(routes["revenue"].sum()),

        "total_profit":
        float(routes["profit"].sum()),

        "total_passengers":
        int(routes["passengers"].sum())
    },

    "top_routes":
    routes.head(10).to_dict(
        orient="records"
    ),

    "revenue_forecast":
    revenue_forecast.to_dict(
        orient="records"
    ),

    "passenger_forecast":
    passenger_forecast.to_dict(
        orient="records"
    )
}

with open(
    "frontend/assets/dashboard.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        dashboard,
        f,
        indent=4
    )

print(
    "Dashboard JSON generated"
)