import pandas as pd

airports = pd.read_csv(
    "raw_data/airports.csv"
)

print("\nAIRPORTS")
print(airports.shape)

print("\nCOLUMNS")
print(airports.columns.tolist())

print("\nFIRST 5 ROWS")
print(airports.head())