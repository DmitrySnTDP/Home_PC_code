def revers(n):
    a =''
    for i in range(len(n)-1,-1,-1):
        a+=n[i]
    print(f'После переворота: {a}')
n = input()
revers(n)