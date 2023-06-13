A = [0]*5
a = input('Массив:\n')
a = a.split()
A = [int(i) for i in a]
x = 0
n = 0
for i in A:
    if i>x:
        x = i
        n1 = n
    n+=1
n = 0
for i in A:
    if i==x and n!=n1:
        print(f'Максимальный элемент: A[{n1}]={x}')
        print(f'Второй максимум: A[{n}]={i}')
        break
    n+=1
