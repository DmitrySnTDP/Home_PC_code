# Задание1

t = int(input("Введите температуру: "))

if t< -30:
    print("Очень холодно")
elif t>= -30 and t< -5:
    print("Холодно")
elif t>= -5 and t <10:
    print("Прохладно")
elif t>= 10 and t< 25:
    print("Тепло")
elif t>= 25 and t< 35:
    print("Жарко")
elif t>= 35:
    print("Очень жарко")

# Задание 2

import random

money = ["орёл","решка"]

m = random.choice(money)
n = input("орёл или решка?")
if n == m:
    print("Выиграл")
else:
    print("Проиграл")

# Задание3

n = []
l = int(input("Введите колличество чисел: "))

for i in range(l):
    N = int(input("Введите число: "))
    n.append(N)

n.sort()

print(n)
