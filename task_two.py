def first_sort(n: list):
    minimum = 10000000000
    for i in n:
        if i < minimum:
            minimum = i
    return minimum


print(first_sort([1, 2, 3, 5, 112, 10102301, -14, -3]))


def second_sort(n: list):
    for i in range(len(n)):
        f = 0
        for j in range(len(n) - 1):
            first_el = n[j]
            second_el = n[j + 1]
            if second_el < first_el:
                n[j] = second_el
                n[j + 1] = first_el
                f = 1
        if f == 0:
            return n[0]
    return n[0]


print(second_sort([1, -10, 3, -44, 205, -5]))
