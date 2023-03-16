import configuration as conf
import controller as cont


pb = conf.PhoneBook('book.txt')


def start():
    pb.menu()
    item_menu = int(input("\nВыберите пункт меню: "))
    while item_menu != 0:
        cont.treatment(item_menu)
        pb.menu()
        item_menu = int(input("\nВыберите пункт меню: "))
    print("\nВы вышли из программы")