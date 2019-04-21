# Задача 1

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
amount = 0
for n in range(0, 1000):
    if n % 3 == 0 or n % 5 == 0:
        amount += n
print(amount)
