import random
import timeit
import cProfile

r = [random.randint(0, 999) for _ in range(1000)]
print(f'Массив: {r}')


def function_test(r):
    min_index_1 = 0
    min_index_2 = 1
    for i in r:
        if r[min_index_1] > i:
            min_index_2 = min_index_1
            min_index_1 = r.index(i)
        elif r[min_index_2] > i:
            min_index_2 = r.index(i)
    return r[min_index_1], r[min_index_2]


print(f'Два наименьших элемента: {function_test(r)}', '''timeit(function_test(r), setup = 'from main import function_test')''')

'''Второй способ через сортировку списка'''

def function_test_2(r):
    sort_list = []
    sort_list.extend(r)
    sort_list.sort()
    return sort_list[0], sort_list[1]

print(f'Два наименьших элемента (второй способ): {function_test_2(r)}')

'''if __name__ == '__main__':
    cProfile.run('function_test_2(r)')'''


# что-то я не понял как это оформлять