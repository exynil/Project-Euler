# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
#
# Какое число является 10001-ым простым числом?

# python 3.7.3


from itertools import count


def is_simple(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


counter = 0

for x in count(2):
    if is_simple(x):
        counter += 1
        if counter == 10001:
            print(f'10001 простым числом является - {x}')
            break
