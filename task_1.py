from collections import defaultdict

count_comp = int(input('Введите количество компаний: '))

dict_a = defaultdict(list)

al_prib = 0

for i in range(count_comp):
    name = input('Введите название предприятия: ')
    prices = input('Через пробел введите прибыль за каждый квартал (всего 4): ').split()
    for price in prices:
        dict_a[name].append(int(price))
        al_prib += int(price)

sr_year = al_prib / 2

print(dict_a)

print(sr_year)
for i in dict_a:
    if sr_year < sum(dict_a[i]):
        print(f'Компания {i} выше среднего')
    else:
        print(f'Компания {i} ниже среднего')


# Введите количество компаний: 2
# Введите название предприятия: Рога
# Через пробел введите прибыль за каждый квартал (всего 4): 235 345634 55 235
# Введите название предприятия: Копыта
# Через пробел введите прибыль за каждый квартал (всего 4): 345 34 543 34
# defaultdict(<class 'list'>, {'Рога': [235, 345634, 55, 235], 'Копыта': [345, 34, 543, 34]})
# 173557.5
# Компания Рога выше среднего
# Компания Копыта ниже среднего
