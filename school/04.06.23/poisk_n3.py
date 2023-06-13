from random import*
a = 0
n = 10
A = [0]*n
A = [randint(100,200) for i in range(n)]
for i in A:
    if i%10==2:
        a = i
        break
print('Массив:\n', *A)
if a>=100:
    print(f'Нашли: A[{A.index(a)}]={a}')
else:
    print('Не нашли')
