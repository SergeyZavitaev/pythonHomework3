# Задача 30:  Заполните массив элементами
# арифметической прогрессии. Её первый элемент,
#  разность и количество элементов нужно ввести
# с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Functions


def input_number(text):
    return int(input(text))


def count_progres_num(a1, num, d):
    return a1 + (num - 1) * d


def fill_arr_as_progress(a1, size, d):
    array = []
    for number in range(1, size + 1):
        array.append(count_progres_num(a1, number, d))
    return array


# Solution

a1_first_elem = input_number("Введите первый элемент прогрессии: ")
d_diff = input_number("Введите разность прогрессии: ")
arr_size = input_number("Введите колличество элементов прогрессии: ")

print(fill_arr_as_progress(a1_first_elem, arr_size, d_diff))
