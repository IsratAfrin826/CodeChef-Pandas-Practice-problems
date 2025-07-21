import pandas as pd

# Create a sample DataFrame
data = {'Col A': [10, 20, 30, 40],
        'Column B': ['Apple', 'Banana', 'Cherry', 'Date'],
        'Another Column C': [True, False, True, False]}
df = pd.DataFrame(data)

# Your task is to rename 'Col A' to 'ID' and 'Another Column C' to 'Active'
df=df.rename(columns={'Col A':'ID','Another Column C':'Active'})

# Then reorder the columns to be 'ID', 'Column B', 'Active'
df=df[['ID','Column B','Active']]

# Add the code to rename and reorder the columns here
# Display the DataFrame
print(df)
