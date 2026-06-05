import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if not present
os.makedirs("charts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Load CSV


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "expenses.csv")

print(csv_path)

df = pd.read_csv(csv_path)

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# SUMMARY STATISTICS
# -----------------------------

total_expense = df["Amount"].sum()
average_expense = df["Amount"].mean()
highest_expense = df["Amount"].max()
lowest_expense = df["Amount"].min()

summary_df = pd.DataFrame({
    "Metric": [
        "Total Expense",
        "Average Expense",
        "Highest Expense",
        "Lowest Expense"
    ],
    "Value": [
        total_expense,
        average_expense,
        highest_expense,
        lowest_expense
    ]
})

# -----------------------------
# CATEGORY ANALYSIS
# -----------------------------

category_expense = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

category_df = category_expense.reset_index()

# -----------------------------
# MONTHLY ANALYSIS
# -----------------------------

df["Month"] = df["Date"].dt.strftime("%Y-%m")

monthly_expense = (
    df.groupby("Month")["Amount"]
    .sum()
)

monthly_df = monthly_expense.reset_index()

# -----------------------------
# BUDGET ALERT
# -----------------------------

MONTHLY_BUDGET = 30000

for month, value in monthly_expense.items():
    if value > MONTHLY_BUDGET:
        print(f"WARNING: Budget exceeded in {month}")
        print(f"Spent: ₹{value}")

# -----------------------------
# PIE CHART
# -----------------------------

plt.figure(figsize=(8, 8))
category_expense.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Expense Distribution by Category")
plt.tight_layout()
plt.savefig("charts/pie.png")
plt.close()

# -----------------------------
# BAR CHART
# -----------------------------

plt.figure(figsize=(8, 5))
category_expense.plot(kind="bar")
plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("charts/bar.png")
plt.close()

# -----------------------------
# TREND CHART
# -----------------------------

plt.figure(figsize=(8, 5))
monthly_expense.plot(
    kind="line",
    marker="o"
)
plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Expense")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/trend.png")
plt.close()

# -----------------------------
# EXCEL REPORT
# -----------------------------

with pd.ExcelWriter(
    "reports/Expense_Report.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Raw Data",
        index=False
    )

    summary_df.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    category_df.to_excel(
        writer,
        sheet_name="Category Analysis",
        index=False
    )

print("\nREPORT GENERATED SUCCESSFULLY")
print("charts/pie.png")
print("charts/bar.png")
print("charts/trend.png")
print("reports/Expense_Report.xlsx")