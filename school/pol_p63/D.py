n = int(input())
a = input()
a = a.split()
A = [0]*n
A = [int(i) for i in a]
m = min(A)
k = 0
for i in range(n):
    if A[i]==m and k==0:
        s = str(i+1)
        k = 1
    elif A[i]==m:
        s = s+' '+str(i+1)
print(s)