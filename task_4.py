"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict

from timeit import timeit

dict_default = {}

dict_order = OrderedDict()

A = [12, 13, 14, 15, 16]


def one():
    for i in range(len(A) - 1, 0, -1):
        dict_default[i] = A[i]


def two():
    for i in range(len(A) - 1, 0, -1):
        dict_order[i] = A[i]


def three():
    for i in range(1, 3):
        del dict_default[i]


def four():
    for i in range(1, 3):
        del dict_order[i]


one()
print(timeit('one', globals=globals()))

two()
print(timeit('two', globals=globals()))
print()

# Быстрее заполняется OrderDict

three()
print(timeit('three', globals=globals()))

four()
print(timeit('four', globals=globals()))

# Быстрее удаляется OrderDict

print(dict_default)

print(dict_order)