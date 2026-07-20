import collections

# Инициализируем стартовую базу данных питомцев
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_pet(ID: int):
    # Возвращаем данные питомца, если ID существует, иначе возвращаем False
    return pets[ID] if ID in pets else False

def get_suffix(age: int) -> str:
    # Определяем корректное склонение слова "год" на основе числового значения
    if age % 100 in [11, 12, 13, 14]:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

def pets_list():
    # Проверяем базу на наличие записей
    if not pets:
        print("База данных пуста.")
        return
    # Перебираем и выводим краткую сводку по всем существующим ID
    for ID in pets:
        pet_data = pets[ID]
        name = list(pet_data.keys())[0]
        print(f"ID: {ID} | Имя: {name}")

def create():
    # Определяем следующий ID на основе последней записи в словаре
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1
        
    # Запрашиваем данные о новой записи через консоль
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    # Записываем структуру в общий словарь
    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Запись успешно создана под ID: {new_id}")

def read():
    ID = int(input("Введите ID питомца для чтения: "))
    pet_record = get_pet(ID)
    
    # Проверяем существование записи перед ее выводом
    if not pet_record:
        print("Ошибка: Питомца с таким ID не существует.")
        return
        
    # Извлекаем вложенные параметры для формирования строки
    name = list(pet_record.keys())[0]
    details = pet_record[name]
    
    suffix = get_suffix(details["Возраст питомца"])
    print(f'Это {details["Вид питомца"]} по кличке "{name}". '
          f'Возраст питомца: {details["Возраст питомца"]} {suffix}. '
          f'Имя владельца: {details["Имя владельца"]}')

def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet_record = get_pet(ID)
    
    # Проверяем существование записи перед изменением данных
    if not pet_record:
        print("Ошибка: Питомца с таким ID не существует.")
        return
        
    old_name = list(pet_record.keys())[0]
    print(f"Текущие данные питомца {old_name}: {pet_record[old_name]}")
    
    # Запрашиваем обновленные параметры
    new_name = input(f"Введите новое имя (оставьте пустым, чтобы сохранить '{old_name}'): ") or old_name
    new_type = input("Введите новый вид питомца: ")
    new_age = int(input("Введите новый возраст питомца: "))
    new_owner = input("Введите новое имя владельца: ")
    
    # Удаляем старый внутренний ключ, если имя изменилось, и сохраняем новые параметры
    del pets[ID][old_name]
    pets[ID][new_name] = {
        "Вид питомца": new_type,
        "Возраст питомца": new_age,
        "Имя владельца": new_owner
    }
    print("Запись успешно обновлена.")

def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    
    # Удаляем элемент из словаря, если переданный ID присутствует в ключах
    if ID in pets:
        del pets[ID]
        print(f"Запись ID {ID} успешно удалена.")
    else:
        print("Ошибка: Питомца с таким ID не существует.")

# Главный цикл управления базой данных
while True:
    command = input("\nВведите команду (create, read, update, delete, list, stop): ").strip().lower()
    
    if command == 'stop':
        print("Программа завершена.")
        break
    elif command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда. Повторите ввод.")