# Задача 1. Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5
# N = input("Введите число: ")
# print(N)
# N = int(input("Введите число: "))
# print(N)

# N = int(input("Enter num: "))


def S4_HW1(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors


# print(S4_HW1(N))


# Задача 2. В первом списке находится информация об ассортименте мороженного,
# во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»
# list_1 = ["«Сливочное»", "«Бурёнка»", "«Вафелька»", "«Сладкоежка»"]
# list_2 = ["«Сливочное»", "«Бурёнка»", "«Вафелька»"]
# for el in list_1:
#     if el not in list_2:
#         print(f" Закончилось: {el}")
# # print(*set(list_1).difference(set(list_2)))
# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142
def S4_T3():
    p = "1415926535"
    d = int(input("Введите кол-во знаков после запятой: "))

    print(f"Число π = 3", end=",")
    for i in range(len(p)):
        if i <= (d - 1):
            print(f"{p[i]}", end="")


# S4_T3()
import math

print(f"{math.pi:.4}")
