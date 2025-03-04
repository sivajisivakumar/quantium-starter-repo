import pandas as pd

# Example data with regions
data = {
    'date': ['2020-12-01', '2020-12-02', '2020-12-03', '2021-01-14', '2021-01-15', '2021-01-16'],
    'sales_value': [200, 210, 230, 250, 300, 320],
    'region': ['north', 'east', 'south', 'west', 'north', 'east']  # Example regions
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
