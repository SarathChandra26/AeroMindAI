import pandas as pd

routes = pd.read_csv(
    "raw_data/routes.dat",
    header=None
)

print("\nROUTES")
print(routes.shape)

print("\nFIRST 5 ROWS")
print(routes.head())