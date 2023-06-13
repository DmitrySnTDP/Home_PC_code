n = int(input())
A = [0]*n
a = input().split()
A = [int(i) for i in a]
if n%2==0:
    for i in range(0,n,2):
        k = A[i]
        A[i] = A[i+1]
        A[i+1] = k
else:
    for i in range(0,n-1,2):
        A[i],A[i+1]=A[i+1],A[i]
print(*A)