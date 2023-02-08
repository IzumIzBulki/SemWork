# def sum(*args):  # * можно вводить переменные без ограничения
#     res = ""
#     for i in args:
#         res += i
#     return res
# print(sum("q","w","e"))

# from modul import max1
# print(max1(5, 9))
#
# from modul import *    # импорт всех функций в файле(папке) modul
# print(max1(5, 9))
#
# import modul as m1   # импорт всех функций в файле(папке) modul
# print(m1.max1(5, 9))

# from modul import fibonachi as fib
# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)
#
# from modul import quic_sort as sort
# print(sort([9, 3, 3, 11, 4, 5, 6, 7, 8, 9]))

from modul import merge_sort as sort
list = [9, 3, 3, 11, 4, 5, 6, 7, 8, 9]
sort(list)
print(list)
