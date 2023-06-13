n = int(input())
A = [0]*n
a = input().split()
A = [int(i) for i in a]

l_list = []
num_list = []
num = A[0]
l = 1
k = 0

for i in range(1,n):

    if A[i-1]!=A[i]:
        l_list.append(l)
        num_list.append(num)

    elif A[i-1]==A[i]==num:
        l+=1

    elif A[i-1]==A[i]:
        k = 1
        l_list.append(l)
        num_list.append(num)
        l = 2 
        num = A[i]
l_list.append(l)
num_list.append(num)

if k==1:
    print(num_list[l_list.index(max(l_list))],max(l_list))
else:
    print(num,l)

