def sum_order(n, count=0, obr_count=0):
    if n == 0:
        print(f'Пожалуйста, {count} ')
        return
    count += n
    n -= 1
    obr_count += 1
    sum_order(n, count, obr_count)


sum_order(5)
