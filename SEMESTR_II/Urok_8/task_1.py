# Запрашиваем количество элементов в массиве
total_elements = int(input("Введите количество чисел N: "))

# Заполняем список числами, считывая каждое с новой строки
numbers_list = [int(input("Введите целое число: ")) for _ in range(total_elements)]

# Разворачиваем список в обратном порядке
reversed_list = numbers_list[::-1]

# Выводим элементы перевернутого массива, каждый на новой строке
for number in reversed_list:
    print(number)