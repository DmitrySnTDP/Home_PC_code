n = int(input())
A = [0]*n
a = input()
a = a.split()
x = int(input())
A = [int(i) for i in a]
count = 0
for i in A:
    if x==i:
        count+=1
print(count)
