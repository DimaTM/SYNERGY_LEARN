import math

def calculate_factorial(number: int) -> int:
    # Находим факториал переданного числа стандартными средствами
    return math.factorial(number)

# Запрашиваем у пользователя начальное натуральное число
user_number = int(input("Введите натуральное число: "))

# Вычисляем факториал введенного числа (например, для 3 получим 6)
initial_factorial = calculate_factorial(user_number)
print(f"Факториал числа {user_number} равен: {initial_factorial}")

# Создаем список факториалов чисел в убывающем порядке от найденного значения до 1
factorials_sequence = [calculate_factorial(i) for i in range(initial_factorial, 0, -1)]

# Выводим результирующий список
print(factorials_sequence)