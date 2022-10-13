"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib
import itertools

list_hash = []

a = input('Введите слово: ')


for i in range(0, len(a)):
    comb = list(itertools.combinations(a[i:], len(a[i:]) - 1))
    for j in comb:
        word = ''.join(j)
        if word in a and word:
            hash = hashlib.sha256(word.encode('UTF-8')).hexdigest()
            if hash not in list_hash:
                list_hash.append(hash)
                print(word)

print(len(list_hash))