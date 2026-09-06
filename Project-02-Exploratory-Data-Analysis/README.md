# Exploratory Data Analysis (EDA) | DecodeLabs Internship

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Batch](https://img.shields.io/badge/Batch-2026-orange)

**Industrial Training Kit – DecodeLabs | Data Analytics Internship**

---

## Overview

This repository contains the complete deliverables for **Exploratory Data Analysis (EDA)**.

The goal was to move beyond raw tables and uncover the **story** hidden inside the cleaned order dataset — patterns, trends, outliers, and business-relevant insights.

**Focus Areas:**
- Descriptive statistics (mean, median, count, distribution)
- Trend and outlier identification
- Correlation analysis
- Business-oriented “So What?” insights
- Clear visual evidence for stakeholders

---

## Dataset

| Attribute           | Value                                      |
|---------------------|--------------------------------------------|
| Source              | Cleaned dataset from Data Cleaning project |
| Records             | 1,200 orders                               |
| Date Range          | 2023-01-01 → 2025-06-30                    |
| Unique Customers    | 1,189                                      |
| Unique Products     | 7                                          |
| Total Revenue       | $1,264,761.96                              |

---

## Key Findings

| Metric                    | Result                          |
|---------------------------|---------------------------------|
| Average Order Value       | $1,053.97                       |
| Median Order Value        | $823.62                         |
| Cancellation Rate         | 20.8%                           |
| Return Rate               | 20.6%                           |
| TotalPrice Outliers (IQR) | 8 orders (0.7%)                 |
| Strongest Correlation     | UnitPrice ↔ TotalPrice (0.72)   |

**Business Signals:**
- High cancellation + return rates (~41% combined) indicate friction in the order lifecycle.
- Revenue is fairly balanced across products; Chair, Printer, and Laptop lead slightly.
- Order value distribution is right-skewed (mean > median) — a few high-value orders pull the average up.
- Quantity and ItemsInCart are moderately correlated (0.65).

---

## Project Structure

```
├── cleaned_dataset.xlsx          # Input: cleaned order data
├── eda_analysis.py               # Full EDA script (stats + charts)
├── eda_outputs/                  # Generated tables & visualizations
│   ├── descriptive_statistics.xlsx
│   ├── revenue_by_product.xlsx
│   ├── correlation_matrix.xlsx
│   ├── outliers_totalprice.xlsx
│   └── *.png charts
├── Project_Report.pdf            # Formal project report
└── README.md                     # This file
```

---

## How to Run

### Prerequisites
```bash
pip install pandas openpyxl numpy matplotlib seaborn
```

### Execute
```bash
python eda_analysis.py
```

The script will:
1. Load the cleaned dataset
2. Compute descriptive statistics and distributions
3. Detect outliers using the IQR method
4. Build a correlation matrix
5. Generate business metrics and charts
6. Export tables and PNG visualizations to `eda_outputs/`

---

## Tools Used

- **Python 3** + **Pandas** – data analysis
- **Matplotlib / Seaborn** – visualizations
- **NumPy** – numerical calculations

---

## Author

**Data Analyst Intern**  
DecodeLabs | Batch 2026  
Industrial Training Kit – Exploratory Data Analysis

---

## License

This project is part of the DecodeLabs Industrial Training program and is intended for educational and evaluation purposes.
