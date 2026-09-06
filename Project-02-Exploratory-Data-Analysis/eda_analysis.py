"""
DecodeLabs Data Analytics Internship
Project 2: Exploratory Data Analysis (EDA)
Batch 2026
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 11

OUTPUT_DIR = Path("eda_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel("cleaned_dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

print("=" * 70)
print("PROJECT 2: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 70)

print("\n1. DATASET OVERVIEW")
print(f"Total Orders        : {len(df):,}")
print(f"Date Range          : {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Unique Customers    : {df['CustomerID'].nunique():,}")
print(f"Unique Products     : {df['Product'].nunique()}")
print(f"Total Revenue       : ${df['TotalPrice'].sum():,.2f}")

print("\n2. DESCRIPTIVE STATISTICS")
desc = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe().round(2)
print(desc)
desc.to_excel(OUTPUT_DIR / "descriptive_statistics.xlsx")

print("\n3. CATEGORICAL DISTRIBUTIONS")
for col in ["Product", "OrderStatus", "PaymentMethod", "ReferralSource", "CouponCode"]:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\n4. REVENUE BY PRODUCT")
rev_prod = (
    df.groupby("Product")["TotalPrice"]
    .agg(Total_Revenue="sum", Avg_Order_Value="mean", Order_Count="count")
    .round(2)
    .sort_values("Total_Revenue", ascending=False)
)
print(rev_prod)
rev_prod.to_excel(OUTPUT_DIR / "revenue_by_product.xlsx")

print("\n5. REVENUE BY ORDER STATUS")
rev_status = (
    df.groupby("OrderStatus")["TotalPrice"]
    .agg(Total_Revenue="sum", Avg_Order_Value="mean", Order_Count="count")
    .round(2)
    .sort_values("Total_Revenue", ascending=False)
)
print(rev_status)

print("\n6. OUTLIER DETECTION (IQR Method on TotalPrice)")
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["TotalPrice"] < lower) | (df["TotalPrice"] > upper)]
print(f"Q1 = {Q1:.2f} | Q3 = {Q3:.2f} | IQR = {IQR:.2f}")
print(f"Lower bound = {lower:.2f} | Upper bound = {upper:.2f}")
print(f"Outliers found: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")
outliers[["OrderID", "Product", "Quantity", "UnitPrice", "TotalPrice", "OrderStatus"]].to_excel(
    OUTPUT_DIR / "outliers_totalprice.xlsx", index=False
)

print("\n7. CORRELATION MATRIX")
corr = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr().round(3)
print(corr)
corr.to_excel(OUTPUT_DIR / "correlation_matrix.xlsx")

print("\n8. KEY BUSINESS METRICS")
cancel_rate = (df["OrderStatus"] == "Cancelled").mean() * 100
return_rate = (df["OrderStatus"] == "Returned").mean() * 100
print(f"Cancellation Rate   : {cancel_rate:.1f}%")
print(f"Return Rate         : {return_rate:.1f}%")
print(f"Avg Order Value     : ${df['TotalPrice'].mean():.2f}")
print(f"Median Order Value  : ${df['TotalPrice'].median():.2f}")
print(f"Avg Qty per Order   : {df['Quantity'].mean():.2f}")

# -------------------- VISUALIZATIONS --------------------
print("\n9. GENERATING VISUALIZATIONS...")

# Product count
fig, ax = plt.subplots()
df["Product"].value_counts().plot(kind="bar", color="#2c5282", ax=ax)
ax.set_title("Order Count by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Number of Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_orders_by_product.png", dpi=150)
plt.close()

# Revenue by product
fig, ax = plt.subplots()
rev_prod["Total_Revenue"].plot(kind="bar", color="#276749", ax=ax)
ax.set_title("Total Revenue by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Revenue ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_revenue_by_product.png", dpi=150)
plt.close()

# Order Status
fig, ax = plt.subplots()
df["OrderStatus"].value_counts().plot(kind="bar", color="#c53030", ax=ax)
ax.set_title("Order Status Distribution")
ax.set_xlabel("Status")
ax.set_ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_order_status.png", dpi=150)
plt.close()

# TotalPrice distribution
fig, ax = plt.subplots()
sns.histplot(df["TotalPrice"], bins=30, kde=True, color="#2b6cb0", ax=ax)
ax.set_title("Distribution of Total Price (Order Value)")
ax.set_xlabel("Total Price ($)")
ax.axvline(df["TotalPrice"].mean(), color="red", linestyle="--", label=f"Mean: ${df['TotalPrice'].mean():.0f}")
ax.axvline(df["TotalPrice"].median(), color="green", linestyle="--", label=f"Median: ${df['TotalPrice'].median():.0f}")
ax.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_totalprice_distribution.png", dpi=150)
plt.close()

# Boxplot TotalPrice
fig, ax = plt.subplots()
sns.boxplot(x=df["TotalPrice"], color="#ed8936", ax=ax)
ax.set_title("Boxplot of Total Price (Outlier View)")
ax.set_xlabel("Total Price ($)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "05_totalprice_boxplot.png", dpi=150)
plt.close()

# Correlation heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, fmt=".2f", ax=ax)
ax.set_title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "06_correlation_heatmap.png", dpi=150)
plt.close()

# Monthly trend
monthly_orders = df.groupby("YearMonth").size()
fig, ax = plt.subplots(figsize=(12, 5))
monthly_orders.plot(kind="line", marker="o", color="#2c5282", ax=ax)
ax.set_title("Monthly Order Volume Trend")
ax.set_xlabel("Year-Month")
ax.set_ylabel("Number of Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "07_monthly_trend.png", dpi=150)
plt.close()

# Referral source
fig, ax = plt.subplots()
df["ReferralSource"].value_counts().plot(kind="bar", color="#805ad5", ax=ax)
ax.set_title("Orders by Referral Source")
ax.set_xlabel("Referral Source")
ax.set_ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "08_referral_source.png", dpi=150)
plt.close()

print(f"All charts saved to: {OUTPUT_DIR}/")
print("\n" + "=" * 70)
print("EDA COMPLETE – Ready for Project Report")
print("=" * 70)