def mer_sort(array):
    tmp_list = []

    def sp(array):
        arr_1 = array[:len(array) // 2]
        arr_2 = array[len(array) // 2:]

        if len(arr_1) > 1:
            sp(arr_1)
        else:
            tmp_list.append(arr_1)
        if len(arr_2) > 1:
            sp(arr_2)
        else:
            tmp_list.append(arr_2)

        return tmp_list

    def mer(tmp_list):
        tmp_new = []

        for i in range(int(len(tmp_list) // 2)):
            tmp = []
            tmp1 = tmp_list[i]
            tmp2 = tmp_list[-(i + 1)]
            n1 = 0
            n2 = 0

            while n1 < len(tmp1) and n2 < len(tmp2):
                if tmp1[n1] < tmp2[n2]:
                    tmp.append(tmp1[n1])
                    n1 += 1
                else:
                    tmp.append(tmp2[n2])
                    n2 += 1
            while n1 < len(tmp1):
                tmp.append(tmp1[n1])
                n1 += 1
            while n2 < len(tmp2):
                tmp.append(tmp2[n2])
                n2 += 1
            tmp_new.append(tmp)
        if len(tmp_new) > 1:
            mer(tmp_new)
        else:
            return print(f'Отсортированный массив:\n{tmp_new[0]}')

    sp(array)
    mer(tmp_list)

array = [0, 2, 3, 5, 4, 7, 6, 9, 8, 1]
print(f'Дан массив:\n{array}')
mer_sort(array)