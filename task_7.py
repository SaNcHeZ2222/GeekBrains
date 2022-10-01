def palindrom(word):
    wordik = ''.join(word.split())
    if wordik == wordik[::-1]:
        print(word, '- Это слово палиндром')
    else:
        print(word, '- Это слово не палиндром')

# В момент выполнения задания не могу получить доступ к видеоуроку, извините, написал с нуля


palindrom('молоко делили ледоколом')
palindrom('молоко делили ледоколомами')
palindrom('топот')


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

# палиндром


def pal_checker(string):
    dc_obj = DequeClass()

    for el in ''.join(string.split()): # Доработал в этой строке ''.join(string.split())
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
