# SWYNEX-EXPLORATORY-DATA-ANALYSIS-PROJECT


## 📌 Project Overview

This project focuses on analyzing an e-commerce dataset to identify important business trends, customer behavior, sales performance, order patterns, payment preferences, shipping methods, and product performance.

The dataset was cleaned and analyzed using **Python, Pandas, Matplotlib and Plotly**.

The analysis includes multiple visualizations and business insights based on delivered orders.

---

## 🎯 Project Objectives

- Clean and prepare the e-commerce dataset
- Analyze order status
- Analyze payment methods
- Analyze sales by category
- Analyze sales by state
- Analyze shipping methods
- Analyze monthly sales trends
- Identify top customers by sales
- Identify top products by sales
- Generate useful business insights

---

## 🛠️ Tools & Technologies

- 🐍 Python
- 🐼 Pandas
- 📊 Matplotlib
- 📈 Plotly
- 📗 Excel
- 💻 VS Code
- 🐙 GitHub

---

# 📊 Data Analysis & Visualizations
This visualization shows the distribution of orders according to their status.
<img width="1857" height="812" alt="Image" src="https://github.com/user-attachments/assets/1583680b-95bd-4f61-a9cc-89d65f823398" />
### Key Observation
The dataset contains different order statuses such as:
- Delivered
- Pending
- Returned
- Cancelled
Delivered orders account for **271 orders (26.6%)**, while pending orders account for **262 orders (25.7%)**.

---

## 2️⃣ Orders by Payment Mode
<img width="1825" height="822" alt="Image" src="https://github.com/user-attachments/assets/3e11274d-eb5e-4734-9dc8-c35c9bc13e07" />
This chart shows the number of orders made using different payment methods.


### Key Observation

The dataset contains the following payment methods:

- Wallet
- COD
- Credit Card
- Debit Card
- UPI

Wallet has **218 orders (21.4%)**, while COD has **213 orders (20.9%)**.

---

## 3️⃣ Sales by Category

This visualization shows the distribution of sales across product categories for delivered orders.
<img width="1877" height="932" alt="Image" src="https://github.com/user-attachments/assets/7923ab0e-0b4e-40d5-8753-2fe301ae38f5" />

### Categories

- Electronics
- Beauty
- Fashion
- Sports
- Grocery
- Home

### Key Observation

Sales are distributed across all six categories, with Home and Grocery contributing significant portions of delivered-order sales.

---

## 4️⃣ Sales by State

The following map shows sales distribution across different states for delivered orders.
<img width="1857" height="867" alt="Image" src="https://github.com/user-attachments/assets/cd7b6fbc-8ae6-4939-8738-e3b3576e191e" />

### Key Observation

Sales vary significantly across states. The visualization helps identify geographical regions with higher delivered-order sales.

This type of analysis can help businesses understand regional demand and plan inventory and marketing activities.

---

## 5️⃣ Orders by Shipping Mode

This chart shows the distribution of orders according to shipping method.
<img width="1855" height="842" alt="Image" src="https://github.com/user-attachments/assets/52a6150d-7c54-4ddc-a911-1a7e9d7106ba" />

### Shipping Modes

- Express
- Standard
- Same Day

### Key Observation

The order distribution is relatively balanced:

- Express: **347 orders (34.1%)**
- Standard: **342 orders (33.6%)**
- Same Day: **329 orders (32.3%)**

---

## 6️⃣ Monthly Sales Trend

This chart shows the monthly sales trend for delivered orders.
<img width="1741" height="785" alt="Image" src="https://github.com/user-attachments/assets/bd80a363-a473-49e3-8839-783118341344" />


### Key Observation

Monthly sales fluctuate throughout the period.

The highest visible sales occur around **2025-04**, while some months show considerably lower sales.

This analysis helps identify periods of high and low sales activity.

---

## 7️⃣ Top 10 Customers by Sales

This visualization identifies the top 10 customers based on sales from delivered orders.
<img width="1837" height="855" alt="Image" src="https://github.com/user-attachments/assets/0f709837-eeee-45a9-89a7-1140ab7901fa" />

### Key Observation

The chart shows the contribution of the highest-value customers to delivered-order sales.

Customer-level analysis can help businesses understand valuable customers and develop customer retention strategies.

---

## 8️⃣ Top 10 Products by Sales

This chart shows the top 10 products based on sales from delivered orders.
<img width="1823" height="870" alt="Image" src="https://github.com/user-attachments/assets/db891323-03f6-4840-897c-a12eb2531d64" />

### Top Products

Some of the highest-selling products include:

- Biscuits
- Yoga Mat
- Face Wash
- Chair
- Polo
- Mixer
- Runner
- Inspiron
- Galaxy A55
- Kurtha

### Key Observation

**Biscuits** generated the highest sales among the displayed top 10 products, followed by **Yoga Mat** and **Face Wash**.

---

# 🔍 Business Insights

Based on the analysis, several useful observations can be identified:

### 1. Order Status

The dataset contains a substantial number of delivered, pending, returned, and cancelled orders. Monitoring these categories can help understand order fulfillment performance.

### 2. Payment Preferences

Wallet, COD, credit card, debit card, and UPI are all used by customers. The relatively balanced distribution indicates that customers use multiple payment methods.

### 3. Category Performance

Sales are spread across Electronics, Beauty, Fashion, Sports, Grocery, and Home categories.

### 4. Regional Sales

The state-level visualization shows that sales are geographically distributed, with some states contributing considerably more sales than others.

### 5. Shipping Preferences

Express, Standard, and Same Day shipping have relatively similar order volumes.

### 6. Monthly Sales

Sales fluctuate from month to month, showing different periods of high and low business activity.

### 7. Customer Analysis

A small group of customers contributes a significant amount of sales, making customer-level analysis useful for understanding high-value customers.

### 8. Product Performance

The top-product analysis helps identify products that generate higher sales and can support inventory and product planning.



# 💻 Python Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
```

---

# 📌 Conclusion

This E-Commerce Data Analysis project demonstrates how raw e-commerce data can be transformed into meaningful business insights using Python and data visualization.

The project covers:

- Data cleaning
- Exploratory Data Analysis
- Sales analysis
- Customer analysis
- Product analysis
- Payment analysis
- Shipping analysis
- Geographic analysis
- Monthly trend analysis

These insights can help businesses understand customer behavior, sales performance, product demand, and order patterns.

