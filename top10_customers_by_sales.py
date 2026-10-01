from pathlib import Path

import pandas as pd
import plotly.express as px

folder = Path(__file__).resolve().parent
file_path = folder / "e commerce project.csv.xlsx"
output_file = folder / "top_10_customers_by_sales.html"

# The first row is a title; the second row contains the column headers.
df = pd.read_excel(
    file_path,
    sheet_name="cleaned data",
    header=1
)
df.columns = df.columns.str.strip()

df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Keep delivered orders with valid customer and sales values.
delivered = df[
    df["Order Status"].astype(str).str.strip().str.lower().eq("delivered")
].dropna(subset=["Customer ID", "Customer Name", "sales"])

# Sum sales by customer ID and name, then select the top 10.
top_customers = (
    delivered.groupby(["Customer ID", "Customer Name"], as_index=False)["sales"]
    .sum()
    .nlargest(10, "sales")
)

# Include the ID in each label so customers with the same name are distinct.
top_customers["Customer"] = (
    top_customers["Customer Name"] + " (" + top_customers["Customer ID"] + ")"
)

# Create an interactive pie chart.
fig = px.pie(
    top_customers,
    names="Customer",
    values="sales",
    title="Top 10 Customers by Sales — Delivered Orders",
    hover_data={"sales": ":,.2f"},
)
fig.update_traces(textposition="inside", textinfo="label+percent")
fig.show()

# Save an interactive copy.
fig.write_html(output_file)
print(f"Interactive chart saved to: {output_file}")