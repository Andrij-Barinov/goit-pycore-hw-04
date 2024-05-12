# ❗ Завдання #2

# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.


# Вимоги до завдання:

# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


# Рекомендації для виконання:

# Використовуйте with для безпечного читання файлу.
# Пам'ятайте про встановлення кодування при відкриті файлів
# Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
# Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
# Опрацьовуйте можливі винятки, пов'язані з читанням файлу.


# Критерії оцінювання:

# Функція має точно обробляти дані та повертати правильний список словників.
# Повинна бути належна обробка винятків і помилок.
# Код має бути чистим, добре структурованим і зрозумілим.


# Приклад використання функції:

# cats_info = get_cats_info("path/to/cats_file.txt")
# print(cats_info)


# Очікуваний результат:

# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]


def get_cats_info(path):
    cats_list = []
    try:
        # Use 'with' to ensure the file is properly closed after reading
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove any leading/trailing whitespace including newline characters
                clean_line = line.strip()
                if clean_line:
                    # Split the line by comma
                    cat_data = clean_line.split(',')
                    # Ensure the line contains exactly three elements
                    if len(cat_data) == 3:
                        cat_dict = {
                            "id": cat_data[0],
                            "name": cat_data[1],
                            "age": cat_data[2]
                        }
                        cats_list.append(cat_dict)
                    else:
                        print(f"Skipping invalid line: {clean_line}")
        return cats_list
    except FileNotFoundError:
        print("The specified file was not found.")
        return []
    except IOError:
        print("An error occurred while reading the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
