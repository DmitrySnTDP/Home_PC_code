from random import randint
a,b = map(int,input('Введите границы диапазона:').split())
m =[randint(a,b) for i in range(10)]
print(*m)
