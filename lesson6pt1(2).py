# Python 3.9 (64-bit)

import sys
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

sum_member = sys.getsizeof(max_random) + sys.getsizeof(min_random) + sys.getsizeof(r) + sys.getsizeof(min_index) + sys.getsizeof(max_index)

print(f'В программе задействовано байт памяти: {sum_member}')

# Массив до изменения: [57, 1, 78, 92, 46, 80, 51, 97, 38, 77]
# Массив после изменения элементов 2 и 8: [57, 97, 78, 92, 46, 80, 51, 1, 38, 77]
# В программе задействовано байт памяти: 296