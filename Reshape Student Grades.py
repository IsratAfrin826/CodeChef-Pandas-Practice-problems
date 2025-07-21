import pandas as pd

# Create a sample DataFrame (replace with your actual data loading if needed)
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 85],
    'History': [78, 85, 80]
}
df = pd.DataFrame(data)

# Reshape the DataFrame
reshaped_df = df.melt(id_vars=['Student'], var_name='Subject', value_name='Grade')

# Print the reshaped DataFrame
print(reshaped_df)