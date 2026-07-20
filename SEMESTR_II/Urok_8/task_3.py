# Запрашиваем максимальную грузоподъемность одной лодки и количество рыбаков
max_weight = int(input("Введите грузоподъемность лодки M: "))
total_fishermen = int(input("Введите количество рыбаков N: "))

# Считываем вес каждого рыбака из последующих строк
weights = [int(input("Введите вес рыбака: ")) for _ in range(total_fishermen)]

# Сортируем веса рыбаков по возрастанию для применения жадного алгоритма
weights.sort()

# Инициализируем указатели на самого легкого и самого тяжелого рыбаков
light_index = 0
heavy_index = total_fishermen - 1

# Переменная для подсчета необходимых лодок
boats_count = 0

# Распределяем рыбаков по лодкам, пока все не будут переправлены
while light_index <= heavy_index:
    # Если остался один рыбак, выделяем ему отдельную лодку
    if light_index == heavy_index:
        boats_count += 1
        break
    
    # Если самый тяжелый и самый легкий помещаются вместе, сажаем обоих
    if weights[light_index] + weights[heavy_index] <= max_weight:
        light_index += 1
        heavy_index -= 1
    # Иначе самый тяжелый рыбак плывет в лодке один
    else:
        heavy_index -= 1
        
    boats_count += 1

# Выводим минимальное количество лодок
print(boats_count)