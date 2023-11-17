numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = 4
numbers[missing_index] = 0
summa = sum(numbers)
avg = summa/(len(numbers))
numbers[missing_index] = avg
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
