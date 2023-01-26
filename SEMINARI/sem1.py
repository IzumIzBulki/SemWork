# print("hello world")
#
# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# c = 30
# print(a, ' + ', b, ' = ', c)
# print('{2} + {0} = {1}'.format(a, b, c))
# print(f"{a}, 1{b}")
#
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# # 100 80 60 40 20
# for i in range(5):
#  print(i)
# # 0 1 2 3 4
#
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
#
#
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к           print(text[len(text)]) -> error
# print(text[-5]) # б
# print(text[:]) # print(text)   весь текст
# print(text[:2]) # съ     от 0 до 2 символов
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё    от 2 до 9 символа
# print(text[6:-18]) # ещё этих мягких    от 6 до -18 символа
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
#
# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
#
#
# def f(x):
#  return x**2
# def f(x):
#  if x == 1:
#     return 'Целое'
#  elif x == 2.3:
#     return 23
#  else:
#     return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f()))


# _______________________________________________________________________________________________

# За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.


# n = 700   # за день
# m = 750   # сколько дней проехать

# print(f'количество дней = {round(m/n)}')
# print(f'количество часов = {round((m/n*100/24)%10)}')


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
#
# 2016
#
# YES

# print('Введите год')
# god = int(input())
# if god % 4 == 0 or god % 400 == 0:
#     print('YES')
# else:
#     print('NO')

#
# 2.
# Напишите программу, которая будет принимать
# на вход дробь и показывать
# первую цифру дробной части числа.
#
# - 6, 78 -> 7
# - 5 -> нет
# - 0, 34 -> 3

# number = float(input("Число:"))
# if number % 1 == 0: #(digital == 0):
#     print("no")
# else:
#     digital = int(number * 10 % 10)
#     print(digital)
# cbcvb

y = 2**2-4
if y == False:
    print('Hallo')
else:
    print(y)

