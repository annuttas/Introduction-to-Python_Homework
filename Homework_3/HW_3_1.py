# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# -------
# in
# 4
# out
# [4, 2, 4, 9]
# 8

import random

rand_list = []
n = int(input("Задайте количество чисел в списке: "))
for i in range(n):
    rand_list.append(random.randint(0, 101))
print('Список:', rand_list)


def sum_index(rand_list):
    s = 0
    for i in range(len(rand_list)):
        if i % 2 != 0:
            s += rand_list[i]
    print(f"Сумма чисел, cтоящих в списке на нечетных позициях: {s}.")


sum_index(rand_list)