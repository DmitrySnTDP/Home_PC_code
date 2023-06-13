from random import * 


count = 0
A = [0]*10
A = [randint(0,5) for i in range(10)]
print('Массив:')
print(*A)

for i in range(8):
    if A[i]==A[i+1]:
        count+=1
        print(f'A[{i}]=A[{i+1}]={A[i]}')
if count==0:
    print('Нет.')