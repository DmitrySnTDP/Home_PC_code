def Summ(n):
    s = 0
    for i in n:
        s+=int(i)
    print(f'Сумма цифр числа {n} равна {s}.')
n = input()
Summ(n)