f = open('17_7.txt')
numbers = f.readlines()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
n = 999
for i in numbers:
    if i%10==6 and len(str(i))==3:
        n = min(n,i)

count = 0
min_sum = 1000001
for i in range(len(numbers)-1):
    para = numbers[i:i+2]
    if ((len(str(para[0]))==3 and len(str(para[1]))!=3) or (len(str(para[0]))!=3 and len(str(para[1]))==3) and sum(para)%n==0):
        count+=1
        min_sum = min(min_sum, sum(para))

print(count,min_sum)