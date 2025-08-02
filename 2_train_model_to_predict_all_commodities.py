# predictions_all_commodities.py

"""
Predicting Food Commodity Prices in Rwanda
============================================
Using Prophet to predictions future prices for each commodity.
Input: processed_food_prices.csv
Output: Individual predictions CSVs per commodity in ./predictions/
"""

# -----------------------------------------
# STEP 1: Import Required Libraries
# -----------------------------------------
import pandas as pd
from prophet import Prophet
import os

# -----------------------------------------
# STEP 2: Load the Processed Dataset
# -----------------------------------------
data_path = "./data/processed/processed_food_prices.csv"
df = pd.read_csv(data_path)

# Ensure columns are correct
assert 'commodity' in df.columns and 'year_month' in df.columns and 'average_price' in df.columns

# -----------------------------------------
# STEP 3: Create Output Directory
# -----------------------------------------
predictions_dir = "./predictions"
os.makedirs(predictions_dir, exist_ok=True)

# -----------------------------------------
# STEP 4: Initialize Combined predictions List
# -----------------------------------------
unique_commodities = df['commodity'].unique()
combined_predictions = []

# -----------------------------------------
# STEP 5: Loop Over Each Commodity and predictions
# -----------------------------------------
for commodity in unique_commodities:
    print(f"predicting for: {commodity}")

    sub_df = df[df['commodity'] == commodity].copy()

    # Prepare for Prophet
    sub_df['ds'] = pd.to_datetime(sub_df['year_month'], format='%Y-%m')
    sub_df['y'] = sub_df['average_price']
    prophet_df = sub_df[['ds', 'y']]

    if prophet_df.shape[0] < 12:
        print(f"Not enough data for {commodity}. Skipping.")
        continue

    # Train model
    model = Prophet()
    model.fit(prophet_df)

    # Predict next 3 months
    future = model.make_future_dataframe(periods=3, freq='M')
    predictions = model.predict(future)

    predictions_output = predictions[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    predictions_output.columns = ['date', 'predicted_price', 'lower_bound', 'upper_bound']
    predictions_output['commodity'] = commodity

    combined_predictions.append(predictions_output)

# -----------------------------------------
# STEP 6: Concatenate All predictions into One File
# -----------------------------------------
final_predictions_df = pd.concat(combined_predictions, ignore_index=True)
final_predictions_df = final_predictions_df[['commodity', 'date', 'predicted_price', 'lower_bound', 'upper_bound']]

# Save to one CSV file
final_path = os.path.join(predictions_dir, "all_commodity_predictions_1.csv")
final_predictions_df.to_csv(final_path, index=False)

# -----------------------------------------
# STEP 7: Print Summary of Predictions
# -----------------------------------------
print("Summary of predictions:")
print("=" * 40)
print(final_predictions_df.head())

print(f"Total commodities predicted: {len(unique_commodities)}")
print(f"Total predictions records: {final_predictions_df.shape[0]}")
print(f"All predictions complete. Check the {final_path} directory.")

