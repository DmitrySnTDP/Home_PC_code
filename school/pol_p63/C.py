n = int(input())
a = input()
a = a.split()
A = [0]*n
A = [int(i) for i in a]
m = max(A)
count = 0
for i in A:
    if m==i:
        count+=1

print(m,count)