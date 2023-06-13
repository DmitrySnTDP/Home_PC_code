from random import randint
A = [0]*10
A = [randint(10,100) for i in range(10)]
a = A[0]
for i in A:
    if i<a:
        a = i
print('Массив:')
print(*A)
print(f'Минимальный элемент: A[{A.index(a)}]={a}')