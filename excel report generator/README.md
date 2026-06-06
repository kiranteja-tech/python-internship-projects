# Excel Report Generator (Python Project)

##  Overview

The **Excel Report Generator** is a Python-based desktop application that converts raw CSV datasets into structured and professionally formatted Excel reports. The application performs automatic data analysis, generates statistical summaries, creates pivot tables, and visualizes insights using charts — all through a simple graphical interface.

This project demonstrates practical data processing, visualization, and report automation using Python.

---

##  Features

*  User-friendly GUI using Tkinter
*  CSV file selection through dialog window
*  Automatic data analysis
*  Statistical summary generation:

  * Total
  * Average
  * Maximum
  * Minimum
  * Standard Deviation
    
*  Pivot table creation
*  Bar chart visualization using Matplotlib
*  Multi-sheet Excel report generation
*  User chooses save location
*  Excel file opens automatically after generation

---

##  Technologies Used

| Tool       | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| Tkinter    | GUI Interface        |
| Pandas     | Data Analysis        |
| Matplotlib | Visualization        |
| OpenPyXL   | Excel Automation     |

---

##  Project Structure

```
Excel-Report-Generator/
│
├── main.py
├── real_world_sales_data.csv
├── chart.png
├── README.md
└── project_explaination.txt
```

---

## ⚙️ Installation

Install required libraries:

```bash
pip install pandas matplotlib openpyxl
```

---

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/excel-report-generator.git
```

2. Navigate to project folder:

```bash
cd excel-report-generator
```

3. Run the application:

```bash
python main.py
```

4. Select a CSV file.
5. Choose where to save the Excel report.
6. The report will open automatically.

---

##  Generated Excel Report

The output Excel file contains:

### Sheet 1 — Raw Data

Original dataset imported from CSV.

### Sheet 2 — Summary

Statistical analysis of numeric columns.

### Sheet 3 — Pivot Table

Aggregated insights based on categorical data.

### Sheet 4 — Bar Chart

Visual representation of summarized data.

---

##  Sample Dataset

The included dataset simulates real-world electronic product sales containing:

* Order ID
* Date
* Region
* Salesperson
* Product
* Units Sold
* Unit Price
* Revenue

This dataset demonstrates business analytics and reporting workflows.

---

##  Learning Outcomes

This project showcases:

* Python GUI development
* Data preprocessing and analysis
* Automated reporting systems
* Data visualization techniques
* Excel automation using Python libraries

---

##  Future Improvements

* Multiple chart types
* Dashboard interface
* Dynamic pivot selection
* Export reports to PDF
* Large dataset optimization

---

## reason for devoloping

Developed as an internship project demonstrating real-world data analysis and automated reporting using Python.

---

