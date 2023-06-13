def Summ(n):
    s = 0
    for i in n:
        s+=int(i)
    return s
n = input('Введите натуральное число:\n')
print(f'Сумма цифр числа {n} равна {Summ(n)}')
