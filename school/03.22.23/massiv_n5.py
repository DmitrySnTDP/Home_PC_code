from random import randint
a,b=map(int,input('Введите границы диапазона:').split())
if a>b:
    c=a
    a=b
    b=c
m=[0]*10
for i in range(10):
    if i>=5:
        m[i]=m[i-5]**2
    elif i<5:
        m[i]=randint(a,b)
print(*m)
