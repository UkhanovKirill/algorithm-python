from functools import reduce

num_1 = 'A2'
num_2 = 'C4F'

num_1, num_2 = list(num_1), list(num_2)
print(num_1)
print(num_2)

lst_convert_hex_int = [int(''.join(i), 16) for i in [num_1, num_2]]
sum_ = sum(lst_convert_hex_int)
mult = reduce(lambda x, y:  x * y, lst_convert_hex_int)

hex_sum = list(hex(sum_).upper()[2:])
hex_mult = list(hex(mult).upper()[2:])

print(hex_sum)
print(hex_mult)