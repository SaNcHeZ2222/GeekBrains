import random


def random_digit(digit, count=0):
    if count > 10:
        return
    attempt = int(input('Попробуйте угадать: '))
    if digit == attempt:
        print('Поздравляю, вы победили')
        return
    if attempt > digit:
        print('Ваше число больше')
        return random_digit(digit, count + 1)
    else:
        print('Ваше число меньше')
        return random_digit(digit, count + 1)


random_digit(random.randint(0, 100))
