# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# Примеры:
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# --------
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def nums(count):
    list = sample(range(count * 3), count)
    print(list)
    return [list[count] for count in range(1, len(list)) if list[count] > list[count - 1]]

print(nums(int(input('Введите число: '))))

# # Разбор д/з

# from random import sample


# def more_then(num):
#     my_list = sample(range(num * 3), num)
#     print(my_list)
#     return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]


# print(more_then(int(input())))

# #  ------------------------------------------- вариант решения -------------------------------------------

# from random import randint


# def more_then(num):
#     original_list = [randint(0, 1000) for _ in range(num)]
#     print(original_list)
#     return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


# print(more_then(int(input())))