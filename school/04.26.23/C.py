def revers(n):
    s=''
    for i in range(len(n)-1,-1,-1):
        s+=n[i]
    return int(s)
n = input('Введите натуральное число:\n')
print(f'После переворота: {revers(n)}')
