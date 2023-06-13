from random import *
n = 10
count = 0
summ = 0
A = [0]*n
A = [randint(1,50) for i in range(n)]
B = [i for i in A if i%10==5]
print(A)
print(sum(B)/len(B))
