import pandas as pd

routes = pd.read_csv(
    "data/top_revenue_routes.csv"
)

scorecard = {
    "Total Revenue":
    routes["revenue"].sum(),

    "Total Profit":
    routes["profit"].sum(),

    "Total Passengers":
    routes["passengers"].sum(),

    "Top Route":
    routes.iloc[0]["source_airport"]
    + " -> " +
    routes.iloc[0]["destination_airport"]
}

for key, value in scorecard.items():
    print(
        f"{key}: {value}"
    )