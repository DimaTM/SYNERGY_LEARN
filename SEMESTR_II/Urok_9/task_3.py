# Считываем последовательность чисел, переданную в одну строку через пробел
numbers_sequence = list(map(int, input("Введите последовательность чисел: ").split()))

# Создаем пустое множество для отслеживания ранее встреченных чисел
history_set = set()

# Перебираем числа из последовательности по порядку
for current_number in numbers_sequence:
    # Если число уже находится в множестве истории, выводим YES
    if current_number in history_set:
        print("YES")
    # Иначе добавляем текущее число в историю и выводим NO
    else:
        print("NO")
        history_set.add(current_number)