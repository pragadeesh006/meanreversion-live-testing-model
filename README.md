# meanreversion-live-testing-model
This is a mean reversion model that is ready to deploy.
Uses 5paisa api to send buy/sell orders based on model forecasts.

This model uses multiple indicators as conditioning factors to forecast reversions.

model description:
checks if past 15 candles are above vwap-to confirm trend.
buy signal--->sees if price is in extremes of BB bands and rsi above 55 or below 45 to enter.
sell signal--->price movement to the other side of the BB band contrary to the entry side.
