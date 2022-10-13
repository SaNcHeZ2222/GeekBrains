"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import uuid

dict_url_hash = {}


def add_url_hash(url):
    global dict_url_hash
    if url not in dict_url_hash.keys():
        salt = uuid.uuid4().hex
        hash_object = hashlib.sha256(salt.encode('UTF-8') + url.encode('UTF-8'))
        hex_dig = hash_object.hexdigest()
        dict_url_hash[url] = hex_dig
        return 'Добавлено', hex_dig
    else:
        return dict_url_hash[url]


print(add_url_hash('https://ya.ru'))
print(add_url_hash('https://ya.ru'))
print(add_url_hash('https://google.com'))
print(add_url_hash('https://ya.ru'))
print(add_url_hash('https://google.com'))
