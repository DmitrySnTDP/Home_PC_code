f = open('17_8.txt')
numbers = f.readlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

count_1 = 0
count_2 = 0
n1 = 10001
n2 = 10001
n1_max = 0
n2_max = 0
for i in numbers:
    if i%6==0:
        count_1+=1
        n1 = min(n1,i)
        n1_max = max(n1_max, i)
    if i%14==0:
        count_2+=1
        n2 = min(n2,i)
        n2_max = max(n2_max, i)

if n1>n2:
    print(count_1,n1_max)
else:
    print(count_2,n2_max)