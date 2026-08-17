import os
import subprocess
import sys

import inquirer

from src.calculations import (
    generate_report_data,
)
from src.report import print_report, save_report_to_file


def clear_screen():
    subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True, check=False)
    subprocess.run(["cls"] if os.name == "nt" else ["clear"], shell=True, check=False)


def choose_csv_file(folder="./data"):
    try:
        all_files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder: {folder} not found. Creating it now.")
        os.makedirs(folder)
        input("\nPress Enter to return to menu ")
        return None

    csv_files = [f for f in all_files if f.endswith(".csv")]

    if not csv_files:
        print(f"No csv file found in {folder}")
        input("\nPress Enter to return to menu ")
        return None

    questions = [
        inquirer.List(
            "csv_file",
            message="Choose file to load",
            choices=csv_files,
        ),
    ]

    return folder + "/" + inquirer.prompt(questions)["csv_file"]


def main_menu(loaded_csv_file=None):
    clear_screen()

    questions = [
        inquirer.List(
            "menu_option",
            message="Menu",
            choices=[
                ("Load csv file", 1),
                ("Generate text report", 2),
                ("Export report to text file", 3),
                ("Exit", 4),
            ],
        ),
    ]

    user_answer = inquirer.prompt(questions)

    match user_answer["menu_option"]:
        case 1:
            clear_screen()

            loaded_csv_file = choose_csv_file()
        case 2:
            clear_screen()

            if loaded_csv_file is None:
                print("Please load a csv file first.")
            else:
                overall, by_category, by_salesperson, top_products = (
                    generate_report_data(loaded_csv_file)
                )
                print_report(overall, by_category, by_salesperson, top_products)

            input("\nPress Enter to return to menu ")
        case 3:
            clear_screen()

            if loaded_csv_file is None:
                print("Please load a csv file first.")
            else:
                overall, by_category, by_salesperson, top_products = (
                    generate_report_data(loaded_csv_file)
                )
                save_report_to_file(
                    overall,
                    by_category,
                    by_salesperson,
                    top_products,
                    "./reports",
                )
                print("Report saved successfully")
            input("\nPress Enter to return to menu ")
        case 4:
            sys.exit()

    return loaded_csv_file
