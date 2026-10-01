from pathlib import Path

import pandas as pd
import plotly.express as px

folder = Path(__file__).resolve().parent
file_path = folder / "e commerce project.csv.xlsx"
output_file = folder / "orders_by_shipping_mode.html"

# The first row is a title; the second row contains the column headers.
df = pd.read_excel(
    file_path,
    sheet_name="cleaned data",
    header=1
)
df.columns = df.columns.str.strip()

# Count orders by shipping mode.
orders_by_shipping = (
    df.dropna(subset=["Shipping Mode"])
    .groupby("Shipping Mode")["Order id"]
    .nunique()
    .reset_index(name="Orders")
    .sort_values("Orders", ascending=False)
)

# Create an interactive pie chart.
fig = px.pie(
    orders_by_shipping,
    names="Shipping Mode",
    values="Orders",
    title="Orders by Shipping Mode",
)
fig.update_traces(textposition="inside", textinfo="label+percent+value")
fig.show()

# Save an interactive copy.
fig.write_html(output_file)
print(f"Interactive chart saved to: {output_file}")