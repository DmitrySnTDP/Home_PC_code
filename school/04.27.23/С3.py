def isPrime(n):
    k = 2
    while k*k<=n and n%k!=0:
        k+=1

    return (k*k>n and n!=1)

n = int(input('Введите натуральное число:\n'))
m = n

while isPrime(n) and n!=0:
    n=n//10

if n>0:
    print(f'Число {m} не гиперпростое')
else:
    print(f'Число {m} гиперпростое')
