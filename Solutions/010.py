# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.

# python 3.7.3


def is_simple(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


prime_numbers = []

for x in range(1, 2000000):
    if is_simple(x):
        prime_numbers.append(x)

print(f'Сумма всех простых чисел до 2000000 равна: {sum(prime_numbers)}')
