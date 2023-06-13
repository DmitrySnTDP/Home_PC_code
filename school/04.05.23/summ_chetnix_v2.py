n = 5
summ = 0
A = [0]*n
A = [int(input()) for i in range(n)]
for i in A:
    if i%2==0:
        summ+=i
print(summ)
