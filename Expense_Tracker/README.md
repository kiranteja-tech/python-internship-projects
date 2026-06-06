# Expense Tracker with Data Visualization

## Project Overview

Expense Tracker is a Python-based data analysis project designed to monitor and analyze personal expenses. The application reads expense records from a CSV file, performs statistical analysis, generates visualizations, and exports summarized reports to Excel.

The project demonstrates practical applications of data analysis, reporting automation, and data visualization using Python libraries.

---

## Features

* Read expense records from CSV files
* Categorize expenses automatically
* Calculate key expense statistics
* Generate category-wise spending analysis
* Create monthly expense summaries
* Budget monitoring and alerts
* Generate visual reports using charts
* Export reports to Excel format

---

## Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming Language         |
| Pandas     | Data Analysis and Processing |
| Matplotlib | Data Visualization           |
| OpenPyXL   | Excel Report Generation      |

---

## Project Structure

```text
Expense_Tracker/
│
├── data/
│   └── expenses.csv
│
├── charts/
│   ├── pie.png
│   ├── bar.png
│   └── trend.png
│
├── reports/
│   └── Expense_Report.xlsx
│
├── main.py
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/expense-tracker.git
```

2. Move into the project directory:

```bash
cd expense-tracker
```

3. Ensure the dataset is present:

```text
data/expenses.csv
```

4. Run the application:

```bash
python main.py
```

---

## Input Dataset

The project uses a CSV dataset containing expense information.

Example:

```csv
Date,Category,Description,Amount
2025-01-02,Food,Breakfast,80
2025-01-03,Travel,Bus Pass,150
2025-01-04,Bills,Electricity Bill,1850
```

---

## Statistical Analysis

The program calculates:

* Total Expense
* Average Expense
* Highest Expense
* Lowest Expense
* Category-wise Expense
* Monthly Expense Summary

---

## Budget Monitoring

The application supports budget tracking.

If monthly expenses exceed the predefined budget limit, the program displays a warning message.

Example:

```text
WARNING: Budget exceeded in 2025-01
Spent: ₹35000
```

---

## Generated Visualizations

### Pie Chart

Displays percentage distribution of expenses across categories.

Output:

```text
charts/pie.png
```

### Bar Chart

Displays category-wise spending comparison.

Output:

```text
charts/bar.png
```

### Trend Chart

Displays monthly expense trends over time.

Output:

```text
charts/trend.png
```

---

## Excel Report

The application generates an Excel report:

```text
reports/Expense_Report.xlsx
```

The report contains:

### Sheet 1 - Raw Data

Original expense records.

### Sheet 2 - Summary

Statistical analysis results.

### Sheet 3 - Category Analysis

Category-wise expense breakdown.

---

## Learning Outcomes

This project demonstrates:

* Data preprocessing using Pandas
* Expense analysis techniques
* Data visualization using Matplotlib
* Automated report generation
* Excel file handling using OpenPyXL
* Practical financial data analysis

---

## Future Enhancements

* Graphical User Interface (GUI)
* PDF report generation
* Expense filtering by date range
* Interactive dashboards
* Database integration
* Multiple user support

---


Internship project developed to demonstrate data analysis, visualization, and report generation using Python.

---

## License

This project is intended for educational and learning purposes.
