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
            #print(row)
            json_str = row
            a.append(json_str)
            #json_data = json.dumps(json_str, indent=4, ensure_ascii=True)
            with open('output.json', 'w') as f:
                #f.write(json_str + '\n')
                json.dump(a, f, indent=4, ensure_ascii=True)

    # TODO считать содержимое csv файла
    #for i in range(len(reader)):

     #   with open('output.json', 'w') as f:
      #      f.write(json_str + '\n')
    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

'''
json_data = json.dumps(data, indent=4, ensure_ascii=False)  # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE
    with open(OUTPUT_FILE,'w') as file2:
        json.dump(data, file2, indent=4, ensure_ascii=False)


with open(filename) as file:
    reader = csv.reader(file)
    # Чтение данных
    for row in reader:
        print(row)

# Открытие файла для получения чтения словарей из сsv строк
with open(filename, 'r') as file:
    reader = csv.DictReader(file)

    # Чтение данных
    for row in reader:
        print(row['First Name'], row['Last Name'], row['Age'])

json_str = '{"name": "John", "age": 25, "city": "New York"}'  # Так будет выглядеть словарь json_data в виде JSON строки
# Сериализация данных в формате JSON
with open('output.json', 'w') as f:
    f.write(json_str + '\n')
'''