# Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру, 7-ое треугольное число
# равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Перечислим делители первых семи треугольных чисел:
#
#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
#
# Каково первое треугольное число, у которого более пятисот делителей?


import math
from itertools import count


def get_amount_of_dividers(number):
    amount = 2
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            amount += 2
    if math.sqrt(number) is float:
        amount -= 1
    return amount


def main():
    for i in count(1):
        number = sum(range(1, i))
        amount_of_dividers = get_amount_of_dividers(number)
        if amount_of_dividers >= 500:
            print(f'{number} - кол-во делителей: {amount_of_dividers}')
            break


if __name__ == '__main__':
    main()
