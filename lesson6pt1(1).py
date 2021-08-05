# Python 3.9 (64-bit)

import sys

a = input('Введите трехзначное число: ')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)

print(f'В программе задействовано байт памяти: {sum_member}')

# Введите трехзначное число: 123
# В программе задействовано байт памяти: 192