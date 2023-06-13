def prost_somn(n):
    if n==1:
        return k
    elif n%2==0:
        k = 2
        prost_somn(n//2)
    elif n%3==0:
        k = 3
        prost_somn(n//3)
    elif n%5==0:
        k = 5
        prost_somn(n//5)
    elif n%7==0:
        k = 7
        prost_somn(n//7)
    elif n%11==0:
        k = 11
        prost_somn(n//11)
    elif n%13==0:
        k = 13
        prost_somn(n//13)
    elif n%17==0:
        k = 17
        prost_somn(n//17)
    elif n%19==0:
        k = 19
        prost_somn(n//19)
    

n = int(input('Введите натуральное число:\n'))
print(prost_somn(n))