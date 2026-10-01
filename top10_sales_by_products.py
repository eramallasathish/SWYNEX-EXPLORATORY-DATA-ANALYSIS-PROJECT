from pathlib import Path

import pandas as pd
import plotly.express as px

folder = Path(__file__).resolve().parent
file_path = folder / "e commerce project.csv.xlsx"
output_file = folder / "top_10_products_by_sales.html"

# The first row is a title; the second row contains the column headers.
df = pd.read_excel(
    file_path,
    sheet_name="cleaned data",
    header=1
)
df.columns = df.columns.str.strip()

df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Keep delivered orders that have product names and sales values.
delivered = df[
    df["Order Status"].astype(str).str.strip().str.lower().eq("delivered")
].dropna(subset=["Product Name", "sales"])

# Sum sales for each product and select the top 10.
top_products = (
    delivered.groupby("Product Name", as_index=False)["sales"]
    .sum()
    .nlargest(10, "sales")
    .sort_values("sales", ascending=True)
)

# Create an interactive horizontal bar graph.
fig = px.bar(
    top_products,
    x="sales",
    y="Product Name",
    orientation="h",
    text="sales",
    title="Top 10 Products by Sales — Delivered Orders",
    labels={"sales": "Sales", "Product Name": "Product"},
)

fig.update_traces(texttemplate="%{text:,.2f}", textposition="outside")
fig.update_layout(yaxis={"categoryorder": "total ascending"})
fig.show()

# Save an interactive copy.
fig.write_html(output_file)
print(f"Interactive graph saved to: {output_file}")