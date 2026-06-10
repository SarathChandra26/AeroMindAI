import pandas as pd
import numpy as np

months = pd.date_range(
    start="2023-01-01",
    periods=36,
    freq="M"
)

revenue = []

base = 500000000

for i in range(len(months)):
    growth = i * 10000000
    seasonality = np.sin(i/3) * 50000000
    noise = np.random.randint(
        -10000000,
        10000000
    )

    revenue.append(
        base +
        growth +
        seasonality +
        noise
    )

df = pd.DataFrame({
    "month": months,
    "revenue": revenue
})

df.to_csv(
    "data/revenue_timeseries.csv",
    index=False
)

print(df.head())