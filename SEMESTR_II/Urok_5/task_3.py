# Запрашиваем минимальную сумму инвестиций и баланс каждого инвестора
min_investment = int(input("Введите минимальную сумму инвестиций (X): "))
michael_money = int(input("Введите сумму Майкла (A): "))
ivan_money = int(input("Введите сумму Ивана (B): "))

# Проверяем возможности инвесторов по отдельности и совместно
can_michael = michael_money >= min_investment
can_ivan = ivan_money >= min_investment

if can_michael and can_ivan:
    print("2")
elif can_michael:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif (michael_money + ivan_money) >= min_investment:
    print("1")
else:
    print("0")