"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


def my_shiny_new_decorator(function_to_decorate):
    @profile
    def the_wrapper_around_the_original_function(*args):
        function_to_decorate(args)
    return the_wrapper_around_the_original_function


@my_shiny_new_decorator
def foo(x: list):
    if len(x) == 1:
        return x[0]
    return x[0] + foo(x[1:])


foo([1, 2, 3, 7])

# Это связано с тем, что функция каждый раз вызывает сама себя и каждый
# раз замеряет сама себя, но это можно решить декоратором, который
# сначал сделает всё внутри, а потом замерит память