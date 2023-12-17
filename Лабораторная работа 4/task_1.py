# TODO решите задачу
import json
FILENAME = "input.json"


def task() -> float:
    summa = 0
    with open(FILENAME) as f:
        json_data = json.load(f)
    summa1 = [x for x in json_data]
    for i in range(len(summa1)):
        val = summa1[i]["score"] * summa1[i]["weight"]
        summa += val
    return round(summa, 3)


print(task())
