def NOD_and_NOK(a,b):
    x,y = a,b
    
    while x!=0 and y!=0:
        if x>=y:
            x%=y
        else:
            y%=x
            
    nod = x+y
    nok = a*b//nod

    return nod,nok

a,b = map(int,input('Введите два натуральных числа:\n').split())

n = NOD_and_NOK(a,b)

print(f'НОД({a},{b})={n[0]}')
print(f'НОК({a},{b})={n[1]}')