a=input()
n=0
for i in a:
    if i.isdigit():
        n=0
    else:
        n=1
        break
if n==0:
    print('Да')
else:
    print('Нет')
    
