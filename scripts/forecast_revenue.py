import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv(
    "data/revenue_timeseries.csv"
)

series = df["revenue"]

model = ExponentialSmoothing(
    series,
    trend="add"
)

fit = model.fit()

forecast = fit.forecast(12)

forecast_df = pd.DataFrame({
    "month": range(1,13),
    "forecast_revenue": forecast
})

print("\nNEXT 12 MONTH FORECAST\n")

print(forecast_df)

forecast_df.to_csv(
    "data/revenue_forecast.csv",
    index=False
)