import csv


class MissingFieldsError(Exception):
    pass


def get_data(data_file):
    transactions = []

    with open(data_file) as file:
        reader = csv.DictReader(file)
        required_fieldnames = {
            "date",
            "product",
            "category",
            "salesperson",
            "cost_price",
            "sell_price",
            "quantity",
        }

        if not required_fieldnames.issubset(reader.fieldnames):
            missing_fields = required_fieldnames - set(reader.fieldnames)
            raise MissingFieldsError(
                f"Csv file do not have required fields: {', '.join(missing_fields)}"
            )

        for row in reader:
            row["sell_price"] = float(row["sell_price"])
            row["cost_price"] = float(row["cost_price"])
            row["quantity"] = int(row["quantity"])
            transactions.append(row)

    return transactions
