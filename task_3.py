from random import randint


# Пример 1
comp = {str(i): randint(1, 1000) for i in range(1, 6)}

print('Пример 1')
print(comp)

price = [i for i in comp.values()]

for i in range(len(price)): # n
    for j in range(len(price) - 1): # n
        first_el = price[j] # 1
        second_el = price[j + 1] # 1
        if second_el < first_el: # 1
            price[j] = second_el # 1
            price[j + 1] = first_el # 1


def max_3():
    for i, j in enumerate(price[2:]): # n
        for key, value in comp.items(): # n
            if j == value: # 1
                print(key, end=' ')


max_3()
print()
# Общая сложность n**2

# Пример 2

comp = {str(i): randint(1, 1000) for i in range(1, 6)}

print("Пример 2")


print(comp)


def sorting(nums, low, high):
    sr = nums[(low + high) // 2] # 1
    i = low - 1 # 1
    j = high + 1 # 1
    while True:
        i += 1
        while nums[i] < sr:
            i += 1
        j -= 1
        while nums[j] > sr:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def quick_sort_help(items, low, high):
        if low < high:
            split_index = sorting(items, low, high)
            quick_sort_help(items, low, split_index)
            quick_sort_help(items, split_index + 1, high)
    quick_sort_help(nums, 0, len(nums) - 1)

#     Общая сложность n log n

comp_value = list(comp.values())
quick_sort(comp_value)
print({list(comp.values()).index(i) + 1: i for i in comp_value[2:]})
