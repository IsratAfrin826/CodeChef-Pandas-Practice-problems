import pandas as pd

# Create a DataFrame for customer information
customer_info = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
})

# Create a DataFrame for order data
order_data = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 1, 5, 3],
    'Amount': [50.00, 75.50, 100.00, 25.00, 120.00]
})

# Your task: Merge the two DataFrames based on the 'CustomerID' column.
# Store the result in a new DataFrame called 'combined_data'.
# Use the default merge type (inner join).

combined_data = pd.merge(customer_info, order_data,on='CustomerID')

# Display the resulting merged DataFrame
print(combined_data)
