a,b,c=map(int,input().split())
if max(a,b,c)!=a and min(a,b,c)!=a:
    print('Среднее число:',a)
elif max(a,b,c)!=b and min(a,b,c)!=b:
    print('Среднее число:',b)
else:
    print('Среднее число:',c)
    
