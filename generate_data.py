import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n = 1200

categories = {
    "Technology": {"sub": ["Phones", "Laptops", "Accessories", "Monitors"], "base_price": (200, 2500), "margin": (0.10, 0.30)},
    "Furniture":  {"sub": ["Chairs", "Tables", "Bookcases", "Storage"],    "base_price": (100, 1800), "margin": (-0.05, 0.20)},
    "Office Supplies": {"sub": ["Binders", "Paper", "Pens", "Labels"],     "base_price": (5, 150),   "margin": (0.20, 0.45)},
}

regions = {
    "West":    ["Los Angeles", "San Francisco", "Seattle", "Portland"],
    "East":    ["New York", "Philadelphia", "Boston", "Atlanta"],
    "Central": ["Chicago", "Dallas", "Houston", "Denver"],
    "South":   ["Miami", "Nashville", "New Orleans", "Charlotte"],
}

segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]

start_date = datetime(2021, 1, 1)
end_date   = datetime(2023, 12, 31)

rows = []
order_id_counter = 1000

for _ in range(n):
    cat_name  = random.choices(list(categories.keys()), weights=[3, 2.5, 4.5])[0]
    cat_info  = categories[cat_name]
    sub_cat   = random.choice(cat_info["sub"])
    region    = random.choices(list(regions.keys()), weights=[3, 3.5, 2, 1.5])[0]
    city      = random.choice(regions[region])
    segment   = random.choices(segments, weights=[5, 3, 2])[0]
    ship_mode = random.choices(ship_modes, weights=[5, 2.5, 2, 0.5])[0]

    order_date  = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    ship_date   = order_date + timedelta(days=random.choice([1,2,3,4,5,7]))

    sales = round(random.uniform(*cat_info["base_price"]) * random.randint(1, 4), 2)
    discount = random.choices([0.0, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50],
                               weights=[50, 15, 10, 10, 7, 5, 3])[0]
    sales_after_discount = round(sales * (1 - discount), 2)
    margin_pct = random.uniform(*cat_info["margin"]) - discount * 0.5
    profit = round(sales_after_discount * margin_pct, 2)
    quantity = random.randint(1, 6)

    rows.append({
        "Order ID":        f"ORD-{order_id_counter:05d}",
        "Order Date":      order_date.strftime("%Y-%m-%d"),
        "Ship Date":       ship_date.strftime("%Y-%m-%d"),
        "Ship Mode":       ship_mode,
        "Customer ID":     f"CUST-{random.randint(1000, 1300):04d}",
        "Segment":         segment,
        "City":            city,
        "Region":          region,
        "Category":        cat_name,
        "Sub-Category":    sub_cat,
        "Sales":           sales_after_discount,
        "Quantity":        quantity,
        "Discount":        discount,
        "Profit":          profit,
    })
    order_id_counter += 1

df = pd.DataFrame(rows)
df.to_csv("data/superstore_sales.csv", index=False)
print(f"Generated {len(df)} rows")
print(df.head())
