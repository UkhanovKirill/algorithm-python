import random

def fi_med(array):

    for i in range(len(array) - 1):

        left = 0
        right = 0
        equal = 0

        for j in range(len(array)):

            if i != j:

                if array[i] > array[j]:
                    left += 1
                elif array[i] < array[j]:
                    right += 1
                elif array[i] == array[j]:
                    equal += 1

        if left == right:
            return array[i]

        else:
            if abs(left - right) - equal == 0:
                return array[i]

SIZE = 7
array = [random.randint(- SIZE, SIZE) for i in range(2 * SIZE - 1)]

print(f'Сгенерированный массив: \n{array}')
print(f'Медианой массива является число: {fi_med(array)}')
