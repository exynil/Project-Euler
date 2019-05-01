# Следующая повторяющаяся последовательность определена для множества натуральных чисел:
#
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)
#
# Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не
# доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности
# оканчиваются на 1.
#
# Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
#
# Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.

# python 3.7.3


def collatz_function(number):
    followers = [number]
    if number == 1:
        return followers
    if number % 2 == 0:
        return followers + collatz_function(number / 2)
    else:
        return followers + collatz_function(number * 3 + 1)


def main():
    element = 0
    followers_length = 0
    for i in range(1, 1000000):
        length = len(collatz_function(i))
        if length > followers_length:
            element, followers_length = i, length

    print(f'Элемент: {element}')
    print(f'Длина последовательности: {followers_length}')


if __name__ == '__main__':
    main()
