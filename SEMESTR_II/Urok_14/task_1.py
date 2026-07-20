def print_list_recursive(target_list: list, index: int = 0) -> None:
    # Базовый случай: если текущий индекс равен длине списка, значит все элементы выведены
    if index == len(target_list):
        print("Конец списка")
        return

    # Выводим текущий элемент списка в консоль
    print(target_list[index])

    # Вызываем функцию повторно для следующего индекса, сдвигая указатель вперед
    print_list_recursive(target_list, index + 1)

# Исходный список элементов для обработки
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Запускаем рекурсивный обход списка с начального нулевого индекса
print_list_recursive(my_list)