# Data Cleaning & Preparation | DecodeLabs Internship Project 1

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Batch](https://img.shields.io/badge/Batch-2026-orange)

**Industrial Training Kit – DecodeLabs | Data Analytics Internship**

---

## Overview

This repository contains the complete deliverables for **Project 1: Data Cleaning & Preparation**.

The goal of this project was to transform a raw e-commerce order dataset into a clean, reliable, analysis-ready dataset by applying professional data integrity practices.

**Focus Areas:**
- Handling missing values (strategic imputation)
- Removing / verifying duplicates
- Standardizing data formats
- Documenting cleaning steps for reproducibility
- Achieving **0% error rate** on unique identifiers and date formats

---

## Dataset

| Attribute              | Value                          |
|------------------------|--------------------------------|
| Source File            | `Dataset for Data Analytics.xlsx` |
| Records                | 1,200 orders                   |
| Columns                | 14                             |
| Date Range             | 2023-01-01 → 2025-06-30        |
| Primary Key            | `OrderID`                      |

**Columns:**  
`OrderID`, `Date`, `CustomerID`, `Product`, `Quantity`, `UnitPrice`, `ShippingAddress`, `PaymentMethod`, `OrderStatus`, `TrackingNumber`, `ItemsInCart`, `CouponCode`, `ReferralSource`, `TotalPrice`

---

## Data Quality Findings

| Check                        | Result                          |
|------------------------------|---------------------------------|
| Duplicate rows               | 0                               |
| Duplicate OrderIDs           | 0                               |
| Duplicate TrackingNumbers    | 0                               |
| Missing values               | 309 in `CouponCode` (25.75%)    |
| TotalPrice calculation errors| 0                               |
| Invalid dates                | 0                               |
| Whitespace issues            | 0                               |

---

## Cleaning Actions Performed

| Change ID | Description                                      | Impact                              | Status   |
|-----------|--------------------------------------------------|-------------------------------------|----------|
| CR001     | Imputed missing `CouponCode` with `"No Coupon"`  | Preserved all 1,200 records         | Resolved |
| CR002     | Trimmed whitespace from all text columns         | Ensured string consistency          | Resolved |
| CR003     | Rounded `UnitPrice` & `TotalPrice` to 2 decimals | Standardized monetary precision     | Resolved |
| CR004     | Validated `Date` as proper datetime (ISO 8601)   | 0 invalid dates                     | Resolved |
| CR005     | Verified uniqueness of IDs & calculation integrity | 100% data integrity confirmed     | Resolved |

> **Note:** Listwise deletion was deliberately avoided to preserve statistical power, following industry best practices.

---

## Verification Gate (Project 2 Unlock Criteria)

| Metric                     | Result     | Status              |
|----------------------------|------------|---------------------|
| Error rate on Unique IDs   | 0%         | **PASS**            |
| Error rate on Date Formats | 0%         | **PASS**            |
| Missing CouponCode (after) | 0          | **PASS**            |
| Calculation mismatches     | 0          | **PASS**            |

---

## Project Structure

```
├── Dataset for Data Analytics.xlsx   # Original raw dataset
├── cleaned_dataset.xlsx              # Final cleaned dataset
├── data_cleaning.py                  # Reproducible Python cleaning script
├── Project_Report.docx               # Formal project report
└── README.md                         # This file
```

---

## How to Run

### Prerequisites
```bash
pip install pandas openpyxl numpy
```

### Execute the cleaning script
```bash
python data_cleaning.py
```

The script will:
1. Load the raw dataset
2. Perform a full data quality audit
3. Apply all cleaning rules
4. Validate the Verification Gate
5. Export `cleaned_dataset.xlsx`

---

## Tools Used

- **Python 3** + **Pandas** – primary cleaning engine
- **openpyxl** – Excel read/write support
- **python-docx** – Word document generation for the project report

---

## Key Principles Applied

- **Data Integrity First** – No silent data loss
- **Reproducibility** – Every step is scripted
- **Documentation** – Formal Change Log for stakeholder transparency
- **Professional Standards** – Follows the 80/20 rule of data science (80% cleaning, 20% analysis)

---

## Author

**Data Analyst Intern**  
DecodeLabs | Batch 2026  
Industrial Training Kit – Project 1

---

## License

This project is part of the DecodeLabs Industrial Training program and is intended for educational and evaluation purposes.
