from random import * 


count = 0
count2 = 0
A = [0]*10
A = [randint(0,5) for i in range(10)]
print('Массив:')
print(*A)

x = int(input('Что ищем:'))

for i in A:
    if i==x:
        count+=1
        print(f'A[{count2}]={i}')
    count2+=1

if count == 0:
    print('Не нашли.')
    