import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv(
    "data/passenger_timeseries.csv"
)

series = df["passengers"]

model = ExponentialSmoothing(
    series,
    trend="add"
)

fit = model.fit()

forecast = fit.forecast(12)

forecast_df = pd.DataFrame({
    "month": range(1,13),
    "forecast_passengers": forecast
})

print("\nPASSENGER FORECAST\n")

print(forecast_df)

forecast_df.to_csv(
    "data/passenger_forecast.csv",
    index=False
)