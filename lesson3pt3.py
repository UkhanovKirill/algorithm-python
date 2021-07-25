import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {r}')

max_random = r[0]
min_random = r[0]

for i in r:
    if i > max_random:
        max_random = i
    elif i < min_random:
        min_random = i
min_index = r.index(min_random)
max_index = r.index(max_random)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив после изменения элементов {min_index + 1} и {max_index + 1}: {r}')