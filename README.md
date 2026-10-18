# Sales Report CLI

A command-line tool that reads a sales CSV file and generates a summary report: overall revenue, cost, profit and margin, a breakdown by category and by salesperson, and the top products. Reports can be printed to the terminal or exported to a text file.

## Features

- Interactive menu (arrow keys) built with `inquirer`
- Choose a CSV file from the `data/` folder
- Report sections: overall totals, by category, by salesperson, top product (by units sold, revenue and profit)
- Export to `reports/` with automatic file numbering, so reports from the same day are never overwritten
- Input validation:
    - a CSV missing required columns is rejected with a message listing the missing columns
    - rows with missing or invalid values are skipped, and their row numbers are shown at the top of the report (on screen and in the exported file)
- Zero-revenue safe: margin is reported as `0` instead of crashing

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Installation

```bash
git clone <repo-url>
cd sales-report-cli

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Menu options:

| Option                     | What it does                                             |
| -------------------------- | -------------------------------------------------------- |
| Load csv file              | Pick a `.csv` file from the `data/` folder               |
| Generate text report       | Print the report for the loaded file                     |
| Export report to text file | Save the report to `reports/report_<YYYY-MM-DD>_<n>.txt` |
| Exit                       | Quit the program                                         |

If `data/` does not exist it is created automatically. Place your CSV files there (a sample is included).

## CSV format

The file must contain a header row with these columns (order does not matter, extra columns are ignored):

| Column        | Type    | Description               |
| ------------- | ------- | ------------------------- |
| `date`        | text    | Transaction date          |
| `product`     | text    | Product name              |
| `category`    | text    | Product category          |
| `salesperson` | text    | Who made the sale         |
| `cost_price`  | number  | Cost of one unit          |
| `sell_price`  | number  | Selling price of one unit |
| `quantity`    | integer | Units sold                |

Example:

```csv
date,product,category,salesperson,cost_price,sell_price,quantity
2026-01-05,Laptop,Electronics,Ann,2400,3200,1
2026-01-05,Mouse,Electronics,Ann,40,80,3
2026-01-06,Desk,Furniture,Bob,400,650,1
```

Revenue is `sell_price × quantity`, cost is `cost_price × quantity`, profit is `revenue − cost`, and margin is `profit / revenue × 100`.

## Example report

Generated from `data/sample_sales.csv`:

```text
SALES REPORT

Overall:
  Revenue:    20960.00
  Cost:       14570.00
  Profit:     6390.00
  Margin:     30.49%

By category:
  Electronics    revenue: 16760.00  profit: 4720.00  margin: 28.16%
  Furniture      revenue: 4200.00  profit: 1670.00  margin: 39.76%

By sales person:
  Ann            revenue: 8160.00  profit: 2300.00  margin: 28.19%
  Bob            revenue: 3800.00  profit: 1430.00  margin: 37.63%
  Cara           revenue: 9000.00  profit: 2660.00  margin: 29.56%

Top product:
  By units sold:  Mouse (12 units)
  By revenue:     Laptop (12800.00)
  By profit:      Laptop (3200.00)
```

If any rows were skipped, an `Errors:` section listing their row numbers appears right below the title.

## Project structure

```text
sales-report-cli/
├── main.py              # entry point: runs the menu loop
├── src/
│   ├── data_loader.py   # reads and validates the CSV
│   ├── calculations.py  # totals, grouping, top products
│   ├── report.py        # builds, prints and saves the report
│   └── interface.py     # interactive menu (inquirer)
├── tests/
│   └── test_calculations.py
├── data/                # input CSV files
├── reports/             # exported reports (git-ignored)
├── pytest.ini
└── requirements.txt
```

Calculation logic is kept separate from output and user interaction, so the calculation functions are pure and easy to test.

## Running tests

```bash
pytest
```

The tests cover the calculation logic (`calculate_overall`, `calculate_by_field`), including multiple transactions, quantity handling and the zero-revenue edge case.

## Future improvements

- Configurable column names, so CSV files with a different layout can be used
- Standalone executable (e.g. PyInstaller)
- Tests for `find_top_products` and `get_data`
- Graceful handling of Ctrl+C in the menu
- Edge cases in report file naming
