from memory_profiler import profile


@profile
def func_1(n):
    A = []
    for i in range(n):  # n
        A.append(n * n)  # 1
    return A


@profile
def func_2(n):
    B = [i * i for i in range(n)]
    return B



func_1(10000)


func_2(10000)


# Быстрее работает генератор