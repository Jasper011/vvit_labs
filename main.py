from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
from utils.validator import validate_numbers
from pathlib import Path
import logging
import json


base_dir = Path(__file__).parent
config_path = base_dir / "config.json"

try:
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
except FileNotFoundError:
    print(f"Конфиг {config_path} не найден.")
    raise SystemExit(1)
except json.JSONDecodeError as error:
    print(f"Ошибка в JSON-конфиге: {error}")
    raise SystemExit(1)

data_path = base_dir / config["input_file"]
log_path = base_dir / config["log_file"]
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')


def main():
    logging.info("Запуск программы")
    print(Path.cwd())

    if (data_path).exists():  
        try:  
            numbers = read_numbers(data_path)
            validate_numbers(numbers)
        except ValueError as error:
            logging.error(f"Validation error: {error}")
            return
    else:
        logging.error(f"Файл {data_path} не найден.")
        return
    logging.info(f"Файл прочитан. Прочитанные числа: {numbers}")
    average = calculate_average(numbers)
    minimum = find_min(numbers)
    maximum = find_max(numbers)
    print(f'Среднее: {average}, минимум: {minimum}, максимум: {maximum}')
    logging.info('Завершение программы')

if __name__ == "__main__":
    main()
