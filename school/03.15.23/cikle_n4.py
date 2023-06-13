a=int(input('Введите число:'))
n=0
while a>0:
    if a%10==1:
        n+=1
    a=a//10
print(n)
