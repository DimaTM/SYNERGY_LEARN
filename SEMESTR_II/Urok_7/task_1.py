# Запрашиваем у пользователя строку без пробелов
input_string = input("Введите строку: ")

# Сравниваем строку с её перевернутой копией
if input_string == input_string[::-1]:
    print("yes")
else:
    print("no")