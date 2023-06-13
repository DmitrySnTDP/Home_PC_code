a,b=map(int,input('Введите 2 числа:').split())
x=a
y=b
k1=0
k2=0
while x!=y:
    k1+=1
    if x>y:
        x-=y
    else:
        y-=x
x=a
y=b
while x!=0 and y!=0:
    k2+=1
    if x>y:
        x%=y
    else:
        y%=x
e=max(x,y)
print('НОД(',a,',',b,')=',e,sep='')
print('Обычный алгоритм:',k1,sep='')
print('Модифицированный:',k2,sep='')
