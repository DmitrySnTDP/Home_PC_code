def sov(n):
    summ = 0
    
    for i in range(1,n):
        if n%i==0:
            summ+=i

    return True if summ==n else False

n = int(input('Введите натуральное число:\n'))

print(f'Число {n} совершенное.') if sov(n) else print(f'Число {n} не совершенное.')