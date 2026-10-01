from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

file_path = Path(__file__).resolve().parent / "e commerce project.csv.xlsx"

# The first row is a title; the second row contains the column headers.
df = pd.read_excel(
    file_path,
    sheet_name="cleaned data",
    header=1
)
df.columns = df.columns.str.strip()

df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Keep completed orders with valid category and sales values.
delivered = df[
    df["Order Status"].astype(str).str.strip().str.lower().eq("delivered")
].dropna(subset=["Category", "sales"])

# Add up sales within each category.
sales_by_category = delivered.groupby("Category")["sales"].sum().sort_values(
    ascending=False
)

# Display the pie chart.
plt.figure(figsize=(9, 9))
plt.pie(
    sales_by_category.values,
    labels=sales_by_category.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales by Category — Delivered Orders")
plt.axis("equal")
plt.tight_layout()
plt.show()