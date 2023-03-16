import os
global book
book = 'book.txt'


class PhoneBook:
    def __init__(self, path: str = 'book.txt'):
        self.path = path

    def menu(self):
        print("\n1: Показать контакты")
        print("2: Добавить контакт")
        print("3: Изменить контакт")
        print("4: Найти контакт")
        print("5: Удалить контакт")
        print("0: Выход")
    
    # Изменить контакт
    def change_contact(self):
        print("Для выхода в главное меню, введите 0")
        item_menu = input("Выберите фамилию или номер телефона которую требуется изменить: ")
        if item_menu == "0":
            print("Вы вышли в главное меню!")
            return
        else:
            new_item_menu = input("Выберите новую фамилию или номер телефона: ")
            with open (self.path, 'r', encoding='utf-8') as b:
                old_data = b.read()
            new_data = old_data.replace(item_menu, new_item_menu, 1)
            with open (self.path, 'w', encoding='utf-8') as b:
                b.write(new_data)
            print(f"контакт: {item_menu}\nбыл изменен на: {new_item_menu}")
    
    # Удалить контакт
    def deleted(self):
        print("Для выхода в главное меню, введите 0")
        item_menu = input("Выберите фамилию или номер телефона которую желаете удалить: ")
        if item_menu == "0":
            print("Вы вышли в главное меню!")
            return
        else:   
            with open(self.path, encoding='utf-8') as in_file, open("output.txt", "w", encoding='utf-8') as out_file:
                for line in in_file:
                    line = line.split()
                    if line[0] == item_menu:
                        print(f"Контакт [ {' '.join(line)} ] удален")
                    elif line[-1] == item_menu:
                        print(f"Контакт [ {' '.join(line)} ] удален")
                    else:
                        out_file.write(f"{' '.join(line)}\n")
            os.remove('book.txt')
            os.rename("output.txt", 'book.txt')

    # Найти контакт
    def search(self):
        print("Для выхода в главное меню, введите 0")
        item_menu = input("Введите фамилию или номер телефона: ")
        if item_menu == "0":
            print("Вы вышли в главное меню!")
            return
        else:   
            data = open(self.path, 'r', encoding='utf-8')
            for line in data:
                line = line.split()
                if line[0] == item_menu:
                    print(' '.join(line))
                if line[-1] == item_menu:
                    print(' '.join(line))
            data.close()

    # Добавить контакт
    def add_in_book(self):
        print("Для выхода в главное меню, введите 0")
        surname = input("Введи фамилию: ")
        numbers = input("Введи номер: ")
        if surname == "0" or surname == "0" :
            print("Вы вышли в главное меню!")
            return
        else:   
            data = open(self.path, 'a', encoding='utf-8')
            data.write(f'\n{surname}\t|\t')
            data.write(f"{numbers}")
            print("Контакт успешно добавлен")

    # Показать контакты
    def open_book(self):
        data = open(self.path, 'r', encoding='utf-8')
        for line in data:
            print(' '.join(line.split()))
        data.close()

