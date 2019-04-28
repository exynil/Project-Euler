# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#
# a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

import math

for a in range(1, 1000):
    for b in range(a, 1000):
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        if a + b + c == 1000:
            print(f'{a} + {b} + {c} = {a + b + c}')
            print(f'{a}^2 + {b}^2 = {c}^2')
            print(f'{a} * {b} * {c} = {a * b * c}')
            break
    else:
        continue
    break

