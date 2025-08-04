

````markdown
# 🌾 Crops Prices Prediction in Rwanda

This project predicts the prices of various food commodities in Rwanda using historical data. It involves data collection, cleaning, exploratory data analysis, modeling, and visualization of results. It also includes Power BI reports for policy-making and decision support.

---

A complete pipeline for **predicting food prices in Rwanda** using historical data from the [World Food Programme](https://data.humdata.org/dataset/wfp-food-prices-for-rwanda), with visual insights powered by **Power BI** and predicting models using **Facebook Prophet**.


## 📁 Project Structure

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

🔗 LinkedIn: [https://www.linkedin.com/in/muheto-hodal-006568130/](https://www.linkedin.com/in/muheto-hodal-006568130/)

Power Point: \[[PowerPoint](https://gamma.app/docs/Food-Price-Prediction-and-Visualization-Using-Python-Power-BI-18rdur5xclu7q4k)]

---

```
