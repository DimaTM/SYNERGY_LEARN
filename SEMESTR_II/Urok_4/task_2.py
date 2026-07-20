# Запрашиваем у пользователя пятизначное целое число
number = int(input("Введите пятизначное целое число: "))

# Извлекаем отдельные цифры числа с помощью деления нацело и остатка от деления
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = number // 10000

# Возводим количество десятков в степень единиц
powered_tens = tens ** units

# Умножаем полученный результат на количество сотен
multiplied_by_hundreds = powered_tens * hundreds

# Вычисляем разность между десятками тысяч и тысячами
diff_thousands = ten_thousands - thousands

# Делим итоговое значение на полученную разность для получения вещественного числа
result = multiplied_by_hundreds / diff_thousands

# Выводим финальный результат
print(result)