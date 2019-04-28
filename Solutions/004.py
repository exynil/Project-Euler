# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
# полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# python 3.7.3


def is_palindrome(string):
    if string[::-1] == string:
        return True
    return False


for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if is_palindrome(str(i * j)):
            print(f'{i} * {j} = {i * j}')
            break
    else:
        continue
    break
