def count_chet(digit, chet=0, nechet=0):
    if digit == 0:
        print(f'Количество четных и нечетных цифр в числе равно: ({chet}, {nechet})')
        return
    last_elem = digit % 10
    digit = digit // 10
    if last_elem % 2 == 0:
        count_chet(digit, chet + 1, nechet)
    else:
        count_chet(digit, chet, nechet + 1)


digit = int(input('Введите число: '))
count_chet(digit)
