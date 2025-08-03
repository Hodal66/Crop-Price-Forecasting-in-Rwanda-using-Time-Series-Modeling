# food_price_analysis.py

"""
Food Price Forecasting in Rwanda
================================
This script performs robust data cleaning, preprocessing, and analysis on historical
food price data in Rwanda, preparing it for Power BI and machine learning modeling.

Dataset Source:
https://data.humdata.org/dataset/wfp-food-prices-for-rwanda

Author: MUHETO Hodal
"""

# -----------------------------------------
# STEP 1: Import Required Libraries
# -----------------------------------------
import pandas as pd
import numpy as np
import os

# -----------------------------------------
# STEP 2: Load Dataset
# -----------------------------------------
data_path = "./data/raw/wfp_food_prices_rwa.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"File not found at {data_path}")

df = pd.read_csv(data_path, low_memory=False)
print("Initial dataset shape:", df.shape)

# -----------------------------------------
# STEP 3: Remove Invalid Header Rows
# -----------------------------------------
# Sometimes datasets include multiple headers or placeholder rows
df = df[df['date'] != '#date']  # Remove bad header rows

# -----------------------------------------
# STEP 4: Convert Data Types
# -----------------------------------------
# Convert 'date' to datetime and 'price' to numeric (ignore errors)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# -----------------------------------------
# STEP 5: Drop Useless or Redundant Columns
# -----------------------------------------
# Keep only relevant columns for analysis
columns_to_keep = ['date', 'admin1', 'admin2', 'market', 'commodity', 'unit', 'price']
df = df[columns_to_keep]
print("After dropping unnecessary columns:", df.shape)

# -----------------------------------------
# STEP 6: Handle Missing & Invalid Data
# -----------------------------------------
# Drop rows where essential values are missing
df = df.dropna(subset=['date', 'price'])

# Filter out price values that are negative or zero
df = df[df['price'] > 0]

# Fill missing categorical values with 'Unknown'
for col in ['admin1', 'admin2', 'market', 'commodity']:
    df[col] = df[col].fillna('Unknown')

# -----------------------------------------
# STEP 7: Create Year-Month Column
# -----------------------------------------
# Useful for grouping and time series modeling
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# -----------------------------------------
# STEP 8: Group & Aggregate
# -----------------------------------------
# Group by commodity and month to get average price
grouped_df = df.groupby(['commodity', 'year_month'])['price'].mean().reset_index()
grouped_df.rename(columns={'price': 'average_price'}, inplace=True)

print("Grouped data preview:")
print(grouped_df.head())

# -----------------------------------------
# STEP 9: Final Check
# -----------------------------------------
print("Final cleaned dataset shape:", df.shape)
print("Aggregated dataset shape (for Power BI or ML):", grouped_df.shape)
print("Date range:", df['date'].min(), "to", df['date'].max())
print("Number of unique commodities:", df['commodity'].nunique())
print("Number of provinces (admin1):", df['admin1'].nunique())

# -----------------------------------------
# STEP 10: Export Cleaned Data
# -----------------------------------------
output_dir = "./data/processed"  # Learning new way to create directory path
os.makedirs(output_dir, exist_ok=True)

df.to_csv(os.path.join(output_dir, "cleaned_food_prices.csv"), index=False)
grouped_df.to_csv(os.path.join(output_dir, "processed_food_prices.csv"), index=False)

print("Cleaned dataset exported as 'cleaned_food_prices.csv'")
print("Aggregated dataset exported as 'processed_food_prices.csv'")

# -----------------------------------------
# STEP 11: Ready for Modeling
# -----------------------------------------
# This structured data is now ready for:
# - Power BI visualization
# - Forecasting with Prophet, ARIMA, or Linear Regression
# - Time series trend analysis

