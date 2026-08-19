import os
from datetime import datetime, timezone


def build_report_lines(
    overall,
    by_category,
    by_salesperson,
    top_products,
    missing_value_rows,
    invalid_data_rows,
):
    lines = []

    label_width = 12
    name_width = 15
    top_label_width = 16
    indent = "  "

    lines.append("SALES REPORT")

    if missing_value_rows or invalid_data_rows:
        lines.append("\nERRORS:")

        if missing_value_rows:
            lines.append(
                f"{indent}Rows skipped (missing values): {', '.join(str(n) for n in missing_value_rows)}"
            )

        if invalid_data_rows:
            lines.append(
                f"{indent}Rows skipped (invalid data): {', '.join(str(n) for n in invalid_data_rows)}"
            )

    lines.append("\nOverall:")
    lines.append(f"{indent}{'Revenue:':<{label_width}}{overall['revenue']:.2f}")
    lines.append(f"{indent}{'Cost:':<{label_width}}{overall['cost']:.2f}")
    lines.append(f"{indent}{'Profit:':<{label_width}}{overall['profit']:.2f}")
    lines.append(f"{indent}{'Margin:':<{label_width}}{overall['margin']:.2f}%")

    lines.append("\nBy category:")
    for category, values in by_category.items():
        lines.append(
            f"{indent}{category:<{name_width}}revenue: {values['revenue']:.2f}  profit: {values['profit']:.2f}  margin: {values['margin']:.2f}%"
        )

    lines.append("\nBy sales person:")
    for salesperson, values in by_salesperson.items():
        lines.append(
            f"{indent}{salesperson:<{name_width}}revenue: {values['revenue']:.2f}  profit: {values['profit']:.2f}  margin: {values['margin']:.2f}%"
        )

    lines.append("\nTop product:")
    lines.append(
        f"{indent}{'By units sold:':<{top_label_width}}{top_products['by_quantity'][0]} ({top_products['by_quantity'][1]} units)"
    )
    lines.append(
        f"{indent}{'By revenue:':<{top_label_width}}{top_products['by_revenue'][0]} ({top_products['by_revenue'][1]:.2f})"
    )
    lines.append(
        f"{indent}{'By profit:':<{top_label_width}}{top_products['by_profit'][0]} ({top_products['by_profit'][1]:.2f})"
    )

    return lines


def print_report(
    overall,
    by_category,
    by_salesperson,
    top_products,
    missing_value_rows,
    invalid_data_rows,
):
    lines = build_report_lines(
        overall,
        by_category,
        by_salesperson,
        top_products,
        missing_value_rows,
        invalid_data_rows,
    )
    for line in lines:
        print(line)


def get_report_filename(folder):
    counter = 1
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    while True:
        filepath = f"{folder}/report_{timestamp}_{counter}.txt"
        if not os.path.exists(filepath):
            return filepath
        counter += 1


def save_report_to_file(
    overall,
    by_category,
    by_salesperson,
    top_products,
    missing_value_rows,
    invalid_data_rows,
    folder,
):
    filename = get_report_filename(folder)

    lines = build_report_lines(
        overall,
        by_category,
        by_salesperson,
        top_products,
        missing_value_rows,
        invalid_data_rows,
    )
    with open(filename, "w") as f:
        f.writelines(line + "\n" for line in lines)
