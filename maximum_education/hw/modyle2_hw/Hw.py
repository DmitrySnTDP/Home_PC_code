# задание 1

# def calculate():
#     print('Возможные операции')
#     print('+ -сложение')
#     print('- -вычитание')
#     print('* -умножение')
#     print('/ -деление')

#     operation = input('Введи операцию\n')

#     if operation == '+':
#         try:
#             input_num1 = int(input('Введи первое число\n'))
#             input_num2 = int(input('Введи второе число\n'))
#         except ValueError:
#             print('Числа некорректны')
#         else:
#             print(input_num1+input_num2)


#     elif operation == '-':
#         try:
#             input_num1 = int(input('Введи первое число\n'))
#             input_num2 = int(input('Введи второе число\n'))
#         except ValueError:
#             print('Числа некорректны')
#         else:
#             print(input_num1-input_num2)


#     elif operation == '*':
#         try:
#             input_num1 = int(input('Введи первое число\n'))
#             input_num2 = int(input('Введи второе число\n'))
#         except ValueError:
#             print('Числа некорректны')
#         else:
#             print(input_num1*input_num2)


#     elif operation == '/':
#         try:
#             input_num1 = int(input('Введи первое число\n'))
#             input_num2 = int(input('Введи второе число\n'))
#         except ValueError:
#             print('Числа некорректны')

#         else:
#             print(input_num1/input_num2)
#     else:
#         print('Неккоретная операция')
    
#     calculate()

# calculate()

# Задание 2


# a = int(input('Введите значение a: '))
# b = int(input('Введите значение b: '))
# c = int(input('Введите значение c: '))

# print(b*b-4*a*c)

# задание 3

import math

a = int(input('Введите число\n'))
q = math.sqrt(a)
print('Корень из числа ',a,' равен ',q)