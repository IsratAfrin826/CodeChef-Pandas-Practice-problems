import pandas as pd
import io

data = """ID,Name,Age,City
1,Alice,25,New York
2,Bob,30,London
3,Charlie,35,Paris
1,Alice,25,New York
4,David,28,Tokyo
2,Bob,30,London
5,Eve,22,Sydney
"""

df = pd.read_csv(io.StringIO(data))

# Remove duplicate rows from the DataFrame
df=df.drop_duplicates()

# Print the DataFrame after removing duplicates
print(df)
