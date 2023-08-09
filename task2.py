# Задача 32: Определить индексы
# элементов массива (списка),
# значения которых принадлежат
# заданному диапазону
# (т.е. не меньше заданного минимума
#  и не больше заданного максимума)

import random

# Functions


def random_num(left_limit=0, right_limit=10):
    return random.randint(left_limit, right_limit)


def random_fill_num_arr(down_limit=0, up_limit=5, num_of_elem=10):
    temp_array = []
    for n in range(num_of_elem):
        temp_array.append(random_num(down_limit, up_limit))
    return temp_array


def seek_ind_nums_in_diapason(down_diap_limit=0, up_diap_limit=5, array=[3, 10]):
    indexes_arr = []
    for n in range(len(array)):
        if array[n] > down_diap_limit and array[n] < up_diap_limit:
            indexes_arr.append(n)
    return indexes_arr


# Solution

seek_diapason = [3, 14]
random_arr_diapason = [-20, 20]
arr_num_of_elem = 10

print(
    "Исходный массив: ",
    random_arr := random_fill_num_arr(
        random_arr_diapason[0], random_arr_diapason[1], arr_num_of_elem
    ),
    "\nДиапазон поиска: ",
    seek_diapason,
    "\nИндексы чисел в диапазоне: ",
    seek_ind_nums_in_diapason(seek_diapason[0], seek_diapason[1], random_arr),
)
