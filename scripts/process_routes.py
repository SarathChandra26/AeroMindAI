import pandas as pd

routes = pd.read_csv(
    "raw_data/routes.dat",
    header=None
)

routes = routes.iloc[:, :6]

routes.columns = [
    "airline_code",
    "airline_id",
    "source_airport",
    "source_id",
    "destination_airport",
    "destination_id"
]

routes = routes.dropna()

routes.to_csv(
    "data/routes_clean.csv",
    index=False
)

print(
    f"Routes processed: {len(routes)}"
)

print("\nSample:")
print(routes.head())