# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Примеры:
# in
# 54
# out
# [2, 3, 3, 3]
# -------
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# -------
# in
# 650
# out
# [2, 5, 5, 13]

def factorization(n):
    i = 2
    prime_fact = []
    while i * i <= n:
        while n % i == 0:
            prime_fact.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        prime_fact.append(n)
    return prime_fact


number = int(input('Задайте натуральное число:\n'))
print(f"Список простых множителей заданного числа {number}:\n{factorization(number)}")

# # Разбор д/з

# def find_prime_nums(num):
#     pr_fact = []
#     di = 2
#     while num > 1:
#         if num % di == 0:
#             pr_fact.append(di)
#             num //= di
#         else:
#             di += 1
#     return pr_fact


# print(find_prime_nums(int(input())))
