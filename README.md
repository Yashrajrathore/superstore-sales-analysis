# 🛒 Superstore Sales — End-to-End EDA & Business Intelligence

**Tools:** Python · Pandas · Matplotlib · Seaborn  
**Dataset:** 1,200 orders · 3 years (2021–2023) · 4 regions · 3 categories  

---

## 📌 Objective

Perform a full exploratory data analysis on a retail superstore dataset to uncover
revenue drivers, profitability leaks, discount risks, and regional opportunities —
and translate raw numbers into actionable business recommendations.

---

## 📊 Key Findings

| Insight | Detail |
|---|---|
| **Top Revenue Driver** | Technology (₹10.5L, 15.9% margin) |
| **Highest Margin Category** | Office Supplies (28.4% margin) |
| **Best Region** | East leads revenue; Central leads margin (13.4%) |
| **Discount Risk** | ≥40% discount → 49% of orders are loss-making |
| **Pareto Rule** | Top 10 of 16 cities = 80% of total revenue |
| **Seasonality** | Q4 peaks consistently across all 3 years |

---

## 📁 Project Structure

```
superstore-sales-analysis/
│
├── data/
│   └── superstore_sales.csv       # 1,200-row sales dataset
│
├── outputs/                       # Generated charts
│   ├── 01_category_analysis.png
│   ├── 02_subcategory_profit.png
│   ├── 03_regional_performance.png
│   ├── 04_monthly_trend.png
│   ├── 05_discount_analysis.png
│   ├── 06_segment_analysis.png
│   └── 07_pareto_cities.png
│
├── analysis.py                    # Main EDA script
├── generate_data.py               # Dataset generation script
├── requirements.txt
└── README.md
```

---

## 🔍 Analysis Modules

### 1. Data Cleaning & Engineering
- Validated 1,200 rows for nulls, duplicates, and type consistency
- Engineered: `Ship Days`, `Profit Margin`, `Loss Flag`, `YearMonth`

### 2. Category & Sub-Category Analysis
- Revenue, profit, and margin breakdown across 3 categories and 12 sub-categories
- Identified top 5 and bottom 5 sub-categories by profitability

### 3. Regional Performance
- Side-by-side revenue vs profit comparison across 4 regions
- Central region: lowest revenue but best margin — signals operational efficiency

### 4. Monthly & Seasonal Trends
- 36-month revenue trend with YoY comparison
- Confirmed Q4 seasonality — supports inventory and campaign planning

### 5. Discount Impact Analysis
- Scatter + bar chart showing profit degradation by discount level
- Critical finding: discounts ≥40% produce losses nearly half the time
- Recommendation: Cap discounts at 20%; use targeted promos instead of blanket cuts

### 6. Customer Segment Breakdown
- Consumer (52%), Corporate (31%), Home Office (18%) revenue split
- Home Office has the best margin despite lowest order volume

### 7. Pareto (80/20) Analysis
- Top 10 cities drive 80% of revenue
- Business recommendation: prioritise loyalty and retention in these cities

---

## 💡 Business Recommendations

1. **Reduce high discounts** — Orders with ≥40% discount are loss-making 49% of the time.
   Cap discounts at 20% to protect margins.
2. **Double down on Office Supplies** — Highest margin category (28.4%) but lowest revenue.
   Growth opportunity with targeted B2B marketing.
3. **Invest in East region** — Highest absolute revenue; upsell Technology products.
4. **Leverage Q4 seasonality** — Stock up and run campaigns in Sept–Oct to capture peak demand.
5. **Protect top-10 city customers** — 80% of revenue from 63% of cities; churn risk is high.

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yashrajrathore/superstore-sales-analysis
cd superstore-sales-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python generate_data.py

# 4. Run full analysis (outputs saved to /outputs)
python analysis.py
```

---

## 📦 Requirements

```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
```

---

## 👤 Author

**Yash Raj Rathore**  
[LinkedIn](https://www.linkedin.com/in/yashraj-rathore20) · [GitHub](https://github.com/yashrajrathore)
