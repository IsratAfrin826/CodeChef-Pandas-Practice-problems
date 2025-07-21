import pandas as pd

data = {'Department': ['Sales', 'Marketing', 'Sales', 'IT', 'Marketing', 'IT', 'Sales'],
        'Salary': [50000, 60000, 55000, 70000, 62000, 75000, 53000]}

df = pd.DataFrame(data)

# Calculate the average salary for each department

average_salary_by_department =  df.groupby('Department')['Salary'].mean()

print(average_salary_by_department)
