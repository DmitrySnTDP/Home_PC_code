def NOD(a,b):
    while a!=0 and b!=0:
        if a>b:
            a %= b
        else:
            b %= a
    if a>b:
        return a
    else:
        return b
a,b = map(int,input('Введите два натуральных числа:\n').split())
print(f'НОД({a},{b})={NOD(a,b)}')
