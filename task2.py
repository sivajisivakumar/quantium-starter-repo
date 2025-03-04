import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_0.csv')
df3 = pd.read_csv('data/daily_sales_data_0.csv')


df1 = df1[df1['product'] == 'Pink Morsels']
df2 = df2[df2['product'] == 'Pink Morsels']
df3 = df3[df3['product'] == 'Pink Morsels']

df1['sales'] = df1['quantity'] * df1['price']
df2['sales'] = df2['quantity'] * df2['price']
df3['sales'] = df3['quantity'] * df3['price']

df1 = df1[['sales', 'date', 'region']]
df2 = df2[['sales', 'date', 'region']]
df3 = df3[['sales', 'date', 'region']]

combined_df = pd.concat([df1, df2, df3], ignore_index=True)

combined_df.to_csv('data/formatted_sales_data.csv', index=False)