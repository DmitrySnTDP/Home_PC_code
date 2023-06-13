from random import *
n = 10
count = 0
summ = 0
A = [0]*n
A = [randint(1,50) for i in range(n)]
for i in A:
    if i%5==0:
        summ+=i
        count+=1
print(summ/count)
