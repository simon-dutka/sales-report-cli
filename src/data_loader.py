import csv


class MissingFieldsError(Exception):
    pass


def get_data(data_file):
    transactions = []
    missing_value_rows = []
    invalid_data_rows = []

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
            # Check if any field name is missing
            missing_fields = required_fieldnames - set(reader.fieldnames)
            raise MissingFieldsError(
                f"Csv file do not have required fields: {', '.join(missing_fields)}"
            )

        for row_num, row in enumerate(reader, start=2):
            # Check if any value is missing
            if any(not row[field] for field in required_fieldnames):
                missing_value_rows.append(row_num)
                continue

            # Check if value is in right type
            try:
                row["sell_price"] = float(row["sell_price"])
                row["cost_price"] = float(row["cost_price"])
                row["quantity"] = int(row["quantity"])
                transactions.append(row)
            except ValueError:
                invalid_data_rows.append(row_num)

    return transactions, missing_value_rows, invalid_data_rows
