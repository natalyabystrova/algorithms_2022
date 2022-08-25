"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

profit = {'audi': 123456789, 'kia': 12345, 'volvo': 123456, 'VAZ': 1234, 'bmw': 1234567}

# # решение 1:
# def func(arr): # O(nlogn)
#     res = sorted(profit, key=profit.get)[-3:] # O(n) = O(nlogn) + O(n) = O(nlogn)
#     return res #O(1)
# func(profit)

# решение 2:
def func_2(arr): #O(1) + 3 x O(n) + O(1) + O(n) + 0(1) = 3O(n) = O(n)
    lst = [] #O(1)
    for i in range(3): #3
        maxm = max(arr, key=profit.get) #O(n)
        lst.append(maxm) #O(1)
        profit.pop(max(profit, key=profit.get)) #O(n) + O(1) = O(n)
    return lst #O(1)
# func_2(profit)

'''Второе решение эффективнее, т. к. имеет сложность О(n),  а первое - O(nlogn)'''
