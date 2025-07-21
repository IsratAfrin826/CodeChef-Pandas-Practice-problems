import pandas as pd
import io

data = """
Name,Age,City
Alice,25,New York
Bob,30,London
Alice,25,New York
Charlie,35,Paris
Bob,30,Manchester
Alice,28,New York
"""

df = pd.read_csv(io.StringIO(data))

# Remove duplicate rows based on the 'Name' column, keeping the first occurrence
df_no_duplicates = df.drop_duplicates(subset='Name',keep='first')

print(df_no_duplicates.to_csv(index=False).strip())
