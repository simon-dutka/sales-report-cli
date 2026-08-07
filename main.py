import csv
import shutil


def get_data(data_file):
    transactions = []

    with open(data_file) as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["sell_price"] = float(row["sell_price"])
            row["cost_price"] = float(row["cost_price"])
            row["quantity"] = int(row["quantity"])
            transactions.append(row)

    return transactions


def calculate_overall(transactions):
    overall = {"revenue": 0, "cost": 0, "profit": 0, "margin": 0}

    for transaction in transactions:
        overall["revenue"] += transaction["sell_price"] * transaction["quantity"]

        overall["cost"] += transaction["cost_price"] * transaction["quantity"]

    overall["profit"] = overall["revenue"] - overall["cost"]
    overall["margin"] = overall["profit"] / overall["revenue"] * 100

    return overall


def calculate_by_field(transactions, field_name):
    groups = {}

    for transaction in transactions:
        key = transaction[field_name]

        if key not in groups:
            groups[key] = {"revenue": 0, "cost": 0, "quantity": 0}

        groups[key]["revenue"] += transaction["sell_price"] * transaction["quantity"]
        groups[key]["cost"] += transaction["cost_price"] * transaction["quantity"]
        groups[key]["quantity"] += transaction["quantity"]

    for key, values in groups.items():
        values["profit"] = values["revenue"] - values["cost"]

        values["margin"] = values["profit"] / values["revenue"] * 100

    return groups


def find_top_products(transactions):
    calculated = calculate_by_field(transactions, "product")

    top_revenue = max(calculated.items(), key=lambda item: item[1]["revenue"])
    top_profit = max(calculated.items(), key=lambda item: item[1]["profit"])
    top_quantity = max(calculated.items(), key=lambda item: item[1]["quantity"])

    top_revenue_pair = (top_revenue[0], top_revenue[1]["revenue"])
    top_profit_pair = (top_profit[0], top_profit[1]["profit"])
    top_quantity_pair = (top_quantity[0], top_quantity[1]["quantity"])

    return {
        "by_revenue": top_revenue_pair,
        "by_profit": top_profit_pair,
        "by_quantity": top_quantity_pair,
    }


def print_report(overall, by_category, by_salesperson, top_products):
    terminal_width = shutil.get_terminal_size().columns

    label_width = 12
    name_width = 15
    top_label_width = 16
    indent = "  "

    print(f"{'SALES REPORT':^{terminal_width}}\n")
    print("Overall:")
    print(f"{indent}{'Revenue:':<{label_width}}{overall['revenue']:.2f}")
    print(f"{indent}{'Cost:':<{label_width}}{overall['cost']:.2f}")
    print(f"{indent}{'Profit:':<{label_width}}{overall['profit']:.2f}")
    print(f"{indent}{'Margin:':<{label_width}}{overall['margin']:.2f}%")

    print("\nBy category:")
    for category, values in by_category.items():
        print(
            f"{indent}{category:<{name_width}}revenue: {values['revenue']:.2f}  profit: {values['profit']:.2f}  margin: {values['margin']:.2f}%"
        )

    print("\nBy sales person:")
    for salesperson, values in by_salesperson.items():
        print(
            f"{indent}{salesperson:<{name_width}}revenue: {values['revenue']:.2f}  profit: {values['profit']:.2f}  margin: {values['margin']:.2f}%"
        )

    print("\nTop product:")
    print(
        f"{indent}{'By units sold:':<{top_label_width}}{top_products['by_quantity'][0]} ({top_products['by_quantity'][1]} units)"
    )
    print(
        f"{indent}{'By revenue:':<{top_label_width}}{top_products['by_revenue'][0]} ({top_products['by_revenue'][1]:.2f})"
    )
    print(
        f"{indent}{'By profit:':<{top_label_width}}{top_products['by_profit'][0]} ({top_products['by_profit'][1]:.2f})"
    )
