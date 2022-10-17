"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

list_1 = []

deq = deque()


def append_list(*args):
    for i in args:
        list_1.append(i)


def append_left_deq(*args):
    for i in args:
        deq.appendleft(i)


def pop_list():
    pop = list_1.pop()


def popleft_deq():
    pop = deq.popleft()


def extend_list(lst: list):
    list_1.extend(lst)


def extend_left_deque(lst: list):
    deq.extendleft(lst)


def get_item_list(numbers: list):
    for i in numbers:
        a = list_1[i]


def get_item_deque(numbers: list):
    for i in numbers:
        a = deque[i]


append_list(1, 2, 3, 4, 5, 6)

print(timeit('append_list(n)', setup='n = (1, 2, 3, 4, 5, 6)', globals=globals()))

append_left_deq(1, 2, 3, 4, 5, 6)

print(timeit('append_left_deq(n)', setup='n = (1, 2, 3, 4, 5, 6)', globals=globals()))
print()
# Добавлнение происходит быстрее в списке

print(timeit('pop_list', globals=globals()))

print(timeit('popleft_deq', globals=globals()))
print()
# Взятие последнего элемента происходит быстрее в deque

print(timeit('extend_list(n)', setup='n = (7, 8, 9, 10)', globals=globals()))

print(timeit('extend_left_deque(n)', setup='n = (7, 8, 9, 10)', globals=globals()))
print()

# Объединение происходит быстрее в списке

print(timeit('get_item_list(n)', setup='n = (9, 6, 3, 1)', globals=globals()))

print(timeit('get_item_deque(n)', setup='n = (9, 6, 3, 1)', globals=globals()))

# Получение элементов из списка происходит быстрее
