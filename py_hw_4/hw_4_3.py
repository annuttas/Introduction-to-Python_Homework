# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# Примеры:
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# -------
# in
# -1
# out
# Negative value of the number of numbers!
# []
# -------
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randrange

def create_list(count, range_from, range_to):
    if count >= 0 and 0 <= range_from < range_to:
        new_list = []
        for i in range(count):
            new_list.append(randrange(range_from, range_to + 1))
        return new_list
    else:
        print("Заданы неверные параметры")

def uniq_num(list_in):
    new_list = []
    for i in range(len(list_in)):
        print(f"{list_in[i]} - {list_in.count(list_in[i])}")
        if list_in.count(list_in[i]) == 1:
            new_list.append(list_in[i])

    return new_list

num_list = create_list(int(input("Задайте количество элементов в последовательности чисел:\n")), int(input("Задайте начало диапазона случайных чисел для элементов в списке:\n")), int(input("Задайте конец диапазона случайных чисел для элементов в списке:\n")))
print(f"Созданный список:\n{num_list}")
print(f"Список неповторяющихся элементов исходной последовательности в том же порядке:\n{uniq_num(num_list)}")

# # Разбор д/з

# from random import randrange


# def list_rand_nums(count: int):
#     if count < 0:
#         pritn("Negative value of the number of numbers!")
#         return []

#     list_nums = []
#     for i in range(count):
#         list_nums.append(randrange(count))

#     return list_nums


# def uniq_el(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums, 0)

#     for i in list_nums:
#         my_dict[i] += 1

#     for k in my_dict:
#         if my_dict[k] == 1:
#             result.append(k)

#     return result


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(uniq_el(all_list))
