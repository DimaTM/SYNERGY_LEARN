import random

def generate_random_matrix(rows: int, cols: int) -> list[list[int]]:
    # Инициализируем пустую структуру для новой матрицы
    matrix = []
    
    # Заполняем строки случайными числами в диапазоне от -100 до 100
    for _ in range(rows):
        row = [random.randint(-100, 100) for _ in range(cols)]
        matrix.append(row)
        
    return matrix

def sum_matrices(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    # Получаем размеры исходных матриц для генерации результирующей сетки
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    # Создаем базовую пустую матрицу под результаты сложения
    result_matrix = []
    
    # Поэлементно складываем значения из двух матриц, находящиеся на одинаковых позициях
    for i in range(rows):
        result_row = []
        for j in range(cols):
            element_sum = matrix_a[i][j] + matrix_b[i][j]
            result_row.append(element_sum)
        result_matrix.append(result_row)
        
    return result_matrix

def print_matrix(matrix: list[list[int]], name: str):
    # Выводим матрицу в консоль в читаемом построчном виде
    print(f"\n--- {name} ---")
    for row in matrix:
        print(row)

# Определяем произвольную размерность матриц для демонстрации универсальности алгоритма
num_rows = 10
num_cols = 10

# Генерируем две независимые матрицы с заданными размерами
matrix_1 = generate_random_matrix(num_rows, num_cols)
matrix_2 = generate_random_matrix(num_rows, num_cols)

# Вычисляем сумму сгенерированных матриц
matrix_3 = sum_matrices(matrix_1, matrix_2)

# Отображаем результаты работы программы
print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")
print_matrix(matrix_3, "Матрица 3 (Результат сложения)")