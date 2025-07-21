import pandas as pd
import io

data = """Employee,Sales,Marketing,IT
Alice,Manager,Analyst,NaN
Bob,Analyst,NaN,Manager
Charlie,NaN,Analyst,Analyst
"""

df = pd.read_csv(io.StringIO(data))

# Use melt to reshape the DataFrame
df_melted = df.melt(id_vars=['Employee'], var_name='Department', value_name='Role')



# Drop rows where the Role is NaN (employee is not in that department)
df_reshaped = df_melted.dropna(subset=['Role'])



print(df_reshaped.to_string(index=False))
