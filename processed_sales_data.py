import pandas as pd
import glob

# Step 1: Load all CSV files from the 'data' folder
files = glob.glob('data/*.csv')

# Initialize an empty DataFrame to hold combined data
all_data = pd.DataFrame()

# Step 2: Process each CSV file
for file in files:
    # Read the current CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Step 3: Filter for only 'Pink Morsels'
    df = df[df['product'] == 'Pink Morsels']
    
    # Step 4: Create a 'sales' column by multiplying 'quantity' and 'price'
    df['sales'] = df['quantity'] * df['price']
    
    # Step 5: Keep only 'sales', 'date', and 'region' columns
    df = df[['sales', 'date', 'region']]
    
    # Append the processed data to the all_data DataFrame
    all_data = pd.concat([all_data, df], ignore_index=True)

# Step 6: Save the processed data to a new CSV file
all_data.to_csv('daily_sales_data_0.csv', index=False)

print("Data processing complete. Saved to 'processed_sales_data.csv'.")
