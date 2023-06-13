a,b=map(int,input('Введите 2 числа').split())
x=a
y=b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print('НОД(',x,',',y,')=',max(a,b),sep='')
