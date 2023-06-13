n = int(input())
A = [0]*n
a = input()
a = a.split()
A = [int(i) for i in a]
x = 0
k = 0
for i in A:
    if i>0 and k==0 and i%2==0:
        y = i
        k = 1
    elif i>0 and k==1 and i%2==0 and y>i:
        y = i
for i in A:
        if i>x and i%2==0:
            x = i

     
print(y,x)
print(-1,-1)
