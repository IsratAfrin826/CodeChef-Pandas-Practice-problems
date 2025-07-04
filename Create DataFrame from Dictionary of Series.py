import pandas as pd

names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages = pd.Series([25, 30, 22, 35])

data = {
    'Name': names,
    'Age': ages

}

df = pd.DataFrame(data)

print(df)