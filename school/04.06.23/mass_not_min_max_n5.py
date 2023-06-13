from random import randint
A = [0]*10
A = [randint(10,100) for i in range(10)]
a = A[0]
b = A[0]
for i in A:
    if i%2==0 and i<a:
        a = i
    if i%2==0 and i>b:
        b = i
print('Массив:')
print(*A)
print('Минимальный чётный:',a)
print('Максимальный чётный:',b)