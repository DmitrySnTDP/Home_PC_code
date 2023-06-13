# Задание 1

# def summa_n(x):
#     n = 1
#     s = 0
#     for i in range(x):
#         s=s+n
#         n = n+1
#     return s

# k = int(input('Введите число: '))

# print(summa_n(k))

# Задание 2

# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#     return

# for i in range(5):
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#     print('Следующий.')

# Задание 3

# def summa_2(x,y):
#     s=x+y
#     return s

# def minus_2(x,y):
#     s=x-y
#     return s

# def umn_2(x,y):
#     s=x*y
#     return s

# def delit_2(x,y):
#     s=x/y
#     return s

# f = open('kalkulator.txt', 'a')
# num1 = int(input('Введи первое число: '))
# num2 = int(input("Введи второе число: "))
# oper = input('введи +,-,* или /  ')

# if oper == '+':
#     f.write(str(summa_2(num1, num2)))
# elif oper == '-':
#     f.write(str(minus_2(num1, num2)))
# elif oper == '*':
#     f.write(str(umn_2(num1, num2)))
# elif oper == '/':
#     f.write(str(delit_2(num1,num2)))
# f.close()