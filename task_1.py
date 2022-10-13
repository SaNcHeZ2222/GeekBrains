import time

print('a')

A = {}

B = []


def time_get(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(start_time - time.time())
        return res

    return wrapped


@time_get
def func(values: dict):
    for i in range(len(values)):  # n
        A[i + 1] = values[i]  # 1
    return


@time_get
def func_2(values: list):
    for i in range(len(values)):  # n
        B.append(values[i])  # 1
    return


func([1, 12, 15, 78, 20])
func_2([1, 12, 15, 78, 20])

# Значения всегда разные, но в за частую добавление в список просходит медленее

print('b')


@time_get
def list_b(values: list):
    for i in range(len(values)):  # n
        print(values[i], end=' ')  # 1


@time_get
def dict_b(values: dict):
    for key in values.keys():  # n
        print(values[key], end=' ')  # 1


list_b(B)
dict_b(A)

# Значения всегда разные, но в за частую получение из списка просходит медленее

print('c')


@time_get
def list_c(values: list):
    for key in range(len(values) - 1, -1, -1):  # n
        del values[key]  # 1


@time_get
def dict_c(values: dict):
    for key in list(values.keys()):  # n
        del values[key]  # 1


list_c(B)
dict_c(A)

# Значния всегда
