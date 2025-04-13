#Employee Performance Data

'''Scenario:
A company has collected employee performance data but has noticed several data quality issues. Your task is to clean the dataset and prepare it for analysis using Pandas.'''

import pandas as pd
import numpy as np

df=pd.read_csv('employee_data_dirty.csv')
print(df)

# 1. Handling missing values

#a. identifying missing values
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('a. identifying missing values')

print(df.isnull().sum())

#b. Fill missing Performance_Rating with the department’s average rating (KK)
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('b.Fill missing Performance_Rating with the department’s average rating')
df['Performance_Rating'] = df.groupby('Department')['Performance_Rating'].transform(lambda x: x.fillna(x.mean()))
print(df['Performance_Rating'])

#c. Replace missing Salary with the department’s median salary
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('c. Replace missing Salary with the department’s median salary')
df['Salary'] = df.groupby('Department')['Salary'].transform(lambda x: x.fillna(x.median()))
print(df['Salary'])

#d. If an employee's Projects_Completed is missing, fill it with 0
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('d. If an employee\'s Projects_Completed is missing, fill it with 0')
df['Projects_Completed'] = df['Projects_Completed'].fillna(0)
print(df['Projects_Completed'])

# 2. Fixing Incorrect & Inconsistent Data

# a. Convert Working_Hours column values like ? to NaN and fill them with the mean working hours.
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('a. Convert Working_Hours column values like ? to NaN and fill them with the mean working hours')
df['Working_Hours'] = df['Working_Hours'].replace('?', np.nan).astype(float)
df['Working_Hours'] = df['Working_Hours'].fillna(df['Working_Hours'].mean())
print(df['Working_Hours'])

#b. Fix negative values in the Age column by taking absolute values.
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('b. Fix negative values in the Age column by taking absolute values')
df['Age'] = df['Age'].abs()
print(df['Age'])

#c. Standardize Department Names to lowercase (e.g., "HR" → "hr").
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('c. Standardize Department Names to lowercase (e.g., "HR" → "hr")')
df['Department'] = df['Department'].str.lower()
print(df['Department'])

# for particular deparment lower case(its mine question)

#d. Remove duplicate records (e.g., Alice appears twice).
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('d. Remove duplicate records (e.g., Alice appears twice)')
df1 = df.drop_duplicates('Name')
print(df1)

#3. formatting & Final Checks

#a. Convert Salary into integer values (if stored as float). 
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('a. Convert Salary into integer values (if stored as float)')
df['Salary'] = df['Salary'].astype(int)
print(df['Salary'])

#b. Save the cleaned dataset as cleaned_employee_data.csv.
print('--------------------------------------------------------------------')
print('--------------------------------------------------------------------')
print('b. Save the cleaned dataset as cleaned_employee_data.csv')
df.to_csv('cleaned_employee_data.csv', index=False) #always use index=False to avoid writing row numbers
print('cleaned_employee_data.csv created')
print('--------------------------------------------------------------------')