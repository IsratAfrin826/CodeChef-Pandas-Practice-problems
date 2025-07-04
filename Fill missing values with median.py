import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 92, np.nan, 78, 95],
        'City': ['NY', 'LA', 'Chicago', 'NY', 'LA']}
df = pd.DataFrame(data)

# find median of 'Score' and replace all missing values with the median score
median_score = df['Score'].median()
df['Score'] = df['Score'].fillna(median_score)

print(df)
