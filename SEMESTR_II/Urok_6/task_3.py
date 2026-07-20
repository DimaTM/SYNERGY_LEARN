# Запрашиваем границы отрезка A и B (где A <= B)
start_range = int(input("Введите число A: "))
end_range = int(input("Введите число B: "))

# Список для хранения найденных четных чисел
even_numbers = []

# Перебираем все целые числа на заданном отрезке включительно
for current_number in range(start_range, end_range + 1):
    # Если число делится на 2 без остатка, добавляем его в список
    if current_number % 2 == 0:
        even_numbers.append(str(current_number))

# Выводим все собранные четные числа через пробел
print(" ".join(even_numbers))