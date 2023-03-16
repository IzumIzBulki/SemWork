import configuration as conf

pb = conf.PhoneBook('book.txt')


def treatment(number):
    if number == 1:
        print("\nВы перешли в меню Показать контакты")
        pb.open_book()
    elif number == 2:
        print("\nВы перешли в меню Добавить контакт")
        pb.add_in_book()
    elif number == 3:
        print("\nВы перешли в Изменить контакт")
        pb.change_contact()
    elif number == 4:
        print("\nВы перешли в Найти контакт")
        pb.search()
    elif number == 5:
        print("\nВы перешли в Удалить контакт")
        pb.deleted()