import pandas as pd
import numpy as np

months = pd.date_range(
    start="2023-01-01",
    periods=36,
    freq="ME"
)

passengers = []

base = 100000

for i in range(len(months)):

    growth = i * 2500

    seasonality = np.sin(i/3) * 10000

    noise = np.random.randint(
        -3000,
        3000
    )

    passengers.append(
        int(
            base +
            growth +
            seasonality +
            noise
        )
    )

df = pd.DataFrame({
    "month": months,
    "passengers": passengers
})

df.to_csv(
    "data/passenger_timeseries.csv",
    index=False
)

print(df.head())