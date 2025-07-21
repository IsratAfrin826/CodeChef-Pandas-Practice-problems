import pandas as pd

# Define the start date
start_date = '2023-01-01'

# Create a date range for 7 days
dates = pd.date_range(start=start_date, periods=7, freq='D')

# Sample temperature values (replace with your own)
temperatures = [25, 26, 24, 27, 28, 25, 26]

# Create a pandas Series with the dates as the index
temperature_series = pd.Series(temperatures, index=dates)

# Print the time series
print(temperature_series)
