def calculator():
    symbol = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if symbol == '0':
        return
    elif symbol not in '+-*/':
        print('Проблема, попробуй ещё раз ввести символ')
        return calculator()
    number_1, number_2 = input('Введите два числа через пробел: ').split()
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
        if symbol == '+':
            print(number_1 + number_2)
            return calculator()
        elif symbol == '*':
            print(number_1 * number_2)
            return calculator()
        elif symbol == '-':
            print(number_1 - number_2)
            return calculator()
        elif symbol == '/':
            if number_2 == 0:
                print('Делить на ноль нельзя')
                return calculator()
            print(number_1 / number_2)
            return calculator()
    except ValueError:
        print('Введите число, а не строку')
        return calculator()


calculator()
