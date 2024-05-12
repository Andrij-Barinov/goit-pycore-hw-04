# ❗ Завдання #3

# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.


# Вимоги до завдання:

# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


# Рекомендації для виконання:

# Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
# Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
# Для роботи з файловою системою використовуйте модуль pathlib.
# Забезпечте належне форматування виводу, використовуючи функції colorama.


# Критерії оцінювання:

# Створення та використання віртуального оточення.
# Правильність отримання та обробки шляху до директорії.
# Точність виведення структури директорії.
# Коректне застосування кольорового виведення за допомогою colorama.
# Якість коду, включаючи читабельність, структурування та коментарі.


# Приклад використання:

# Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.

# python hw03.py /шлях/до/вашої/директорії

# Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням різних кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.

# Для директорії зі наступною структурою

# 📦picture
#  ┣ 📂Logo
#  ┃ ┣ 📜IBM+Logo.png
#  ┃ ┣ 📜ibm.svg
#  ┃ ┗ 📜logo-tm.png
#  ┣ 📜bot-icon.png
#  ┗ 📜mongodb.jpg

# Скрипт повинен вивести схожу структуру


import sys
from pathlib import Path
from colorama import init, Fore

def list_directory(path, prefix=''):
    # Initializing Colorama for color output
    init()

    try:
        # Check if the path exists and is a directory
        if not path.exists() or not path.is_dir():
            print(Fore.RED + f'Error: Path {path} does not exist or is not a directory.' + Fore.RESET)
            return

        entries = list(path.iterdir())
        entries_count = len(entries)
        for index, item in enumerate(entries):
            connector = "┗" if index == entries_count - 1 else "┣"
            
            if item.is_dir():  # If the element is a directory
                print(f'{prefix}{connector} 📂 ' + Fore.BLUE + f'{item.name}/' + Fore.RESET)
                # Recursive call to display the contents of a directory
                extension = "  " if index == entries_count - 1 else "┃ "
                list_directory(item, prefix + extension)
            else:
                print(f'{prefix}{connector} 📜 ' + Fore.GREEN + f'{item.name}' + Fore.RESET)

    except PermissionError:
        print(Fore.RED + f'Error accessing {path}' + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f'Error: {e}' + Fore.RESET)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task_three.py <directory path>" + Fore.RESET)
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    if directory_path.is_dir():
        print(Fore.BLUE + f'📦 {directory_path.name}/' + Fore.RESET)  # Display the name of the root directory in blue
        list_directory(directory_path)
    else:
        print(Fore.RED + f'Error: path {directory_path} is not a directory.' + Fore.RESET)