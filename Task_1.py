# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите цифру от 1 до 7, обозначающую день недели: "))
if day >= 1 and day <= 5:
    print("Этот день рабочий")
elif day > 5 and day <= 7:
    print("Ура, выходной!")
else:
    print("Введено неверное значение")