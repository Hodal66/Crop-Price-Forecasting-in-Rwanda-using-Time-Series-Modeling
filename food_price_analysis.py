# food_price_analysis.py

"""
Food Price Forecasting in Rwanda
================================
This script performs data cleaning, preprocessing, and analysis on historical
food price data in Rwanda, with the goal of preparing it for Power BI visualization
and machine learning forecasting.

Dataset Source:
https://data.humdata.org/dataset/wfp-food-prices-for-rwanda

Author: [Your Name]
"""

# -------------------- 1. IMPORT LIBRARIES --------------------
import pandas as pd
import numpy as np

# -------------------- 2. LOAD DATA --------------------
df = pd.read_csv("./data/raw/wfp_food_prices_rwa.csv", low_memory=False)

# -------------------- 3. PREVIEW DATA --------------------
print("Initial dataset shape:", df.shape)
df = df[df['date'] != '#date']  # Remove header-like row

# -------------------- 4. HANDLE DATATYPES --------------------
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# -------------------- 5. DROP UNNECESSARY COLUMNS --------------------
columns_to_keep = ['date', 'admin1', 'admin2', 'market', 'commodity', 'unit', 'price']
df = df[columns_to_keep]

# -------------------- 6. HANDLE MISSING VALUES --------------------
df = df.dropna(subset=['price', 'date'])
df = df[df['price'] > 0]

# Fill other missing columns (if needed)
df['admin1'] = df['admin1'].fillna('Unknown')
df['admin2'] = df['admin2'].fillna('Unknown')
df['market'] = df['market'].fillna('Unknown')
df['commodity'] = df['commodity'].fillna('Unknown')

print("Cleaned dataset shape:", df.shape)

# -------------------- 7. AGGREGATE BY MONTH --------------------
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# Group by commodity and month
grouped_df = df.groupby(['commodity', 'year_month'])['price'].mean().reset_index()
grouped_df.rename(columns={'price': 'average_price'}, inplace=True)

print("Grouped Data Sample:")
print(grouped_df.head())

# -------------------- 8. EXPORT FOR POWER BI --------------------
grouped_df.to_csv("./data/processed/processed_food_prices.csv", index=False)
print("✅ Clean dataset exported as 'processed_food_prices.csv' for Power BI.")

# -------------------- 9. READY FOR MODELING --------------------
# This structured output can now be used for training forecasting models
# like Linear Regression, ARIMA, Prophet, etc. (to be handled next).
