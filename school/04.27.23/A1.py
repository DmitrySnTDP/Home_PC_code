def sorter(a,b,c):
    if a>b and a>c:
        x = a
    elif b>a and b>c:
        x = b
    else:
        x = c
    if a<b and a<c:
        z = a
    elif b<a and b<c:
        z = b
    else:
        z = c
    if a!=x and a!=z:
        y = a
    elif b!=x and b!=z:
        y = b
    else:
        y = c
    return z,y,x
a,b,c = map(int,input().split())
print(*sorter(a,b,c))
