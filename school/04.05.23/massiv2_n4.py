from random import *
n = 10
A = [randint(0,100) for i in range (n)]
B = [i for i in A if i<50]
C = [i  for i in A if i>=50]
print('Массив:\n',*A)
print(f'Ср. арифм. элементов <50:{sum(B)/len(B)}')
print(f'Ср. арифм. элементов >=50:{sum(C)/len(C)}')
      
