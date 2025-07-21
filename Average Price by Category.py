import pandas as pd
import io

data = """Category,Price
Electronics,500
Clothing,50
Electronics,750
Books,20
Clothing,75
Books,30
Electronics,600
Clothing,60
Books,25
"""

products_df = pd.read_csv(io.StringIO(data))

average_price_by_category = products_df.groupby('Category')['Price'].mean()

print(average_price_by_category)
