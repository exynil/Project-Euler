# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# python 3.7.3


# Фукнция получает число и возвращает все множители числа
def get_multipliers(number):
    multipliers = []
    for i in range(2, number + 1):
        while True:
            if number % i == 0:
                multipliers.append(i)
                number /= i
            else:
                break
    return multipliers


# Функция принимает массив чисел и возвращает наименьшее кратное число.
def get_lcm(array):
    multipliers = get_multipliers(array[0])
    for i in array:
        for j in get_multipliers(i):
            if j not in multipliers:
                multipliers.append(j)
            elif get_multipliers(i).count(j) > multipliers.count(j):
                for k in range(0, get_multipliers(i).count(j) - multipliers.count(j)):
                    multipliers.append(j)
    lcm = 1
    for m in multipliers:
        lcm *= m
    return lcm


print(get_lcm(range(1, 20)))
