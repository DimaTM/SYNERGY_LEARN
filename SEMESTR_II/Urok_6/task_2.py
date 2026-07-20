# Запрашиваем натуральное число X (до 2 миллиардов)
target_number = int(input("Введите натуральное число X: "))

# Счетчик количества натуральных делителей
divisors_count = 0

# Перебираем потенциальные делители от 1 до квадратного корня из X для оптимизации скорости
current_divisor = 1
while current_divisor * current_divisor <= target_number:
    # Проверяем, делится ли X на текущее число без остатка
    if target_number % current_divisor == 0:
        # Увеличиваем счетчик для найденного делителя
        divisors_count += 1
        
        # Проверяем, является ли парный делитель отличным от текущего
        if current_divisor * current_divisor != target_number:
            divisors_count += 1
            
    current_divisor += 1

# Выводим общее количество найденных делителей
print(divisors_count)