import csv


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
