def coup(digit, rest=''):
    if digit == 0:
        print(rest)
        return
    last_elem = str(digit % 10)
    digit = digit // 10
    rest += last_elem
    coup(digit, rest)


coup(int(input('Введите число: ')))

