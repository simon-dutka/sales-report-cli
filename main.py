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
