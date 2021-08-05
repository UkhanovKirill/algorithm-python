# Python 3.9 (64-bit)

import sys

x1, y1, x2, y2 = [int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split()]

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')

sum_member = sys.getsizeof(x1) + sys.getsizeof(x2) + sys.getsizeof(y1) + sys.getsizeof(y2) + sys.getsizeof(k) + sys.getsizeof(b)

print(f'В программе задействовано байт памяти: {sum_member}')

# Введите кординаты (x1 y1 x2 y2): 1 1 2 2
# Уравнение прямой: y = 1.0x + 0.0
# В программе задействовано байт памяти: 160