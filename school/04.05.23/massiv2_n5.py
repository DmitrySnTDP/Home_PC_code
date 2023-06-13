n = int(input('Введите размер массива:'))
A = [0]*n
for i in range(n):
    if i<2:
        A[i] = 1
    else:
        A[i] = A[i-1]+A[i-2]
print(*A)