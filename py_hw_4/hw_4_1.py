# 1. Вычислить число c заданной точностью d
# Примеры:
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# -------
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

print(Decimal(input("Введите число:\n")).quantize(Decimal(input("Задайте точность:\n"))))

# # Разбор д/з
# # 1 вариант

# from decimal import Decimal # модуль decimal одноиммённый класс Decimal в котором мы можем применить quantize

# def accuracy(num, acc):
#     number = Decimal(f"{num}")
#     return number.quantize(Decimal(f"{acc}"))


# print(accuracy(float(input("Enter a real number")), float(input("Enter a required accuracy 0.0001: "))))

# # 2 вариант

# num = float(input('Enter a real number: '))
# -, accu = input("Enter a required accuracy '0.0001': ").split(".")
# print(f"{num:.{len(accu)}f}")