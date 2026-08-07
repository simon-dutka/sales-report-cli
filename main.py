from src.calculations import calculate_by_field, calculate_overall, find_top_products
from src.data_loader import get_data
from src.report import print_report


def main():
    csv_file = "./data/sample_sales.csv"

    transactions = get_data(csv_file)
    overall = calculate_overall(transactions)
    by_category = calculate_by_field(transactions, "category")
    by_salesperson = calculate_by_field(transactions, "salesperson")
    top_products = find_top_products(transactions)

    print_report(overall, by_category, by_salesperson, top_products)


if __name__ == "__main__":
    main()
