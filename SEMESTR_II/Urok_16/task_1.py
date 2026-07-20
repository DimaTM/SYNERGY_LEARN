class CashRegister:
    def __init__(self, start_money: float = 0.0):
        # Инициализируем начальный баланс кассы
        self.money = start_money

    def top_up(self, x: float):
        # Увеличиваем текущий баланс на переданную сумму
        self.money += x

    def count_1000(self) -> int:
        # Вычисляем количество полных тысяч в кассе путем целочисленного деления
        return int(self.money // 1000)

    def take_away(self, x: float):
        # Проверяем наличие достаточной суммы перед списанием
        if x > self.money:
            raise ValueError("Недостаточно денег в кассе для выполнения операции")
        # Уменьшаем баланс кассы
        self.money -= x