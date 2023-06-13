def prost(a,b):
    for i in range(2,min(a,b)+1):
            return (a%i==0 and b%i==0)

a,b = map(int,input('Введите два натуральных числа:\n').split())

if prost(a,b):
    print(f'Числа {a} и {b} не взаимно простые.')
else:
    print(f'Числа {a} и {b} взаимно простые.')