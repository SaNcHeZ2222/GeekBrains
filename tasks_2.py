"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
"""
from collections import defaultdict

dict_digits = defaultdict(list)

for i in input('Введите первое число: '):
    dict_digits['1'].append(i)

for i in input('Введите второе число: '):
    dict_digits['2'].append(i)

print(dict_digits)

print('Сумма:', hex(int(''.join(dict_digits['1']), 16) + int(''.join(dict_digits['2']), 16))[2:].upper())

print('Произведение:', hex(int(''.join(dict_digits['1']), 16) * int(''.join(dict_digits['2']), 16))[2:].upper())
