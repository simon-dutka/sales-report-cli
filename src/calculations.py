from src.data_loader import get_data


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


def generate_report_data(csv_file):
    transactions = get_data(csv_file)
    overall = calculate_overall(transactions)
    by_category = calculate_by_field(transactions, "category")
    by_salesperson = calculate_by_field(transactions, "salesperson")
    top_products = find_top_products(transactions)
    return overall, by_category, by_salesperson, top_products
