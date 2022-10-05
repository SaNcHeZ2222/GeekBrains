def sum_n_order(n, elem=1, count=1):
    if n == 1:
        print(count)
        return
    elem = elem / -2
    count += elem
    n -= 1
    return sum_n_order(n, elem, count)


sum_n_order(int(input('Введите длину последовательности: ')))
