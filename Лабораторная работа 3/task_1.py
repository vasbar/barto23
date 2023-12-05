# TODO Напишите функцию для поиска индекса товара
def idxs(spis, tovar):
    for i, current_tovar in enumerate(spis):
        if tovar == current_tovar:
            return i


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = idxs(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
