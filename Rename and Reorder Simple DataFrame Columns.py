import pandas as pd
import io

data = """Old_Name_A,Another_Column,Original_B,Extra_C
1,10,100,1000
2,20,200,2000
3,30,300,3000
"""

df = pd.read_csv(io.StringIO(data))

# Rename columns
df = df.rename(columns={'Old_Name_A':'New_Column_A','Original_B':'Renamed_B'})


# Reorder columns
df=df[['Renamed_B', 'New_Column_A', 'Another_Column', 'Extra_C']]

print(df.to_csv(index=False))
