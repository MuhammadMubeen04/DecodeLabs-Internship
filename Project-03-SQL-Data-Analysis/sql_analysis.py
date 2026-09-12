"""
DecodeLabs Data Analytics Internship
Project 3: SQL Data Analysis
Batch 2026
"""

import pandas as pd
import sqlite3
from pathlib import Path

OUTPUT_DIR = Path("sql_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

conn = sqlite3.connect("orders.db")

def run_query(title, sql, filename=None):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
    print(sql.strip())
    print("-" * 70)
    df = pd.read_sql(sql, conn)
    print(df.to_string(index=False))
    if filename:
        df.to_excel(OUTPUT_DIR / filename, index=False)
        print(f"[Saved] {filename}")
    return df

# ---------------------------------------------------------
# 1. Basic SELECT
# ---------------------------------------------------------
run_query(
    "1. BASIC SELECT – First 10 orders",
    """
    SELECT OrderID, Date, Product, Quantity, TotalPrice, OrderStatus
    FROM orders
    LIMIT 10;
    """,
    "01_basic_select.xlsx"
)

# ---------------------------------------------------------
# 2. WHERE – Filter high-value orders
# ---------------------------------------------------------
run_query(
    "2. WHERE – High-value orders (TotalPrice > 2000)",
    """
    SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice, OrderStatus
    FROM orders
    WHERE TotalPrice > 2000
    ORDER BY TotalPrice DESC;
    """,
    "02_high_value_orders.xlsx"
)

# ---------------------------------------------------------
# 3. WHERE + ORDER BY – Cancelled orders
# ---------------------------------------------------------
run_query(
    "3. WHERE + ORDER BY – Cancelled orders sorted by value",
    """
    SELECT OrderID, Product, TotalPrice, PaymentMethod, ReferralSource
    FROM orders
    WHERE OrderStatus = 'Cancelled'
    ORDER BY TotalPrice DESC;
    """,
    "03_cancelled_orders.xlsx"
)

# ---------------------------------------------------------
# 4. GROUP BY + COUNT – Orders by Product
# ---------------------------------------------------------
run_query(
    "4. GROUP BY + COUNT – Order volume by Product",
    """
    SELECT Product,
           COUNT(*) AS OrderCount
    FROM orders
    GROUP BY Product
    ORDER BY OrderCount DESC;
    """,
    "04_orders_by_product.xlsx"
)

# ---------------------------------------------------------
# 5. GROUP BY + SUM + AVG – Revenue by Product
# ---------------------------------------------------------
run_query(
    "5. GROUP BY + SUM + AVG – Revenue metrics by Product",
    """
    SELECT Product,
           COUNT(*) AS OrderCount,
           SUM(TotalPrice) AS TotalRevenue,
           AVG(TotalPrice) AS AvgOrderValue,
           SUM(Quantity) AS TotalUnitsSold
    FROM orders
    GROUP BY Product
    ORDER BY TotalRevenue DESC;
    """,
    "05_revenue_by_product.xlsx"
)

# ---------------------------------------------------------
# 6. GROUP BY + COUNT – Order Status distribution
# ---------------------------------------------------------
run_query(
    "6. GROUP BY – Order Status distribution",
    """
    SELECT OrderStatus,
           COUNT(*) AS OrderCount,
           ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 1) AS Percentage
    FROM orders
    GROUP BY OrderStatus
    ORDER BY OrderCount DESC;
    """,
    "06_order_status.xlsx"
)

# ---------------------------------------------------------
# 7. GROUP BY – Revenue by Payment Method
# ---------------------------------------------------------
run_query(
    "7. GROUP BY – Revenue by Payment Method",
    """
    SELECT PaymentMethod,
           COUNT(*) AS OrderCount,
           SUM(TotalPrice) AS TotalRevenue,
           AVG(TotalPrice) AS AvgOrderValue
    FROM orders
    GROUP BY PaymentMethod
    ORDER BY TotalRevenue DESC;
    """,
    "07_payment_method.xlsx"
)

# ---------------------------------------------------------
# 8. GROUP BY – Referral Source performance
# ---------------------------------------------------------
run_query(
    "8. GROUP BY – Referral Source performance",
    """
    SELECT ReferralSource,
           COUNT(*) AS OrderCount,
           SUM(TotalPrice) AS TotalRevenue,
           AVG(TotalPrice) AS AvgOrderValue
    FROM orders
    GROUP BY ReferralSource
    ORDER BY TotalRevenue DESC;
    """,
    "08_referral_source.xlsx"
)

# ---------------------------------------------------------
# 9. WHERE + GROUP BY – Revenue of Delivered orders only
# ---------------------------------------------------------
run_query(
    "9. WHERE + GROUP BY – Revenue from Delivered orders by Product",
    """
    SELECT Product,
           COUNT(*) AS DeliveredOrders,
           SUM(TotalPrice) AS DeliveredRevenue,
           AVG(TotalPrice) AS AvgDeliveredValue
    FROM orders
    WHERE OrderStatus = 'Delivered'
    GROUP BY Product
    ORDER BY DeliveredRevenue DESC;
    """,
    "09_delivered_by_product.xlsx"
)

# ---------------------------------------------------------
# 10. HAVING – Products with average order value > 1000
# ---------------------------------------------------------
run_query(
    "10. HAVING – Products with Avg Order Value > 1000",
    """
    SELECT Product,
           COUNT(*) AS OrderCount,
           AVG(TotalPrice) AS AvgOrderValue,
           SUM(TotalPrice) AS TotalRevenue
    FROM orders
    GROUP BY Product
    HAVING AVG(TotalPrice) > 1000
    ORDER BY AvgOrderValue DESC;
    """,
    "10_high_aov_products.xlsx"
)

# ---------------------------------------------------------
# 11. Multiple conditions – High quantity cancelled orders
# ---------------------------------------------------------
run_query(
    "11. WHERE (multiple conditions) – Cancelled orders with Quantity >= 4",
    """
    SELECT OrderID, Product, Quantity, TotalPrice, CouponCode
    FROM orders
    WHERE OrderStatus = 'Cancelled'
      AND Quantity >= 4
    ORDER BY TotalPrice DESC;
    """,
    "11_high_qty_cancelled.xlsx"
)

# ---------------------------------------------------------
# 12. Overall business summary
# ---------------------------------------------------------
run_query(
    "12. Overall Business Summary",
    """
    SELECT
        COUNT(*) AS TotalOrders,
        COUNT(DISTINCT CustomerID) AS UniqueCustomers,
        COUNT(DISTINCT Product) AS UniqueProducts,
        SUM(TotalPrice) AS TotalRevenue,
        AVG(TotalPrice) AS AvgOrderValue,
        SUM(CASE WHEN OrderStatus = 'Cancelled' THEN 1 ELSE 0 END) AS CancelledOrders,
        SUM(CASE WHEN OrderStatus = 'Returned' THEN 1 ELSE 0 END) AS ReturnedOrders,
        SUM(CASE WHEN OrderStatus = 'Delivered' THEN 1 ELSE 0 END) AS DeliveredOrders
    FROM orders;
    """,
    "12_business_summary.xlsx"
)

conn.close()
print("\n" + "=" * 70)
print("SQL DATA ANALYSIS COMPLETE")
print(f"All result tables saved to: {OUTPUT_DIR}/")
print("=" * 70)
