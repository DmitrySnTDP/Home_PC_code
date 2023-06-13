n = int(input())
A=[0]*n
a=input().split()
A=[int(i) for i in a]
A.sort()
print(A[0],A[1],A[2])