import math

class Turtle:
    def __init__(self, start_x: int = 0, start_y: int = 0, speed: int = 1):
        # Устанавливаем стартовые координаты и начальную скорость перемещения
        self.x = start_x
        self.y = start_y
        self.s = speed

    def go_up(self):
        # Сдвигаем позицию вверх по оси ординат
        self.y += self.s

    def go_down(self):
        # Сдвигаем позицию вниз по оси ординат
        self.y -= self.s

    def go_left(self):
        # Сдвигаем позицию влево по оси абсцисс
        self.x -= self.s

    def go_right(self):
        # Сдвигаем позицию вправо по оси абсцисс
        self.x += self.s

    def evolve(self):
        # Увеличиваем шаг перемещения на единицу
        self.s += 1

    def degrade(self):
        # Контролируем, чтобы скорость не опустилась до нуля или отрицательных значений
        if self.s <= 1:
            raise ValueError("Скорость перемещения не может быть меньше или равна нулю")
        self.s -= 1

    def count_moves(self, x2: int, y2: int) -> int:
        # Находим абсолютное расстояние до целевых точек по обеим координатным осям
        delta_x = abs(x2 - self.x)
        delta_y = abs(y2 - self.y)
        
        # Рассчитываем количество полных ходов для преодоления дистанции, округляя в большую сторону
        moves_x = math.ceil(delta_x / self.s)
        moves_y = math.ceil(delta_y / self.s)
        
        # Возвращаем суммарное минимальное количество команд перемещения
        return moves_x + moves_y