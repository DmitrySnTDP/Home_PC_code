n = int(input())
A = [0]*n
a = input()
x = int(input())
a = a.split()
A = [int(i) for i in a]
k = 0
n = 0
for i in A:
    if i==x and k==0:
        s = str(n+1)
        k = 1
    elif i==x:
        s = s+' '+str(n+1)
    n+=1
if k==1:
    print(s)
else:
    print(-1)
