# Задание 1

numbers = []

for i in range(101):
    numbers.append(i)

print(numbers)

# Задание 2    

import random

animals = []

for i in range(3):
    a = input("Введите животное: ")
    animals.append(a)

descriptions = []

for i in range(3):
    d = input("Введите описание: ")
    descriptions.append(d)

for i in range(3):
    print(random.choice(animals), random.choice(descriptions))

# Задание 3

import random

a =[0,1,2,3,4,5]
numbers = []

for i in range(30):
    n = random.choice(a)
    numbers.append(n)

print(numbers.count(5))