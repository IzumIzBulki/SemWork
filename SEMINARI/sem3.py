# my_list = [1,2,3,4,4,4,4,5,6,7,8,7,54,4,3,3]
# print(set(my_list)) # set сортирует список и отбирает не повторяющиеся элементы

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на
# K элементов вправо, K – положительное число.

# list_1 = [5, 4, 6, 7, 8, -10]
# k = int(input())
# k = k % len(list_1)
# list_result = list()
# for i in range(k):
#     list_result.append(list_1[len(list_1) - 1 - i])
# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)

# list = [1, 2, 3, 4, 5]
# number = int(input('Введите число, на которое сдвинем массив: '))
# i = 0
# while i < number:
#     list.insert(0, list[len(list)-1])
#     list.pop(len(list)-1)
#     i += 1
# print(list)
#
# list = []
# for i in range(15):
#     list.append(i)
# print(list)
# number = int(input('Введите число, на которое сдвинем массив: '))
#
# newest_list = list[-number:]
# newest_list.extend(list[:-number])
# print(newest_list)
#
# Напишите программу для печати всех уникальных значений в словаре.




# my_dict = {"key1": "123", "key2": "321", "key3": "4213"}
# print(my_dict["key1"])

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
my_set = set()

for item in list_1: #пробежали по словарям
    for key in item: #пробежали по ключам
        my_set.add(item[key].strip())  #отобрали значения не повторяющиеся     #strip удаляет пробелы

print(list_1)
print(my_set)

