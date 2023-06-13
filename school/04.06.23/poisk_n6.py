a = input('Массив:\n')
a = a.split()
A = [0]*len(a)
A = [int(i) for i in a]
count = 0
n = 0
for i in A:
    if i>n:
        count=1
        n = i
    elif i==n:
        count+=1
print('Максимальное значение:',n)
print('Количество элементов:',count)