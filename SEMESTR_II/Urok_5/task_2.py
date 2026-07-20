# Запрашиваем у пользователя слово
word = input("Введите слово из маленьких латинских букв: ")

# Задаем эталонный набор гласных букв
vowels_list = ['a', 'e', 'i', 'o', 'u']

# Подсчитываем общее количество гласных и согласных в слове
total_vowels = sum(word.count(vowel) for vowel in vowels_list)
total_consonants = len(word) - total_vowels

print(f"Общее количество гласных букв: {total_vowels}")
print(f"Общее количество согласных букв: {total_consonants}")

# Проверяем вхождение каждой гласной и выводим её количество либо False
for vowel in vowels_list:
    count = word.count(vowel)
    if count > 0:
        print(f"Буква '{vowel}': {count}")
    else:
        print(f"Буква '{vowel}': False")