import dictionary as dict
import add_contact as ac

def menu():
    print("1: Открыть файл")
    print("2: Сохранить файл")
    print("3: Показать контакты")
    print("4: Добавить контакт")
    print("5: Изменить контакт")
    print("6: Найти контакт")
    print("7: Удалить контакт")
    print("8: Создать новый файл")
    print("9: Выход")

def select_menu():
    global item_menu
    item_menu = int(input("Выберите пункт меню: "))
    print(f"Вы выбрали пункт : {item_menu}")
    return item_menu

def treatment(number):
    if number == 1:
        print("Вы перешли в Открыть файл")
    elif number == 2:
        print("Вы перешли в Сохранить файл")
    elif number == 3:
        dict.list()
    elif number == 4:
        ac.add(dict.list())
    elif number == 5:
        print("Вы перешли в Изменить контакт")
    elif number == 6:
        print("Вы перешли в Найти контакт")
    elif number == 7:
        print("Вы перешли в Удалить контакт")
    elif number == 8:
        print("Вы перешли в Создать новый файл")
    else:
        print("Вы перешли в Выход")