import pandas as pd

# Create a sample DataFrame with a column of numbers stored as strings
data = {'Item': ['Apple', 'Banana', 'Orange', 'Grape'],
        'Quantity_Str': ['10', '5', '8', '12']}
df = pd.DataFrame(data)

# View the data types of the columns
print("Original data types:")
print(df.dtypes)

# Now, convert the 'Quantity_Str' column to an integer data type
df['Quantity_Str'] = df['Quantity_Str'].astype(int)

# Print the DataFrame and the new data types to verify the conversion
print("\nDataFrame after conversion:")
print(df)
print("\nNew data types:")
print(df.dtypes)
