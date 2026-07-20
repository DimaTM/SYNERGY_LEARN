class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создаем дочерний класс, который полностью наследует структуру родителя
class Autobus(Transport):
    pass

# Создаем экземпляр дочернего класса с параметрами из примера
bus_instance = Autobus("Renaul Logan", 180, 12)

# Выводим строковую информацию о характеристиках созданного объекта
print(f"Название автомобиля: {bus_instance.name} Скорость: {bus_instance.max_speed} Пробег: {bus_instance.mileage}")