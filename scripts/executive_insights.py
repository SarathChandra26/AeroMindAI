import pandas as pd

routes = pd.read_csv(
    "data/top_revenue_routes.csv"
)

forecast = pd.read_csv(
    "data/revenue_forecast.csv"
)

top_route = (
    routes.iloc[0]
)

current_revenue = (
    forecast["forecast_revenue"].iloc[0]
)

future_revenue = (
    forecast["forecast_revenue"].iloc[-1]
)

growth = (
    (
        future_revenue -
        current_revenue
    )
    /
    current_revenue
) * 100

insights = f"""
AEROMIND AI EXECUTIVE REPORT

Top Performing Route:
{top_route['source_airport']} -> {top_route['destination_airport']}

Revenue:
₹{top_route['revenue']:,.0f}

Profit:
₹{top_route['profit']:,.0f}

Passengers:
{top_route['passengers']:,.0f}

Forecasted Revenue Trend:
Projected growth of {growth:.2f}%

Recommendation:
Increase capacity on high-demand routes.
Monitor low-profit routes for optimization.
Focus on revenue growth opportunities.
"""

print(insights)

with open(
    "data/executive_report.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(insights)