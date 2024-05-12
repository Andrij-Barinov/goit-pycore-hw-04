# ❗ Завдання #1

# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.


# Вимоги до завдання:

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


# Рекомендації для виконання:

# Використовуйте менеджер контексту with для читання файлів.
# Пам'ятайте про встановлення кодування при відкриті файлів
# Для розділення даних у кожному рядку можна застосувати метод split(',').
# Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
# Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.


# Критерії оцінювання:

# Функція повинна точно обчислювати загальну та середню суми.
# Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
# Код має бути чистим, добре структурованим і зрозумілим.


# Приклад використання функції:

# total, average = total_salary("path/to/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Очікуваний результат:

# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000


def total_salary(path):
    try:
        # Opening a file and initializing variables
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0
            
            # Processing each line in the file
            for line in file:
                if line.strip():  # Checking if a string is not empty
                    name, salary = line.strip().split(',')
                    total += int(salary)  # Adding salary to the total amount
                    count += 1  # Increasing the developer counter
            
            # Calculating the average salary
            if count > 0:
                average = total // count
            else:
                average = 0

        return total, average
    except FileNotFoundError:
        print("The file was not found. Please check the path to the file.")
    except Exception as e:
        print(f"An error occurred while processing a file: {e}")

# Example of use
total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary amount: {total}, Average salary: {average}")