# TODO Напишите функцию find_common_participants
def find_common_participants(spis1, spis2, delimeter=","):
    spis1 = set(spis1.split(delimeter))
    spis2 = set(spis2.split(delimeter))
    res = spis1.intersection(spis2)
    res = list(res)
    res.sort()
    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group,participants_second_group,"|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
