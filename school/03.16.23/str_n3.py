a=input()
n=0
m=0
for i in a:
    if i in ['0']:
        n+=1
    else:
        m+=1
print('Нулей:',n)
print('Единиц:',m)
