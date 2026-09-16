# Data Visualization | DecodeLabs Internship

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Batch](https://img.shields.io/badge/Batch-2026-orange)

**Industrial Training Kit – DecodeLabs | Data Analytics Internship**  
**Optional Mastery Phase: Data Visualization**

---

## Overview

This repository contains the complete deliverables for **Data Visualization**.

The goal was to translate cleaned order data into clear, boardroom-ready visuals that communicate insights within seconds — focusing on data storytelling rather than decorative charts.

**Focus Areas:**
- Choosing the right chart type for the business question
- Maximizing data-ink ratio (minimal chartjunk)
- Writing action titles that state the conclusion
- Using color as a spotlight for the key insight
- Direct labeling over legends
- Answering the “So What?” for every visual

---

## Dataset

| Attribute        | Value                                      |
|------------------|--------------------------------------------|
| Source           | Cleaned dataset from previous milestones   |
| Records          | 1,200 orders                               |
| Date Range       | Jan 2023 – Jun 2025                        |
| Total Revenue    | $1,264,761.96                              |
| Avg Order Value  | $1,053.97                                  |

---

## Charts Created

| #  | Chart Focus                                      | Insight Highlighted                          |
|----|--------------------------------------------------|----------------------------------------------|
| 1  | Revenue by Product (horizontal bar)              | Chair & Printer lead revenue                 |
| 2  | Order Status distribution                        | Cancel + Return = 41% operational risk       |
| 3  | Monthly Order Trend (line)                       | Stable volume across 30 months               |
| 4  | Average Order Value by Product                   | Laptop highest AOV ($1,111)                  |
| 5  | Referral Source revenue                          | Instagram top acquisition channel            |
| 6  | Payment Method revenue                           | Online payments contribute largest share     |
| 7  | Quantity vs Total Price (scatter)                | Positive quantity–value relationship         |
| 8  | KPI Snapshot                                     | $1.26M revenue · 20.8% cancel rate           |

---

## Project Structure

```
├── cleaned_dataset.xlsx                 # Source data
├── data_visualization.py                # Visualization script
├── viz_outputs/                         # All PNG charts
│   ├── 01_revenue_by_product.png
│   ├── 02_order_status.png
│   ├── 03_monthly_trend.png
│   ├── 04_aov_by_product.png
│   ├── 05_referral_revenue.png
│   ├── 06_payment_revenue.png
│   ├── 07_quantity_vs_price.png
│   └── 08_kpi_snapshot.png
├── Project_Report_Visualization.docx    # Formal project report
└── README.md                            # This file
```

---

## How to Run

### Prerequisites
```bash
pip install pandas openpyxl matplotlib seaborn
```

### Execute
```bash
python data_visualization.py
```

The script will:
1. Load the cleaned order dataset
2. Generate 8 insight-driven charts
3. Apply action titles and direct labeling
4. Save all PNGs to the `viz_outputs/` folder

---

## Design Principles Applied

- **Form follows function** — chart type matched to the analytical question
- **Axis integrity** — zero baseline on all bar charts
- **Data-ink ratio** — removed unnecessary grids, borders, and decoration
- **Action titles** — titles state the conclusion, not just the topic
- **Spotlight color** — single accent color highlights the key insight
- **Direct labels** — values shown on bars to reduce cognitive load

---

## Tools Used

- **Python 3** + **Pandas** – data loading and aggregation
- **Matplotlib** – core chart rendering
- **Seaborn** – clean theme and styling

---

## Author

**Data Analyst Intern**  
DecodeLabs | Batch 2026  
Industrial Training Kit – Data Visualization

---

## License

This project is part of the DecodeLabs Industrial Training program and is intended for educational and evaluation purposes.
