# 2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
#
# Какова сумма цифр числа 2^1000?


# python 3.7.3

import math


def main():
    print(sum(map(int, list(str(int(math.pow(2, 1000)))))))


if __name__ == '__main__':
    main()
