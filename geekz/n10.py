n = open(file='10.txt')
A = []
a = int(n.readline())
b = int(n.readline())
c = int(n.readline())
# на 1001 сроке файла записал значение 55555 как ориентир
while c!=55555:
    if a%9==0 or b%9==0 or c%9==0:
        A.append(a*b*c)
    a,b = b,c
    c = int(n.readline())
n.close()
print(len(A), min(A))