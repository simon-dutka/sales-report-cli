import shutil


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
