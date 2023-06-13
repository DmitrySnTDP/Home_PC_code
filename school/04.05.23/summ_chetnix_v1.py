from random import *
n = 10
summ = 0
A = [0]*n
A = [randint(1,50) for i in range(n)]
for i in A:
    if i%2==0:
        summ+=i
print(summ)
