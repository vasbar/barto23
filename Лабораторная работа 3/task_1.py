# TODO Напишите функцию для поиска индекса товара
def idxs(spis, tovar):
    for i in range(len(spis)):
        if tovar == spis[i]:
            return i
        if i == (len(spis) - 1):
            return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = idxs(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
