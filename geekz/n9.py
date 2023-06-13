n = open(file='9.txt')
A = []
a = int(n.readline())
b = int(n.readline())
#  на 1001 сроке файла записал число 9999 как ориентир
while b!=9999:
    if (a+b)%3==0 and (a*b)%10==8:
        A.append(a*b)
    a = b
    b = int(n.readline())
n.close()
print(len(A), max(A))