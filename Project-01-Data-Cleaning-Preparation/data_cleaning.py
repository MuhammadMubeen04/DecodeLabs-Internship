"""
DecodeLabs Data Analytics Internship
Project 1: Data Cleaning & Preparation
Batch 2026
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PROJECT 1: DATA CLEANING & PREPARATION")
print("=" * 60)

raw_file = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(raw_file)

print(f"\n[INFO] Loaded raw dataset: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"[INFO] Columns: {list(df.columns)}")

print("\n" + "-" * 60)
print("STEP 1: DATA QUALITY AUDIT")
print("-" * 60)

print(f"\nMissing values per column:")
print(df.isnull().sum())

print(f"\nDuplicate rows: {df.duplicated().sum()}")
print(f"Unique OrderIDs: {df['OrderID'].nunique()} / {len(df)}")
print(f"Unique TrackingNumbers: {df['TrackingNumber'].nunique()} / {len(df)}")

df['_calc'] = df['Quantity'] * df['UnitPrice']
mismatch = (np.abs(df['TotalPrice'] - df['_calc']) > 0.01).sum()
print(f"TotalPrice mismatches (vs Qty × UnitPrice): {mismatch}")
df.drop(columns=['_calc'], inplace=True)

print(f"\nDate range: {df['Date'].min().date()} → {df['Date'].max().date()}")

print("\n" + "-" * 60)
print("STEP 2: APPLYING CLEANING RULES")
print("-" * 60)

df_clean = df.copy()

missing_before = df_clean['CouponCode'].isnull().sum()
df_clean['CouponCode'] = df_clean['CouponCode'].fillna('No Coupon')
print(f"[CR001] Imputed {missing_before} missing CouponCode values with 'No Coupon'")

text_cols = [
    'OrderID', 'CustomerID', 'Product', 'ShippingAddress',
    'PaymentMethod', 'OrderStatus', 'TrackingNumber',
    'CouponCode', 'ReferralSource'
]
for col in text_cols:
    df_clean[col] = df_clean[col].astype(str).str.strip()
print("[CR002] Trimmed whitespace from all text columns")

df_clean['UnitPrice'] = df_clean['UnitPrice'].round(2)
df_clean['TotalPrice'] = df_clean['TotalPrice'].round(2)
print("[CR003] Rounded UnitPrice and TotalPrice to 2 decimal places")

df_clean['Date'] = pd.to_datetime(df_clean['Date'])
print("[CR004] Confirmed Date column is proper datetime (ISO 8601 ready)")

print("\n" + "-" * 60)
print("STEP 3: VERIFICATION GATE (0% ERROR TARGET)")
print("-" * 60)

dup_ids = df_clean['OrderID'].duplicated().sum()
print(f"Duplicate OrderIDs remaining: {dup_ids}  →  {'PASS (0%)' if dup_ids == 0 else 'FAIL'}")

invalid_dates = df_clean['Date'].isnull().sum()
print(f"Invalid / null Dates remaining: {invalid_dates}  →  {'PASS (0%)' if invalid_dates == 0 else 'FAIL'}")

missing_coupon = df_clean['CouponCode'].isnull().sum()
print(f"Missing CouponCode remaining: {missing_coupon}  →  {'PASS' if missing_coupon == 0 else 'FAIL'}")

print(f"\nFinal shape: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
print("All original records preserved (no listwise deletion).")

output_file = "cleaned_dataset.xlsx"
df_clean.to_excel(output_file, index=False, engine='openpyxl')
print(f"\n[SUCCESS] Cleaned dataset saved → {output_file}")

print("\n" + "=" * 60)
print("CLEANING COMPLETE – Ready for Project 2")
print("=" * 60)
