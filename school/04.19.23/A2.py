def NOD(a,b):
    x,y = a,b
    while a!=0 and b!=0:
        if a>b:
            a-=b
        else:
            b-=a
    if a==0:
        print(f'НОД({x},{y})={b}')
    else:
        print(f'НОД({x},{y})={a}')

a,b = map(int,input().split())
NOD(a,b)