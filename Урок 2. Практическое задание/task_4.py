"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
num = int(input("Введите  целое число"))
count = 0
num_1 = 1
res = 1
num_2 = 0
def rec():
    global count
    count += 1
    if count < num:
        global num_1
        global res
        global num_2
        num_2 = num_1 * (-0.5)
        res = res + num_2
        num_1 = num_2
        num_2 = num_2 * (-0.5)
        return rec()
    else:
        print(res)

rec()
