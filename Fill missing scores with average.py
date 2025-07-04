import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, None, 22, 28],
        'Score': [85, 92, 78, None, 95]}

df = pd.DataFrame(data)

# Calculate the average score
average_score = df['Score'].mean()

# Fill missing values in the 'Score' column with the average score
df['Score'] = df['Score'].fillna(average_score)

print(df)
