import pandas as pd

# List of values
values = [10, 15, 12, 18, 20]

data_index = pd.date_range(start='2023-01-01', periods=len(values), freq='D')


time_series = pd.Series(values, index=data_index)
print(time_series)
