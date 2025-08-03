
# 🇷🇼 Food Price predicting in Rwanda

A complete pipeline for **predicting food prices in Rwanda** using historical data from the [World Food Programme](https://data.humdata.org/dataset/wfp-food-prices-for-rwanda), with visual insights powered by **Power BI** and predicting models using **Facebook Prophet**.

---

## 📁 Project Structure

```

.
├── data/
│   ├── processed/
│   │   ├── cleaned\_food\_prices.csv
│   │   └── processed\_food\_prices.csv
│   ├── raw/
│   │   └── wfp\_food\_prices\_rwa.csv
├── notebooks/
│   └── eda\_visualization.ipynb
├── power\_bi/
│   └── MuhetoHodal\_Powerbi\_Exam\_Report.pbix
├── predictions/
│   ├── all\_commodity\_predictions.csv
│   ├── all\_commodity\_predictions\_1.csv
│   └── all\_commodity\_predictions\_2.csv
├── report/
├── screen\_shoots/
│   └── cleaning\_data\_1.JPG
├── .gitignore
├── requirements.txt
├── 1\_clean\_food\_prices\_data.py
├── 2\_train\_model\_to\_predict\_all\_commodities.py
└── README.md

````

---

## 🎯 Objective

To **analyze**, **clean**, and **forecast** food prices in Rwanda by commodity and location, and export results for dynamic visualization in **Power BI**.

---

## 📌 Key Features

- ✅ Cleaning & preprocessing historical data
- 📊 Exploratory Data Analysis using Jupyter
- 🤖 predicting with Prophet
- 📈 Exported forecasted datasets for Power BI dashboard
- 📎 Power BI Report file included
- 🗂️ Organized by modular scripts and folders

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/food-price-rwanda.git
cd food-price-rwanda
````

2. **Create Virtual Environment & Install Requirements**

```bash
python -m venv venv
source venv/bin/activate      # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

3. **Run Cleaning Script**

```bash
python 1_clean_food_prices_data.py
```

4. **Train the Model on All Commodities**

```bash
python 2_train_model_to_predict_all_commodities.py
```

---

## 🧼 Data Cleaning Pipeline

📄 **File**: `1_clean_food_prices_data.py`

### 🔍 Steps:

```py
# 🟢 STEP 1: Load raw dataset from WFP
# 🟢 STEP 2: Remove invalid rows and clean column formats
# 🟢 STEP 3: Handle missing values (admin1, admin2, etc.)
# 🟢 STEP 4: Filter invalid prices and convert datatypes
# 🟢 STEP 5: Aggregate prices by month and commodity
# 🟢 STEP 6: Export cleaned dataset
```

---

## 📈 predicting (Prophet)

📄 **File**: `2_train_model_to_predict_all_commodities.py`

### 🔮 Key Features:

* Forecasts prices for **each commodity individually**
* Trains Prophet model per group and concatenates results
* Saves output to `predictions/all_commodity_predictions.csv`

---

## 📊 Power BI Dashboard

📁 **Power BI File**: `MuhetoHodal_Powerbi_Exam_Report.pbix`

Features:

* Filter dropdowns for **commodity**, **date**, **market**
* Forecast visualization per commodity
* Interactive price trends over time

✅ Make sure to import:
`predictions/all_commodity_predictions.csv` and
`data/processed/processed_food_prices.csv`

🛠️ If dropdown shows only 2 commodities:

* Ensure table has **no filters applied**
* Confirm dataset is **fully refreshed** under *Transform Data*

---

## 📸 Screenshots

| Cleaning Stage                                   | predicting Output                       |
| ------------------------------------------------ | ---------------------------------------- |
| ![cleaning](./screen_shoots/cleaning_data_1.JPG) | *(Add a forecast screenshot if desired)* |

---

## 🔮 Sample Forecast Output

```csv
commodity,ds,yhat,yhat_lower,yhat_upper
Beans (dry),2024-01-01,385.12,350.90,410.67
Beans (dry),2024-02-01,392.41,358.70,420.23
Maize,2024-01-01,265.35,240.21,292.77
...
```

---

## 🧠 Modeling Strategy

* Model Used: **Facebook Prophet** (preferred for time series with trends & seasonality)
* Trained per-commodity using a modular pipeline
* Granularity: **monthly average prices**

---

## ✅ Achievements & Commits

* ✔️ Data cleaned and prepared for predicting
* ✔️ Prophet model trained on all commodities
* ✔️ Forecasts exported for Power BI
* ✔️ Power BI report built with filters and trends
* ✔️ All deliverables structured, reproducible, and automated

---

## 📦 Requirements

```txt
pandas
numpy
matplotlib
prophet
jupyter
```

(See `requirements.txt` for full list)

---

## 👤 Author

**Muheto Hodal**
📧 [hodalmuheto@gmail.com](mailto:hodalmuheto@gmail.com)
📍 Rwanda
💼 \[LinkedIn: ](https://www.linkedin.com/in/muheto-hodal-23311a211/)

---

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

---

```

