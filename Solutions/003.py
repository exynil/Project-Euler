# Простые делители числа 13195 - это 5, 7, 13 и 29.
#
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

from itertools import count

number = 600851475143

for x in count(2):
    while number % x == 0:
        number /= x
    if number == 1:
        print(x)
        break

