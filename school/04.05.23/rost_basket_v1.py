from random import *
n = 10
count = 0
A = [0]*n
A = [randint(165,195) for i in range(n)]
for i in A:
    if i>180 and i<190:
        count+=1
print(count)
