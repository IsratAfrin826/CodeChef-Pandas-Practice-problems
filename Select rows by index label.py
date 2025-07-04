
data = {'Color': ['Red', 'Yellow', 'Green'],
        'Sweetness': ['High', 'Medium', 'Low']}
fruits_df = pd.DataFrame(data, index=['Apple', 'Banana', 'Grape'])

banana_row = fruits_df.loc['Banana']

print(banana_row)
