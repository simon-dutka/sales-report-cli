from src.interface import main_menu


def main():
    loaded_csv_file = None

    while True:
        loaded_csv_file = main_menu(loaded_csv_file)


if __name__ == "__main__":
    main()
