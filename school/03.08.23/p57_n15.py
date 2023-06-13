x,y=map(float,input('Введите координаты точки:').split())

print('Yes') if y<1 else print('No')
print('Yes') if y<-x else print('No')
print('Yes') if x*x+y*y<1 else print('No')
print('Yes') if (x-1)**2+y*y<1 else print('No')