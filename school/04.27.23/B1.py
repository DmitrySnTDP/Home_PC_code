def sokrat(a,b):
    x,y=a,b
    while x!=0 and y!=0:
        if x>y:
            x-=y
        else:
            y-=x
    if x!=0:
        n = x
    else:
        n = y
    a,b = a//n,b//n
    l = str(a,'/',b)
    return l
a,b = map(int,input('Введите числитель и знаменатель дроби:').split())
print('После сокращения:',sokrat(a,b))
