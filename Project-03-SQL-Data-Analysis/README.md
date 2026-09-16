# SQL Data Analysis | DecodeLabs Internship

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Batch](https://img.shields.io/badge/Batch-2026-orange)

**Industrial Training Kit – DecodeLabs | Data Analytics Internship**

---

## Overview

This repository contains the complete deliverables for **SQL Data Analysis**.

The goal was to extract actionable business insights from the cleaned order dataset using structured SQL queries — filtering, grouping, aggregating, and sorting data with precision.

**Focus Areas:**
- Writing clean SELECT queries
- Filtering with WHERE
- Sorting with ORDER BY
- Grouping with GROUP BY
- Aggregations: COUNT, SUM, AVG
- Using HAVING for post-aggregation filters

---

## Dataset

| Attribute        | Value                                      |
|------------------|--------------------------------------------|
| Source           | Cleaned dataset from previous milestones   |
| Records          | 1,200 orders                               |
| Database         | SQLite (`orders.db`)                       |
| Table            | `orders`                                   |
| Total Revenue    | $1,264,761.96                              |

---

## Key SQL Queries Included

| #  | Query Focus                                      | Clauses Used                  |
|----|--------------------------------------------------|-------------------------------|
| 1  | Basic SELECT (sample rows)                       | SELECT, LIMIT                 |
| 2  | High-value orders                                | WHERE, ORDER BY               |
| 3  | Cancelled orders                                 | WHERE, ORDER BY               |
| 4  | Order volume by Product                          | GROUP BY, COUNT               |
| 5  | Revenue metrics by Product                       | GROUP BY, COUNT, SUM, AVG     |
| 6  | Order Status distribution                        | GROUP BY, COUNT               |
| 7  | Revenue by Payment Method                        | GROUP BY, SUM, AVG            |
| 8  | Referral Source performance                      | GROUP BY, SUM, AVG            |
| 9  | Delivered revenue by Product                     | WHERE + GROUP BY              |
| 10 | Products with Avg Order Value > 1000             | GROUP BY, HAVING              |
| 11 | High-quantity cancelled orders                   | WHERE (multiple conditions)   |
| 12 | Overall business summary                         | COUNT, SUM, AVG, CASE         |

---

## Project Structure

```
├── cleaned_dataset.xlsx       # Source data
├── orders.db                  # SQLite database
├── sql_analysis.py            # Script that runs all SQL queries
├── sql_outputs/               # Query result tables (Excel)
├── Project_Report_SQL.pdf     # Formal project report
└── README.md                  # This file
```

---

## How to Run

### Prerequisites
```bash
pip install pandas openpyxl
```

### Execute
```bash
python sql_analysis.py
```

The script will:
1. Connect to the SQLite database
2. Execute 12 analytical SQL queries
3. Print results to the console
4. Export each result set as an Excel file in `sql_outputs/`

---

## Tools Used

- **SQLite** – lightweight relational database
- **Python 3** + **Pandas** – query execution and result handling
- **SQL** – SELECT, WHERE, ORDER BY, GROUP BY, HAVING, aggregations

---

## Author

**Data Analyst Intern**  
DecodeLabs | Batch 2026  
Industrial Training Kit – SQL Data Analysis

---

## License

This project is part of the DecodeLabs Industrial Training program and is intended for educational and evaluation purposes.
