class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

# Создаем дочерний класс с переопределением логики родительского метода
class Autobus(Transport):
    # Переопределяем метод, задавая параметру вместимости значение по умолчанию
    def seating_capacity(self, capacity=50):
        # Вызываем базовую реализацию родительского метода с установленным значением
        return super().seating_capacity(capacity)

# Создаем объект автобуса
bus_instance = Autobus("Renaul Logan", 180, 12)

# Вызываем переопределенный метод без передачи аргумента, чтобы сработало значение 50
print(bus_instance.seating_capacity())