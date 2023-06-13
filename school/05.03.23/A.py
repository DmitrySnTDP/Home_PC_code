def Nod(a,b):
    if a==0 or b==0:
        return a + b
    if  a > b:
        return Nod(a-b,b)
    else: 
        return Nod(a,b-a)

a,b = map(int,input('Введите два натуральных чила:\n').split())
n = Nod(a,b)
print(f'НОД({a},{b})={n}')