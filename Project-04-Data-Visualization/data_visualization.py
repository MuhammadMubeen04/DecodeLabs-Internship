"""
DecodeLabs Data Analytics Internship
Project 4: Data Visualization
Batch 2026

Principles applied:
- Form follows function (right chart for the question)
- Maximize data-ink ratio (minimal chartjunk)
- Action titles that state the conclusion
- Direct labeling instead of legends where possible
- Color used as a spotlight for the key insight
- Zero baseline on bar charts
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="white", palette="muted")
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

OUTPUT = Path("viz_outputs")
OUTPUT.mkdir(exist_ok=True)

df = pd.read_excel("cleaned_dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)

ACCENT = "#2B6CB0"
MUTED = "#A0AEC0"
DARK = "#2D3748"

print("Generating visualizations...")

# 1. Revenue by Product
rev = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 5))
colors = [ACCENT if v == rev.max() else MUTED for v in rev.values]
bars = ax.barh(rev.index, rev.values, color=colors, height=0.65)
ax.set_xlabel("Total Revenue ($)")
ax.set_title("Chair and Printer lead revenue — nearly equal top performers", loc="left", color=DARK, pad=12)
for bar, val in zip(bars, rev.values):
    ax.text(val + 2000, bar.get_y() + bar.get_height()/2, f"${val:,.0f}", va="center", fontsize=9, color=DARK)
ax.set_xlim(0, rev.max() * 1.18)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "01_revenue_by_product.png", dpi=160, bbox_inches="tight")
plt.close()

# 2. Order Status
status = df["OrderStatus"].value_counts().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 4.5))
colors = ["#C53030" if s in ["Cancelled", "Returned"] else MUTED for s in status.index]
bars = ax.barh(status.index, status.values, color=colors, height=0.6)
ax.set_xlabel("Number of Orders")
ax.set_title("Cancellation + Return = 41% of all orders — major operational risk", loc="left", color=DARK, pad=12)
for bar, val in zip(bars, status.values):
    pct = val / len(df) * 100
    ax.text(val + 5, bar.get_y() + bar.get_height()/2, f"{val} ({pct:.0f}%)", va="center", fontsize=9, color=DARK)
ax.set_xlim(0, status.max() * 1.25)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "02_order_status.png", dpi=160, bbox_inches="tight")
plt.close()

# 3. Monthly Trend
monthly = df.groupby("YearMonth").size()
fig, ax = plt.subplots(figsize=(11, 4.5))
ax.plot(monthly.index, monthly.values, color=ACCENT, linewidth=2.2, marker="o", markersize=4)
ax.fill_between(range(len(monthly)), monthly.values, alpha=0.12, color=ACCENT)
ax.set_ylabel("Orders")
ax.set_title("Order volume remains relatively stable across 30 months", loc="left", color=DARK, pad=12)
ax.set_xticks(range(0, len(monthly), 3))
ax.set_xticklabels(monthly.index[::3], rotation=45, ha="right", fontsize=8)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
ax.set_ylim(0, monthly.max() * 1.15)
plt.tight_layout()
plt.savefig(OUTPUT / "03_monthly_trend.png", dpi=160, bbox_inches="tight")
plt.close()

# 4. AOV by Product
aov = df.groupby("Product")["TotalPrice"].mean().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 5))
colors = [ACCENT if v == aov.max() else MUTED for v in aov.values]
bars = ax.barh(aov.index, aov.values, color=colors, height=0.65)
ax.set_xlabel("Average Order Value ($)")
ax.set_title("Laptop has the highest average order value at $1,111", loc="left", color=DARK, pad=12)
for bar, val in zip(bars, aov.values):
    ax.text(val + 15, bar.get_y() + bar.get_height()/2, f"${val:,.0f}", va="center", fontsize=9, color=DARK)
ax.set_xlim(0, aov.max() * 1.15)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "04_aov_by_product.png", dpi=160, bbox_inches="tight")
plt.close()

# 5. Referral Source
ref = df.groupby("ReferralSource")["TotalPrice"].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 4.5))
colors = [ACCENT if v == ref.max() else MUTED for v in ref.values]
bars = ax.barh(ref.index, ref.values, color=colors, height=0.6)
ax.set_xlabel("Total Revenue ($)")
ax.set_title("Instagram drives the highest revenue among referral sources", loc="left", color=DARK, pad=12)
for bar, val in zip(bars, ref.values):
    ax.text(val + 1500, bar.get_y() + bar.get_height()/2, f"${val:,.0f}", va="center", fontsize=9, color=DARK)
ax.set_xlim(0, ref.max() * 1.18)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "05_referral_revenue.png", dpi=160, bbox_inches="tight")
plt.close()

# 6. Payment Method
pay = df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(9, 4.5))
colors = [ACCENT if v == pay.max() else MUTED for v in pay.values]
bars = ax.barh(pay.index, pay.values, color=colors, height=0.6)
ax.set_xlabel("Total Revenue ($)")
ax.set_title("Online payments contribute the largest share of revenue", loc="left", color=DARK, pad=12)
for bar, val in zip(bars, pay.values):
    ax.text(val + 1500, bar.get_y() + bar.get_height()/2, f"${val:,.0f}", va="center", fontsize=9, color=DARK)
ax.set_xlim(0, pay.max() * 1.18)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "06_payment_revenue.png", dpi=160, bbox_inches="tight")
plt.close()

# 7. Scatter
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["Quantity"], df["TotalPrice"], alpha=0.35, s=28, color=ACCENT, edgecolors="none")
ax.set_xlabel("Quantity")
ax.set_ylabel("Total Price ($)")
ax.set_title("Higher quantities generally drive higher order values", loc="left", color=DARK, pad=12)
ax.spines["left"].set_color(MUTED)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
plt.savefig(OUTPUT / "07_quantity_vs_price.png", dpi=160, bbox_inches="tight")
plt.close()

# 8. KPI Snapshot
fig, axes = plt.subplots(1, 4, figsize=(12, 2.8))
kpis = [
    ("Total Revenue", f"${df['TotalPrice'].sum()/1e6:.2f}M"),
    ("Avg Order Value", f"${df['TotalPrice'].mean():.0f}"),
    ("Cancel Rate", f"{(df['OrderStatus']=='Cancelled').mean()*100:.1f}%"),
    ("Return Rate", f"{(df['OrderStatus']=='Returned').mean()*100:.1f}%"),
]
for ax, (label, value) in zip(axes, kpis):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.5, 0.62, value, ha="center", va="center", fontsize=22, fontweight="bold", color=ACCENT)
    ax.text(0.5, 0.28, label, ha="center", va="center", fontsize=11, color=DARK)
fig.suptitle("Key Performance Snapshot — 1,200 Orders | Jan 2023 – Jun 2025",
             fontsize=12, fontweight="bold", color=DARK, y=1.02)
plt.tight_layout()
plt.savefig(OUTPUT / "08_kpi_snapshot.png", dpi=160, bbox_inches="tight")
plt.close()

print(f"All charts saved to {OUTPUT}/")
print("Data Visualization complete.")