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

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Keep completed orders and rows with valid dates and sales.
delivered = df[
    df["Order Status"].astype(str).str.strip().str.lower().eq("delivered")
].dropna(subset=["Order Date", "sales"])

# Sum sales for each month, in date order.
monthly_sales = (
    delivered.groupby(delivered["Order Date"].dt.to_period("M"))["sales"]
    .sum()
    .sort_index()
)

# Display the bar graph.
plt.figure(figsize=(14, 6))
plt.bar(monthly_sales.index.astype(str), monthly_sales.values, color="steelblue")
plt.title("Monthly Sales Trend — Delivered Orders")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=60, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()