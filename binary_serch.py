def binary_search(list, item): # функция бинарного поиска
    low = 0 # начало массива
    hight = len(list) - 1  # конец массива

    while low <= hight: # пока hight не станет = 1
        mid = (low + hight) // 2 # проверяем средний элемент части массива
        guess = list[mid] # найденный элемент массива
        if guess == item: # сравниваем элементы
            return mid # выводим индекс верного элемента
        if guess > item: # перебор в меньшую половину
            hight = mid - 1
        else: # перебор в большую половину
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 8]

print(binary_search(my_list, 6))

