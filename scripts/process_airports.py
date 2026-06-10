import pandas as pd

airports = pd.read_csv(
    "raw_data/airports.csv"
)

# Keep useful columns
airports = airports[
    [
        "iata_code",
        "name",
        "municipality",
        "iso_country",
        "latitude_deg",
        "longitude_deg"
    ]
]

# Remove airports without IATA code
airports = airports.dropna(
    subset=["iata_code"]
)

airports.columns = [
    "airport_code",
    "airport_name",
    "city",
    "country",
    "latitude",
    "longitude"
]

airports.to_csv(
    "data/airports_clean.csv",
    index=False
)

print(
    f"Airports processed: {len(airports)}"
)

print("\nSample:")
print(airports.head())