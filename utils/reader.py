import logging


def read_numbers(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            numbers = []
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid number format: {line.strip()}")
                    logging.warning(f"Invalid number format: {line.strip()}")
        return numbers
    except FileNotFoundError:
        print("File not found.")
        logging.error(f"Файл {file_path} не найден.")
        return []  