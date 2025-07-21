import pandas as pd
import io

data = """Product,Price
A,"$10.50"
B,"$25.00"
C,"$5.75"
D,"$100.00"
"""

df = pd.read_csv(io.StringIO(data))

# Convert the 'Price' column and print the data types
df['Price'] = df['Price'].str.replace('$','',regex=False).astype(float)

print(df.dtypes)
