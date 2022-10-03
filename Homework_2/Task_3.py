# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input())
sum = 0

list_nums=[]

for i in range(1, num+1):
    result = round((1+1/i)**i)
    list_nums.append(result)
    sum+=result

print(list_nums)
print(sum)