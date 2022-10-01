print("Пример 1")


def check_password(password):
    if len(password) < 6: # 1
        return 0
    else:
        return 1


users = {}

while True:
    login, password = input('Введите логин и пароль через пробел: ').split() # 1
    if login in users.keys(): # 1
        print('Увы, этот логин уже занят')
    else:
        break

while True:
    if check_password(password) == 0: # 1
        password = input('Ваш пароль слишком простой, введите новый: ') # 1
    else:
        print('Отлично, вы успешно зарегистрировались')
        users[login + '_+'] = password # _+ отметка об активации # 1
        print(users)
        break

# 1 общая сложность решения

print('Пример 2')


def check_password(password):
    for i in password: # n
        if ord(i) < 65: # Начиная с заглавных английских 1
            return 0
    return 1

users = {}

while True:
    login, password = input('Введите логин и пароль через пробел: ').split() # 1
    if login in users.keys(): # 1
        print('Увы, этот логин уже занят')
    else:
        break

while True:
    if check_password(password) == 0: # 1
        password = input('Ваш пароль слишком простой, введите новый: ') # 1
    else:
        print('Отлично, вы успешно зарегистрировались')
        users[login + '_+'] = password # _+ отметка об активации # 1
        print(users)
        break

# n общая сложность решения
