"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib
import uuid
import json

salt = uuid.uuid4().hex
password = input('Введите свой пароль: ')
hash_object = hashlib.sha256(salt.encode('UTF-8') + password.encode('UTF-8'))
hex_dig = hash_object.hexdigest()

print(hex_dig)


with open('package.json') as file:
    a = json.load(file)
    a[hex_dig] = {salt: password}
    with open('package.json', 'w') as file_1:
        file_1.write(json.dumps(a))

password_1 = input('Введите пароль ещё раз: ')

with open('package.json') as file:
    a = json.load(file)
    hash_object_1 = hashlib.sha256(salt.encode('UTF-8') + password_1.encode('UTF-8'))
    hex_dig_1 = hash_object_1.hexdigest()
    if hex_dig_1 in a.keys() and password_1 == a[hex_dig_1][salt]:
        print('Ваши пароли совподают')
    else:
        print('Ваши пароли не совподают')

