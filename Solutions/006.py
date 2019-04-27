# Сумма квадратов первых десяти натуральных чисел равна
#
# 1^2 + 2^2 + ... + 10^2 = 385
# Квадрат суммы первых десяти натуральных чисел равен
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
# 3025 − 385 = 2640.
#
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

import math


def get_square_sum(array):
    values = []
    for i in array:
        values.append(math.pow(i, 2))
    return sum(values)


def get_square_of_sum(array):
    values = []
    for i in array:
        values.append(i)
    return math.pow(sum(values), 2)


print(get_square_of_sum(range(1, 101)) - get_square_sum(range(1, 101)))
