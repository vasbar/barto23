# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        a = []
        for row in reader:
            json_str = row
            a.append(json_str)
            with open('output.json', 'w') as f:
                json.dump(a, f, indent=4, ensure_ascii=True)

    # TODO считать содержимое csv файла

    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

