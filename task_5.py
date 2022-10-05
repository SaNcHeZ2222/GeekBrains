def go_matrix_ascii(number=32, count=0):
    if number == 128:
        return
    if count % 10 == 0:
        print()
    print(f'{number} - {chr(number)}', end = ' ')
    go_matrix_ascii(number + 1, count + 1)


go_matrix_ascii()
