# Data Visualization | DecodeLabs Internship

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Batch](https://img.shields.io/badge/Batch-2026-orange)

**Industrial Training Kit – DecodeLabs | Data Analytics Internship**  
**Optional Mastery Phase: Data Visualization**

---

## Overview

This project focuses on **Data Storytelling** — turning cleaned order data into clear, boardroom-ready visuals that communicate insights in seconds.

**Principles applied:**
- Form follows function (right chart for the question)
- Maximize data-ink ratio (minimal chartjunk)
- Action titles that state the conclusion
- Direct labeling over legends
- Color used as a spotlight for the key insight
- Zero baseline on all bar charts

---

## Charts Created

| # | Chart | Insight Highlighted |
|---|-------|---------------------|
| 1 | Revenue by Product | Chair & Printer lead revenue |
| 2 | Order Status | Cancel + Return = 41% risk |
| 3 | Monthly Order Trend | Stable volume over 30 months |
| 4 | Avg Order Value by Product | Laptop highest AOV ($1,111) |
| 5 | Referral Source Revenue | Instagram top acquisition channel |
| 6 | Payment Method Revenue | Online payments lead |
| 7 | Quantity vs Total Price | Positive quantity–value relationship |
| 8 | KPI Snapshot | $1.26M revenue · 20.8% cancel rate |

---

## Project Structure

```
├── cleaned_dataset.xlsx          # Source data
├── data_visualization.py         # Visualization script
├── viz_outputs/                  # All PNG charts
├── Project_Report_Visualization.docx
└── README.md
```

---

## How to Run

```bash
pip install pandas openpyxl matplotlib seaborn
python data_visualization.py
```

Charts are saved to `viz_outputs/`.

---

## Author

**Data Analyst Intern**  
DecodeLabs | Batch 2026  
Industrial Training Kit – Data Visualization

---

## License

Part of the DecodeLabs Industrial Training program (educational use).
