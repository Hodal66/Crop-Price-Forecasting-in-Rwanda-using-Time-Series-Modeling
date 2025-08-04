---
##🌾 Crops Prices Prediction in Rwanda
---
## Introduction

This project predicts the prices of various food commodities in Rwanda using historical data. It involves data collection, cleaning, exploratory data analysis, modeling, and visualization of results. It also includes Power BI reports for policy-making and decision support.

---

A complete pipeline for **predicting food prices in Rwanda** using historical data from the [World Food Programme](https://data.humdata.org/dataset/wfp-food-prices-for-rwanda), with visual insights powered by **Power BI** and predicting models using **Facebook Prophet**.

## 📁 Project Structure
````markdown

```bash
PROJECT_ON_CROPS_PRICES_FORECAST_RWANDA/
│
├── data/
│   ├── processed/
│   │   ├── cleaned_food_prices.csv
│   │   └── processed_food_prices.csv
│   └── raw/
│       └── wfp_food_prices_rwa.csv
│
├── notebooks/
│   └── eda_visualization.ipynb
│
├── power_bi/
│   └── MuhetoHodal_Powerbi_Exam_Report.pbix
│
├── predictions/
│   ├── all_commodity_predictions.csv
│   ├── all_commodity_predictions_1.csv
│   └── all_commodity_predictions_2.csv
│
├── reports/
│   ├── output_images_visualization/
│   ├── power_bi_screen_shoots/
│   └── screen_shoots/
│
├── 1_clean_food_prices_data.py
├── 2_train_model_to_predict_all_commodities.py
├── .gitignore
└── README.md
````

---

## 📌 Objective

To build a machine learning pipeline that predicts the prices of food commodities in Rwanda and provides actionable insights for:

* Farmers (to determine best times to sell)
* Policymakers (for intervention and price control)
* Traders and Investors (to identify market trends)

---

## 🧾 Dataset Description

* **Source**: World Food Programme (WFP) Rwanda dataset
* **File**: `wfp_food_prices_rwa.csv`
* **Content**: Prices of various food items by market, date, and unit

---

## 🧹 Data Processing Steps

| Step               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| 🔸 Raw Data Import | Loaded from `data/raw/wfp_food_prices_rwa.csv`         |
| 🔸 Cleaning        | Performed in `1_clean_food_prices_data.py`             |
| 🔸 Output Files    | `cleaned_food_prices.csv`, `processed_food_prices.csv` |

Processed datasets are stored in `data/processed/`.

---

## 📊 Exploratory Data Analysis (EDA)

Notebook: `eda_visualization.ipynb`

Key insights explored:

* Price variation over time
* Market-specific trends
* Outlier detection
* Seasonal patterns

Visual outputs available in:
`reports/output_images_visualization/`

---

## 🤖 Modeling

Script: `2_train_model_to_predict_all_commodities.py`

* Algorithms used: Linear Regression, Random Forest, etc.
* Target: Predict prices of multiple food commodities
* Input: Processed features (time, market, product, etc.)
* Output: Prediction results saved in CSV format

Prediction outputs:

* `all_commodity_predictions.csv`
* `all_commodity_predictions_1.csv`
* `all_commodity_predictions_2.csv`

---

## 📈 Power BI Dashboard

Power BI file: `MuhetoHodal_Powerbi_Exam_Report.pbix`
Screenshots available in:

* `reports/power_bi_screen_shoots/`
* `reports/screen_shoots/`

Key features:

* Interactive filters by market and product
* Monthly trend lines
* Price comparison per province

---

## 📋 Reporting

Structured reports and images provided in:

* `reports/output_images_visualization/`
* `reports/screen_shoots/`

Visualizations include:

* Price fluctuation trends
* Prediction vs actual price comparison
* Commodity-wise forecasting

---

## 🛠️ Technologies Used

* **Languages**: Python, DAX (Power BI)
* **Libraries**: Pandas, Matplotlib, Scikit-learn, Seaborn
* **BI Tool**: Power BI
* **Environment**: Jupyter Notebooks, Visual Studio Code

---

## 🧠 Key Insights & Recommendations

* 🔍 **Seasonality Detected**: Prices peak in certain months—important for storage and logistics.
* 📉 **Unstable Pricing**: Some markets show volatile patterns—monitoring recommended.
* 📊 **Prediction Models Useful**: Accuracy sufficient for short-term pricing strategies.

---

## ✅ Future Enhancements

* Include real-time API feeds for pricing
* Introduce weather and inflation variables
* Develop a dashboard web app with live data updates

---

## 🙌 Author

**Muheto Hodal**
Power BI | Big Data Analytics | Python Developer

📫 Email: \[[mhthodol@gmail.com](mailto:mhthodol@gmail.com)]

🔗 LinkedIn: [Get_Connected_Here](https://www.linkedin.com/in/muheto-hodal-006568130/)

📋 Power Point: \[[PowerPoint](https://food-price-prediction-an-eu1ph98.gamma.site/)]

📈 Dataset: \[[Download_Here](https://data.humdata.org/dataset/wfp-food-prices-for-rwanda)]

---

## ☄ Screenshoots

**Cleaning, Visualisation $ Training Process**

![cleaning_data_2](https://github.com/user-attachments/assets/9ef3b29a-a1cb-4f18-982b-7f3c442e97e8)
![cleaning_data_1](https://github.com/user-attachments/assets/fad47e99-c173-4f64-acc6-283e9dc8913f)
![training_model_1](https://github.com/user-attachments/assets/00483785-5b98-407e-91e6-3310436b251f)
![data_visualizations_1](https://github.com/user-attachments/assets/2349b1a1-06c4-4945-bfa6-c0388a0902ea)
![data_importing_1](https://github.com/user-attachments/assets/4355f7a9-f41a-4b4b-b767-5462e6e8af67)
<img width="3000" height="1800" alt="price_distribution_by_province" src="https://github.com/user-attachments/assets/f242cb29-3f04-4541-b2e1-e2e8c47fb68c" />
<img width="3000" height="1500" alt="most_reported_commodities" src="https://github.com/user-attachments/assets/0ec5f20f-3157-450c-93c4-0b443a36b707" />
<img width="4200" height="3000" alt="monthly_price_heatmap_top_commodities" src="https://github.com/user-attachments/assets/8b3518b5-c56e-406f-a3e2-a68b809ae3b3" />
<img width="3600" height="1800" alt="maize_price_trend_over_time" src="https://github.com/user-attachments/assets/5b09c40c-b511-4760-9b32-499925932c20" />
<img width="3000" height="1800" alt="top_avg_price" src="https://github.com/user-attachments/assets/33cf1e4c-9880-4751-bf2e-0d04296af6dc" />
<img width="3000" height="1500" alt="top_10_commodities" src="https://github.com/user-attachments/assets/a927e10f-c235-4d4c-a505-ae689996129d" />
<img width="2400" height="1200" alt="records_per_province" src="https://github.com/user-attachments/assets/12d321e6-3e00-4a70-ae85-461084d276e8" />
<img width="3000" height="1800" alt="avg_price_barh_avg_price_rwf" src="https://github.com/user-attachments/assets/eae7c7f9-d107-48e6-b01e-c4d0070e7e5c" />
<img width="3600" height="1800" alt="beans_price_trend" src="https://github.com/user-attachments/assets/2d728793-5e48-493b-acc5-901a44b4df56" />

**Powerbi Dasbord**

![Dashboard_for_DataVisualisation](https://github.com/user-attachments/assets/b664b2a4-4f89-4b9d-b5d0-63e15218952b)
![All_Tables](https://github.com/user-attachments/assets/07f511a9-a2c6-4bf2-91a8-6a893b91f55b)
![Last_Prediction_Table_Contents](https://github.com/user-attachments/assets/74cc2f3c-a913-4312-92bc-ed522c029961)
![Dashboard_for_Predictions_Model_2](https://github.com/user-attachments/assets/8cd834e6-2d54-44b4-8a5b-2658b42ca06f)
![Dashboard_for_Predictions_Model_1](https://github.com/user-attachments/assets/927f25ee-7e6d-4be3-9a25-0abd924924e1)


```
