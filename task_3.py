"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


print(timeit('revers', '123', globals=globals()))
# 0.022437333000000004


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(timeit('revers_2', '123', globals=globals()))
# 0.019926583000000005


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(timeit('revers_3', '123', globals=globals()))
# 0.019421959000000003


def revers_4(enter_num):
    revers_s = ''
    for i in range(1, len(str(enter_num)) + 1):
        revers_s += (str(enter_num)[- i])
    return int(revers_s)


print(timeit('revers_4', '123', globals=globals()))
# 0.018141041999999996
