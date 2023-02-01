# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# number = int(input(f'Введите число: '))
# i = 1
# fact = 1
# fact2 = 1
# while i <= number:
#     fact *= i
#     i += 1
# print(fact)
#
#
# for i in range(1, number+1):
#     fact2 *= i
# print(fact2)


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.




# fibonachi = int(input("Введите число: "))
#
# number_1 = 0
# number_2 = 1
# number_3 = 0
# i = 0
#
# while i < fibonachi:
#     number_3 = number_1 + number_2
#     number_1 = number_2
#     number_2 = number_3
#     i += 1
#     print(number_3)
#     if number_3 == fibonachi:
#         print("нашли")
#         print(i+2)
#         break
# else:
#     print("не нашли")


# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.



from random import randint

watermelons = int(input("Введите количество арбузов: "))
i = 0
min_watermelon = 30000
max_watermelon = 0
heft_watermelon = 0
while i < watermelons:
    heft_watermelon = int(input("Введите вес арбуза: "))   # heft_watermelon = randint(1, 30000)
    i += 1
    if heft_watermelon > max_watermelon:
        max_watermelon = heft_watermelon
    if heft_watermelon < min_watermelon:
        min_watermelon = heft_watermelon
print(f'максимальный вес арбуза: {max} кг, '
      f'минимальный вес арбуза: {min} кг')
