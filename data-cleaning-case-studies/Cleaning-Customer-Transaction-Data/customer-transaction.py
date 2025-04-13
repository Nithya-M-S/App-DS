#2.  Cleaning Customer Transaction Data
'''Scenario:
A retail store has collected customer transaction data, but it contains errors such as missing values, incorrect formats, and duplicate entries. Your task is to clean the dataset using Pandas to prepare it for further analysis.'''

import pandas as pd
import numpy as np

df=pd.read_csv('customer_transaction_data.csv')
print(df)


# A. Handling Missing & Incorrect Data

# 1. Replace ? in Age and Gender with appropriate values (mean age, most common gender).
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print(df.info())
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
#age is in string
df['Age'] = df['Age'].replace('?', np.nan).astype(float)
print('Converted ? to nan value: \n',df['Age'])
print('---------------------------------------------------------------')
df['Age']=df['Age'].fillna(df['Age'].mean()).astype(int)
print('Filled nan with mean value and age to int: \n',df['Age'])

#gender
df['Gender'] = df['Gender'].replace('?', np.nan)
most_common_gender = df['Gender'].mode()[0]
df['Gender']=df['Gender'].fillna(most_common_gender)
print(df['Gender'])

# 2. Fill missing Purchase_Amount with the median purchase amount.
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Filled missing Purchase_Amount with the median purchase amount')
df['Purchase_Amount'] = df['Purchase_Amount'].fillna(df['Purchase_Amount'].median())
print(df['Purchase_Amount'])

# 3. Convert negative Purchase_Amount values to positive.
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Converted negative Purchase_Amount values to positive')
df['Purchase_Amount'] = df['Purchase_Amount'].abs()
print(df['Purchase_Amount'])

#4. Replace missing Payment_Method values with "Unknown".
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Replaced missing Payment_Method values with "Unknown"')
df['Payment_Method'] = df['Payment_Method'].replace('?', np.nan).fillna('Unknown')
print(df['Payment_Method'])

#B. Standardizing Formats

#5.Convert all Purchase_Date values into a proper date format (YYYY-MM-DD).
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Converted all Purchase_Date values into a proper date format (YYYY-MM-DD)')
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce',dayfirst=True)
print(df['Purchase_Date'])


#6.Convert Payment_Method values to lowercase for consistency (e.g., "Credit Card" → "credit card").
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Converted Payment_Method values to lowercase for consistency (e.g., "Credit Card" → "credit card")')
df['Payment_Method'] = df['Payment_Method'].str.lower()
print(df['Payment_Method'])

# C. Removing Duplicates & Final Adjustments

#7.Remove duplicate Transaction_ID entries.
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Removed duplicate Transaction_ID entries')
df = df.drop_duplicates(subset='Transaction_ID')
print(df['Transaction_ID'])

#8. Ensure Purchase_Amount is stored as a float with two decimal places.
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Ensured Purchase_Amount is stored as a float with two decimal places')
df['Purchase_Amount'] = df['Purchase_Amount'].astype(float).round(2)
print(df['Purchase_Amount'])

#9.	Save the cleaned dataset as cleaned_customer_transactions.csv.
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Saved the cleaned dataset as cleaned_customer_transactions.csv')
df.to_csv('cleaned_customer_transactions.csv', index=False)
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('Cleaned dataset saved successfully!')
